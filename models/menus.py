from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models import Base


# 论坛的版块
class Menus(Base):
    __tablename__ = 'Menus'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(20), nullable=False)
    num = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Menus(id='{}', title='{}', order='{}')>".format(
            self.id, self.title, self.num
        )
