from pydantic_settings import BaseSettings


class FuncLLMSettings(BaseSettings):
    model_config = {"env_prefix": "FUNC_LLM_"}

    gcp_project_id: str | None = None
    gcp_region: str = "europe-west1"
    azure_openai_api_key: str | None = None
    azure_openai_resource_name: str | None = None
    azure_openai_api_version: str = "2024-12-01-preview"
