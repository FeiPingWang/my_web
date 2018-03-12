from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models import Base
from flask import g


# 论坛的版块
class Web_View(Base):
    __tablename__ = 'web_view'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), nullable=False)
    views = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Web_View(id='{}', title='{}', views='{}')>".format(
            self.id, self.title, self.views
        )

    @classmethod
    def incre_views(cls):
        web = g.my_session.query(cls).first()
        web.views += 1
        g.my_session.commit()
