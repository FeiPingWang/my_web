from sqlalchemy import Column, Integer, String, DateTime
from models import Base, new_session, Model, engine
import datetime
from flask import flash
from werkzeug.security import generate_password_hash, check_password_hash
import uuid


def generate_uuid():
    return uuid.uuid4().hex


# 用户表
class User(Base):
    __tablename__ = 'User'

    user_id = Column(String(32), default=generate_uuid, primary_key=True, nullable=False)
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
            self.user_id, self.user_name, self.email, self.brief
        )
    
    @classmethod
    def validate(cls, form):
        name = form.get('username', '')
        password = form.get('password', '')
        session = new_session()
        result = session.query(User.user_id, User.user_name, User.password).\
            filter(User.user_name == name).first()
        session.close()
        if result is not None:
            if(check_password_hash(result[2], password) == True):
                return result
        else:
            return None
    
    
    @classmethod
    def get_user_by_id(cls, user_id):
        pass
        