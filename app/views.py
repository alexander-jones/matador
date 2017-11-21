from flask import request, render_template
from flask_table import Table, Col
from app import app
from .forms import LoginForm, RegistrationForm

# Declare your table
class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/table')
def table():
	items = [dict(name='Name1', description='Description1'),
         dict(name='Name2', description='Description2'),
         dict(name='Name3', description='Description3')]
	table = ItemTable(items)
	return table.__html__()