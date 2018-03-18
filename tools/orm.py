from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import app_config


# 如果是测试环境，链接测试用数据库
if app_config.IS_TESTING == 'True':
    db = "mysql+pymysql://root:123456@localhost:3306/moneyfree?charset=utf8"
else:
    db = "mysql+pymysql://root:123456@localhost:3306/testdb?charset=utf8"


engine = create_engine(db, echo=False)
Session = scoped_session(sessionmaker(bind=engine))


def new_session():
    return Session()
