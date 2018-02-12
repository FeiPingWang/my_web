from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String


engine = create_engine("mysql://root:123456@localhost:3306/moneyfree?charset=utf8", echo=False)
Session = sessionmaker(bind=engine)


# 提供session的工厂函数
def new_session():
    return Session()


# 基类
class Model(object):

    @classmethod
    def _add(cls, self):
        session = new_session()
        session.add(self)
        session.commit()
        session.close()
    
    @classmethod
    def _delete(cls, self):
        session = new_session()
        session.delete(self)
        session.commit()
        session.close()
        
        
# 提供给具体的model继承
Base = declarative_base(cls=Model)