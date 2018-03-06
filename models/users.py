from sqlalchemy import Column, Integer, String, DateTime
from models import Base
import datetime
from flask import flash, g
from werkzeug.security import generate_password_hash, check_password_hash
from tools.utils import generate_uuid


# 用户表
class User(Base):
    __tablename__ = 'User'

    id = Column(String(32), default=generate_uuid, primary_key=True, nullable=False)
    user_name = Column(String(20), nullable=False)
    password = Column(String(100), nullable=False)
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
    
        