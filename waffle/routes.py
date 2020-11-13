from flask import render_template, url_for, flash, redirect, request
from waffle import app, db, bcrypt
from waffle.auth_user import Registration, LogIn
from waffle.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = Registration()
    if form.validate_on_submit():
        #Hashes password
        hash_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #Creates User
        user = User(username=form.username.data, email=form.email.data, password=hash_pass)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.username.data}! You can now login!', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Create Account', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LogIn()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('homepage'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Log In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='My Account')


