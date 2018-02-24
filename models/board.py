from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models import Base


# 论坛的版块
class Board(Base):
    __tablename__ = 'Board'
    
    board_id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), nullable=False)
    
    def __repr__(self):
        return "<Board(id='{}', title='{}')>".format(
            self.id, self.title
        )