from flask import session
import uuid


# 根据session得到当前的用户ID
def current_user_id():
    id = session.get('user_id', 'null')
    return id


# 返回独一无二的id
def generate_uuid():
    return uuid.uuid4().hex