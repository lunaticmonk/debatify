from flask import Blueprint,render_template

admin = Blueprint('auth',__name__)

@admin.route('/')
def index():
	return render_template('index.html')

@admin.route('/login')
def login():
	return render_template('login.html')

@admin.route('/register')
def register():
	return render_template('register.html')

@admin.route('/terms')
def terms():
	return render_template('terms.html')

@admin.route('/privacy')
def privacy():
	return render_template('privacy.html')

@admin.route('/about')
def about():
	return render_template('about.html')

