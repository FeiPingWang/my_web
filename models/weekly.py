from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models import Base, new_session
from datetime import datetime
from models.users import User
from models.board import Board


# 周报表
class Weekly(Base):
    __tablename__ = 'Week_Note'

    note_id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), nullable=False)
    content = Column(String, nullable=False)
    ct = Column(DateTime, default=datetime.utcnow)
    mt = Column(DateTime, nullable=False, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('User.user_id'))
    board_id = Column(Integer, ForeignKey('Board.board_id'))
    
    def __init__(self, form, user_id):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        # self.board_id = form.get('board_id', '')
        self.board_id = 1
        self.mt = self.ct
        self.user_id = user_id
        
    
    @classmethod
    def get_all_note(cls):
        session = new_session()
        note = session.query(Weekly.title, Weekly.ct).all()
        return list(note)
        
       

