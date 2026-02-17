import boto3
import time
import statistics
import os

athena = boto3.client("athena")
sns = boto3.client("sns")

DATABASE = os.environ["ATHENA_DB"]
TABLE = os.environ["ATHENA_TABLE"]
SNS_TOPIC = os.environ["SNS_TOPIC"]
OUTPUT_LOCATION = os.environ["ATHENA_OUTPUT"]

def run_query(query):
    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={"Database": DATABASE},
        ResultConfiguration={"OutputLocation": OUTPUT_LOCATION},
    )
    query_execution_id = response["QueryExecutionId"]

    while True:
        result = athena.get_query_execution(QueryExecutionId=query_execution_id)
        state = result["QueryExecution"]["Status"]["State"]
        if state in ["SUCCEEDED", "FAILED", "CANCELLED"]:
            break
        time.sleep(2)

    results = athena.get_query_results(QueryExecutionId=query_execution_id)
    rows = results["ResultSet"]["Rows"]
    return rows

def lambda_handler(event, context):

    query = f"""
    SELECT date(line_item_usage_start_date) as usage_date,
           SUM(line_item_unblended_cost) as total_cost
    FROM {TABLE}
    GROUP BY 1
    ORDER BY 1 DESC
    LIMIT 8;
    """

    rows = run_query(query)

    costs = []
    for row in rows[1:]:
        costs.append(float(row["Data"][1]["VarCharValue"]))

    latest = costs[0]
    historical_avg = statistics.mean(costs[1:])

    if latest > historical_avg * 1.3:
        message = f"Cost anomaly detected! Latest: {latest}, Avg: {historical_avg}"
        sns.publish(
            TopicArn=SNS_TOPIC,
            Message=message,
            Subject="FinOps Cost Anomaly Alert"
        )

    return {"latest": latest, "average": historical_avg}
