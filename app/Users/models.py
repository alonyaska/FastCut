from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from  app.database import Base



class  UsersModel(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False, unique=True)

