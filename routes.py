from flask.helpers import url_for
from app import app, db
from flask import render_template, redirect, flash, url_for
from app.forms import UserInfoForm, EntryForm
from app.models import PhoneBookEntry, User


@app.route('/')
def index():
    title = "Home"
    return render_template('index.html', title = title)

@app.route('/register',  methods=["GET", 'POST'])
def register():
    register_form = UserInfoForm()  
    if register_form.validate_on_submit():
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data
        print(username, email, password)

        new_user = User(username, email, password)
        db.session.add(new_user)
        db.session.commit()
    return render_template('register.html', form=register_form)

@app.route('/new-entry', methods=['GET', 'POST'])
def new_entry():
    form = EntryForm()
    user_id = 1
    if form.validate_on_submit():
        name = form.name.data
        phone_number = form.phone_number.data
        add_entry = PhoneBookEntry(name, phone_number, user_id=1)
        db.session.add(add_entry)
        db.session.commit()

        flash(f'Your entry was submitted!', 'success')
        return redirect(url_for('index'))
    return render_template('newentry.html', form=form)