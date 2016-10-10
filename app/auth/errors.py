from flask import render_template
from . import auth

@auth.app_errorhandler(404)
def page_not_found(e):
	return '<p>page not found</p>', 404

@auth.app_errorhandler(404)
def page_not_found(e):
	return '<p>page not found</p>', 404

