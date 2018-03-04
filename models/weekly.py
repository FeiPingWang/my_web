from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models import Base, new_session
from datetime import datetime
from tools.utils import generate_uuid
from tools.orm import Query_all, convert_to_dict


# 周报表
class Weekly(Base):
    __tablename__ = 'Week_Note'

    id = Column(String(32), default=generate_uuid, primary_key=True, nullable=False)
    title = Column(String(50), nullable=False)
    content = Column(String, nullable=False)
    replys = Column(Integer, nullable=False, default=0)
    views = Column(Integer, nullable=False, default=0)
    ct = Column(DateTime, default=datetime.utcnow)
    mt = Column(DateTime, nullable=False, default=datetime.utcnow)
    user_id = Column(String(32), ForeignKey('User.id'))
    board_id = Column(Integer, ForeignKey('Board.id'))
    
    def __init__(self, form, user_id):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.board_id = form.get('board_id', '')
        self.mt = self.ct
        self.user_id = user_id
        
    def __repr__(self):
        return "<Note(id='{}', title='{}', content='{}', ct='{}')>".format(
            self.id, self.title, self.content, self.ct
        )
        
    @classmethod
    def get_all_note(cls):
        note = Query_all(Weekly.id, Weekly.title, Weekly.ct)
        return note
    
    
if __name__ == '__main__':
    session = new_session()
    note = session.query(Weekly).filter(Weekly.id == '7dee3463990f4bb99dbac63f77046eb9').first()
    print(note)
    session.close()
    print(note)
    
       

