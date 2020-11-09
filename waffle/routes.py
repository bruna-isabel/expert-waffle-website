from flask import render_template, url_for, flash, redirect
from waffle.user_auth import Registration, LogIn
from waffle import app
from waffle.models import User, Post


posts = [
    {
        'author': 'Bruna Isabel',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2020',
    },
    {
        'author': 'Viviana',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 20, 2020', 
    }

]

@app.route('/')
def homepage():
    return render_template('homepage.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        flash(f'Welcome {form.username.data}', 'success')
        print("Validatin")
        return redirect(url_for('homepage'))
    
    return render_template('register.html', title='Create Account', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogIn()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('homepage'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Log In', form=form)
