from flask import session, redirect, url_for
import uuid
from functools import wraps


# 根据session得到当前的用户ID
def current_user_id():
    id = session.get('user_id', 'null')
    return id


# 验证当前用户是否登录的装饰器
def is_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        u = current_user_id()
        if u == 'null':   # 未登陆
            return redirect(url_for('index.login'))
        return func(*args, **kwargs)
    return wrapper
    

# 返回独一无二的id
def generate_uuid():
    return uuid.uuid4().hex


if __name__ == '__main__':
    print(generate_uuid())