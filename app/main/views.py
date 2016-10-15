from flask import Blueprint,render_template,request,flash,g
from flask.ext.login import current_user
from app import db
from app import models,login_manager
from app.models import User,Question
# from app.auth.views import user

welcome = Blueprint('main',__name__, template_folder = "templates")

@welcome.route('/', methods = ['GET','POST'])
def index():
	fetchedTopic = request.form['topic-textarea']
	fetchedQuestion = request.form['question-textarea']
	user_id = current_user.id
	user = load_user(user_id)
	#return user.firstname
	topicandquestion = Question(topic = fetchedTopic,questions = fetchedQuestion, owner = user)
	#db.session.add(topicandquestion)
 	#db.session.commit()
	#return '<p>hello</p>'
	return render_template('listitems.html', topic = fetchedTopic)
	#return "<p>hello</p>"