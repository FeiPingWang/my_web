from sqlalchemy import Column, Integer, String
from models import Base


# 周报表
class Weekly(Base):
    __tablename__ = 'weekly'

    name = Column(String(20))
    password = Column(String(20))
    email = Column(String(30))
    brief = Column(String(140))
