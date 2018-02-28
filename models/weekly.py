from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models import Base, new_session
from datetime import datetime
from tools.utils import generate_uuid


# 周报表
class Weekly(Base):
    __tablename__ = 'Week_Note'

    note_id = Column(String(32), default=generate_uuid, primary_key=True, nullable=False)
    title = Column(String(50), nullable=False)
    content = Column(String, nullable=False)
    ct = Column(DateTime, default=datetime.utcnow)
    mt = Column(DateTime, nullable=False, default=datetime.utcnow)
    user_id = Column(String(32), ForeignKey('User.user_id'))
    board_id = Column(Integer, ForeignKey('Board.board_id'))
    
    def __init__(self, form, user_id):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.board_id = form.get('board_id', '')
        self.mt = self.ct
        self.user_id = user_id
        
    @classmethod
    def get_all_note(cls):
        session = new_session()
        # TODO: query封装一层，每次返回列表字典，这样取值时比较直观
        note = session.query(Weekly.title, Weekly.ct).all()
        session.close()
        return list(note)
        
       

