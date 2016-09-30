from flask import Blueprint,render_template

admin = Blueprint('auth',__name__)

@admin.route('/home')
def home():
	return '<p>Hello there!</p>'


