from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models import Base
from datetime import datetime
from tools.utils import generate_uuid
from flask import g, current_app


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
    type_id = Column(Integer, ForeignKey('Types.id'))
    
    def __init__(self, form, user_id):
        # 这里一定要 ** 去除字符串 **，否则jquery赋值html会出错
        self.title = form.get('title', '').replace("\r\n",'')
        self.content = form.get('content', '').replace("\r\n",'')
        self.type_id = form.get('type_id', '-1')
        print('ty ', self.type_id)
        self.mt = self.ct
        self.user_id = user_id
        
    def __repr__(self):
        return "<Note(id='{}', title='{}', content='{}', ct='{}')>".format(
            self.id, self.title, self.content, self.ct
        )
    
    def incre_views(self):
        self.views += 1
        g.my_session.commit()

    def incre_replys(self):
        self.replys += 1
        g.my_session.commit()

