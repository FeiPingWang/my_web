from sqlalchemy import Column, Integer, String, DateTime
from models import Base, new_session, Model, engine
import datetime
from flask import flash


# 用户表
class User(Base):
    __tablename__ = 'User'

    user_id = Column(Integer, primary_key=True, nullable=False)
    user_name = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    phone = Column(String(20))
    email = Column(String(30))
    brief = Column(String(140), default='new guy')
    ct = Column(DateTime, default=datetime.datetime.utcnow)
    
    def __init__(self, form):
        self.user_name = form.get('username', '')
        self.password = form.get('password', '')
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
            filter(User.user_name == name, User.password == password).first()
        print(result)
        session.close()
        # result is a tuple
        return result
    
    
    @classmethod
    def get_user_by_id(cls, user_id):
        pass
        