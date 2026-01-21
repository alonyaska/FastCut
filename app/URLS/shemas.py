from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SLinks(BaseModel):

    id:int
    user_id:int
    full_url:str
    short_key:str
    created_at:datetime.utcnow()


    model_config = ConfigDict(from_attributes=True)