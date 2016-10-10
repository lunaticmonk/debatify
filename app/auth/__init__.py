from flask import Blueprint

admin = Blueprint('auth',__name__,template_folder = "templates")

from . import views