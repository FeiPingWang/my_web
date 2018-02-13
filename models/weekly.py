from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models import Base
from datetime import datetime
from models.users import User


# 周报表
class Weekly(Base):
    __tablename__ = 'Week_Note'

    note_id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), nullable=False)
    content = Column(String, nullable=False)
    ct = Column(DateTime, default=datetime.datetime.utcnow)
    mt = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('User.user_id'))
    comment = Column(String)
    