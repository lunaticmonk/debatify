from flask import Blueprint,render_template,request,flash
from app import db
from app.models import User,Question

welcome = Blueprint('main',__name__, template_folder = "templates")

@welcome.route('/')
def index():
	return '<p>new blueprint succesfully created.</p>'
