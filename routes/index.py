from flask import Blueprint
from routes.forms import RegisterForm
from flask import render_template


main = Blueprint('index', __name__)


@main.route('/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print(form.name.data)
        print(form.password.data)
        
    return render_template('index.html', form=form)
    
    