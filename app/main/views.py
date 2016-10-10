from flask import Blueprint,render_template,request,flash,g
from app import db
from app.models import User,Question,load_user
from flask_login import current_user

welcome = Blueprint('main',__name__, template_folder = "templates")

@welcome.route('/', methods = ["GET","POST"])
def index():
	fetchedQuestion = request.form['topic-textarea']
	fetchedTopic = request.form['question-textarea']
	topicandquestion = Question(topic = fetchedTopic,questions = fetchedQuestion, owner = current_user)
	db.session.add(topicandquestion)
 	db.session.commit()
	return render_template('listitems.html', topic = fetchedTopic, questions = fetchedQuestion)