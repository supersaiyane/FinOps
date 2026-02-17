resource "aws_athena_database" "finops_db" {
  name   = "finops_billing"
  bucket = aws_s3_bucket.athena_results.bucket
}

resource "aws_glue_catalog_table" "cur_table" {
  name          = "finops_cur"
  database_name = aws_athena_database.finops_db.name
  table_type    = "EXTERNAL_TABLE"

  parameters = {
    classification = "parquet"
  }

  storage_descriptor {
    location      = "s3://${aws_s3_bucket.cur_bucket.bucket}/cur/"
    input_format  = "org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat"
    output_format = "org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat"

    ser_de_info {
      serialization_library = "org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe"
    }
  }
}