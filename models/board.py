from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models import Base
from models import new_session
from tools.orm import Query_all


# 论坛的版块
class Board(Base):
    __tablename__ = 'Board'
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), nullable=False)
    
    def __repr__(self):
        return "<Board(id='{}', title='{}')>".format(
            self.id, self.title
        )
