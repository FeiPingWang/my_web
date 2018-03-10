from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine("mysql+pymysql://root:123456@localhost:3306/moneyfree?charset=utf8", echo=False)
Session = scoped_session(sessionmaker(bind=engine))


def new_session():
    return Session()
