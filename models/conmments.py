from models import Base
from tools.utils import generate_uuid
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from flask import g


class Comments(Base):
    __tablename__ = 'Comments'

    id = Column(String(32), default=generate_uuid, primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    note_id = Column(String(32), nullable=False)
    user_id = Column(String(32), nullable=False)
    ct = Column(DateTime, default=datetime.utcnow)
    
    def __init__(self, content, user_id, note_id):
        # TODO: 优化参数
        self.content = content
        self.user_id = user_id
        self.note_id = note_id
        
    def __repr__(self):
        return "<Comments(id='{}', contnet='{}', ct='{}', note_id='{}', user_id='{}')>".format(
            self.id, self.content, self.ct, self.note_id, self.user_id
        )
    
    @classmethod
    def find_by_note_id(cls, id):
        comments = g.my_session.query(cls).filter(cls.note_id == id).order_by(cls.ct.desc()).all()
            # get 可以根据主键id得到实例
        return list(comments)