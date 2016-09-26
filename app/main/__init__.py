#import os
from flask import Flask,render_template,url_for
from flask_bootstrap import Bootstrap
from flask_script import Manager
#from flask_wtf import Form
#from wtforms.validators import Required

app = Flask(__name__)
manager = Manager(app)

@app.route('/user')
def index():
	return render_template('../templates/index.html')
	#return '<p>hello sumedh!</p>'			



if __name__ == '__main__':
	manager.run()