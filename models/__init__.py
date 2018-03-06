from sqlalchemy.ext.declarative import declarative_base, declared_attr
from flask import g


# 基类
class Model(object):

    @classmethod
    def new(cls, self):
        g.my_session.add(self)
    
    @classmethod
    def delete(cls, self):
        g.my_session.delete(self)

    @classmethod
    def find_by_id(cls, id):
        obj = g.my_session.query(cls).filter(cls.id == id).first()
        return obj

    @classmethod
    def get_all_obj(cls, **kwargs):
        obj = g.my_session.query(cls).all()
        return list(obj)
    
    
# 提供给具体的model继承
Base = declarative_base(cls=Model)