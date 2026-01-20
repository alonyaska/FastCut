from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from  app.database import Base


class URLsModel(Base):
    __tablename__ = "URL"


    id = Column(Integer,primary_key=True)
    user_id = Column(ForeignKey("users.id"))
    full_url = Column(String, nullable=False)
    short_key = Column(String, nullable=False, index=True, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow())
