from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models import Base


# 论坛的版块
class Types(Base):
    __tablename__ = 'Types'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(20), nullable=False)
    url = Column(String(20), nullable=False)
    menu_id = Column(Integer, nullable=False)
    num = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Types(id='{}', title='{}', url='{}', menu_id='{}', order='{}')>".format(
            self.id, self.title, self.url, self.menu_id, self.num
        )
