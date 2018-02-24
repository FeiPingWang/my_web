from flask import session
from models.users import User


# 根据session得到当前的用户ID
def current_user_id():
    id = session.get('user_id', '-1')
    return id
