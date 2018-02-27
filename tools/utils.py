from flask import session


# 根据session得到当前的用户ID
def current_user_id():
    id = session.get('user_id', 'null')
    return id

