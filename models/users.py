from sqlalchemy import Column, Integer, String, DateTime
from models import Base, new_session, Model, engine
import datetime


# 用户表
class User(Base):
    __tablename__ = 'users'

    # id = Column(Integer, primary_key=True)
    name = Column(String(20))
    password = Column(String(20))
    email = Column(String(30))
    brief = Column(String(140), default='新人报道啦')
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    
    def __repr__(self):
        return "<User(id='{}', name='{}', email='{}', brief='{}')>".format(
            self.id, self.name, self.email, self.brief
        )
    
        
if __name__ == '__main__':
    pass
    # # Base.metadata.create_all(engine)
    # session = new_session()
    # u1 = User(name='wfp', password='123456', email='wfp19920821@163.com')
    # # # p = session.query(User).filter(User.name == 'pxx')
    # # # # session.close()
    # # # d = dict(
    # # #     name = 'pxx',
    # # #     email = '1234',
    # # # )
    # # # p.delete()
    # session.add(u1)
    # session.commit()
    