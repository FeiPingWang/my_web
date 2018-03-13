from sqlalchemy.ext.declarative import declarative_base, declared_attr
from flask import g, current_app
from tools.log import logger


# 基类
class Model(object):

    @classmethod
    def new(cls, self):
        try:
            g.my_session.add(self)
        except:
            logger.error('g.my_session add error, rollback')
            g.my_session.rollback()
        else:
            g.my_session.commit()
    
    @classmethod
    def delete(cls, self):
        try:
            g.my_session.delete(self)
        except:
            logger.error('g.my_session delete error, rollback')
            g.my_session.rollback()
        else:
            g.my_session.commit()

    @classmethod
    def update(cls, old, new):
        for name, value in vars(new).items():
            if name != 'id' and name != '_sa_instance_state':
                setattr(old, name, value)
        g.my_session.commit()

    @classmethod
    def find_by_id(cls, id):
        obj = g.my_session.query(cls).filter(cls.id == id).first()
        return obj

    @classmethod
    def get_all_obj(cls, page, **kwargs):
        '''
        根据page来返回指定的对象
        '''
        if int(page) <= 0:
            return None
        
        per_num = current_app.config['PER_PAG_NUM']
        obj = g.my_session.query(cls).offset((int(page) - 1) * per_num).limit(per_num).all()
        return list(obj)
    
    @classmethod
    def get_total_page_num(cls, **kwargs):
        per_num = current_app.config['PER_PAG_NUM']
        obj = g.my_session.query(cls).count()
        
        divisor = int(obj / per_num)
        remainder = obj % per_num
        
        if divisor < 1:
            return 1
        elif divisor > 1 and remainder == 0:
            return divisor
        else:
            return divisor + 1
    
    
# 提供给具体的model继承
Base = declarative_base(cls=Model)


if __name__ == '__main__':
    print(1/4)