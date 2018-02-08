from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

'''
采用flask的扩展表单
'''


# 注册表单
class RegisterForm(FlaskForm):
    name = StringField('username', validators=[DataRequired(message='用户名不能为空')], render_kw={'placeholder':u'输入用户名'})
    password = PasswordField('passwd', validators=[DataRequired(message='密码不能为空')], render_kw={'placeholder':u'输入密码'})
    confirm = PasswordField('confirm',validators=[DataRequired(message='密码不能为空')], render_kw={'placeholder':u'确认密码'})
    email = StringField('email')
    submit = SubmitField('submit')
    
    