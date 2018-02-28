from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models import Base
from models import new_session
from tools.orm import Query_all


# 论坛的版块
class Board(Base):
    __tablename__ = 'Board'
    
    board_id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), nullable=False)
    
    def __repr__(self):
        return "<Board(id='{}', title='{}')>".format(
            self.id, self.title
        )
    
    # 返回所有的版块
    @classmethod
    def get_all_board(cls):
        return Query_all(Board.board_id, Board.title)
        # session = new_session()
        # board_list = session.query(Board.board_id, Board.title).all()
        # return list(board_list)
        