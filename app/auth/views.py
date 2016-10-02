from flask import Blueprint,render_template

admin = Blueprint('auth',__name__)

@admin.route('/login')
def login():
	return render_template('login.html')

@admin.route('/register')
def register():
	return render_template('register.html')

