from pydantic import BaseModel


class CloudConfig(BaseModel):
    cloud: str | None = None
    project: str | None = None
    region: str | None = None
