from flask import render_template
from . import auth


@auth.route('/fuck')
def login():
    return render_template('auth/me.html', name = 'Sumedh')