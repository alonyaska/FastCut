from datetime import datetime
from pydantic import BaseModel, ConfigDict, HttpUrl


class SLink(BaseModel):
    id: int
    user_id: int
    full_url: str
    short_key: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SLinkCreate(BaseModel):
    url: HttpUrl