import os

class SecretsProvider:
    def get_secret(self, key: str) -> str:
        raise NotImplementedError

class EnvSecretsProvider(SecretsProvider):
    def get_secret(self, key: str) -> str:
        value = os.getenv(key)
        if not value:
            raise ValueError(f"Missing secret: {key}")
        return value

secrets_provider = EnvSecretsProvider()
