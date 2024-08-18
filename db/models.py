from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    author = Column(String)
    text = Column(String)


