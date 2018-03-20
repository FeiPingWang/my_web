from sqlalchemy import Column, Integer, String, DateTime, Boolean
from models import Base
import datetime
from flask import flash, g, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from tools.utils import generate_uuid
import os


# 用户表
class User(Base):
    __tablename__ = 'User'

    id = Column(String(32), default=generate_uuid, primary_key=True, nullable=False)
    user_name = Column(String(20), nullable=False)
    password = Column(String(100), nullable=False)
    avater_hash = Column(String(32), default='default.jpg')
    is_admin = Column(Boolean, default=False)
    phone = Column(String(20))
    email = Column(String(30))
    brief = Column(String(140), default='new guy')
    ct = Column(DateTime, default=datetime.datetime.utcnow)
    
    def __init__(self, form):
        self.user_name = form.get('username', '')
        self.password = generate_password_hash(form.get('password', ''))
        self.email = form.get('email', '')
        self.phone = form.get('phone', '')
        self.brief = form.get('brief', '')

    def __repr__(self):
        return "<User(id='{}', name='{}', email='{}', brief='{}')>".format(
            self.id, self.user_name, self.email, self.brief
        )

    def check_username_occupy(self):
        u = g.my_session.query(User).filter(User.user_name == self.user_name).first()
        if u is not None:
            return False
        return True

    @classmethod
    def validate(cls, form):
        name = form.get('username', '')
        password = form.get('password', '')
        
        result = g.my_session.query(cls).filter(User.user_name == name).first()
            
        if result is not None:
            if(check_password_hash(result.password, password) == True):
                return result
        else:
            return None
    
    @classmethod
    def update_avater(cls, id, avate_name):
        u = g.my_session.query(cls).filter(User.id == id).first()
        if not u.avater_hash is None:
            # 事先有老的头像
            old_avater = os.path.join(current_app.config['AVATER_IMG_PATH'], u.avater_hash)
            try:
                os.remove(old_avater)
            except:
                pass
        u.avater_hash = avate_name
        g.my_session.commit()
        return 'success'
