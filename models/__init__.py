from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String


engine = create_engine("mysql+pymysql://root:123456@localhost:3306/moneyfree?charset=utf8", echo=False)
Session = sessionmaker(bind=engine)


# 提供session的工厂函数
def new_session():
    return Session()


# 基类
class Model(object):

    @classmethod
    def new(cls, self):
        session = new_session()
        session.add(self)
        session.commit()
        session.close()
    
    @classmethod
    def delete(cls, self):
        session = new_session()
        session.delete(self)
        session.commit()
        session.close()
        
    # 需要修改对象
    @classmethod
    def find_by_id_session(cls, id):
        session = new_session()
        obj = session.query(cls).filter(cls.id == id).first()
        return session, obj

    # 只查询，不修改
    @classmethod
    def find_by_id(cls, id):
        session = new_session()
        obj = session.query(cls).filter(cls.id == id).first()
        session.close()
        return obj
        
    @classmethod
    def close_session(cls, session):
        session.close()
        
    @classmethod
    def get_all_obj(cls, **kwargs):
        session = new_session()
        obj = session.query(cls).all()
        return list(obj)
    
    
# 提供给具体的model继承
Base = declarative_base(cls=Model)