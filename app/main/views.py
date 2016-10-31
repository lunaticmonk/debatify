from flask import Blueprint,render_template,request,flash,g,redirect,url_for,flash
from app import db,moment,socketio,moment
from app.models import User,Question,load_user,Chats
from flask_login import current_user,login_required
from flask_moment import Moment
from datetime import datetime
from flask_socketio import emit,send


welcome = Blueprint('main',__name__, template_folder = "templates", static_folder = "static")

@welcome.route('/', methods = ["GET","POST"])
def index():
	savedQuestion = request.form['topic-textarea']
	savedTopic = request.form['question-textarea']
	link = 'http://127.0.0.1:5000/welcome/chat/<chat_id>'
	topicandquestion = Question(topic = savedTopic,questions = savedQuestion, owner = current_user, link = link)
	db.session.add(topicandquestion)
 	db.session.commit()
	return redirect(url_for('auth.dashboard'))

@welcome.route('/profile', methods = ['GET','POST'])
def profile():
	return render_template('user.html', user = current_user)

@welcome.route('/edit_profile', methods = ['GET','POST'])
def edit():
	return render_template('edit_profile.html', user = current_user)

@welcome.route('/update_profile', methods = ['GET','POST'])
def update_profile():
	user = current_user
	user.firstname = request.form['firstname']
	user.lastname = request.form['lastname']
	user.about_me = request.form['about_me']
	user.location = request.form['location']
	db.session.add(user)
	db.session.commit()
	flash('You have succesfully updated the info.')
	return redirect(url_for('main.profile'))

# @welcome.route('/chatroom', methods = ['GET','POST'])
# def chat():
# 	#if( request.form['name'] and request.form['room'] != null):
# 	return render_template('chatroom.html', name = request.form['name'], room = request.form['room'], user = current_user)

@welcome.route('/chat', methods = ['GET','POST'])
@login_required
def chatroom():
	#your_chat = Chats.query.filter_by(id = 1).first()
	global chat_id
	chat_id = request.args.get('chat_id')
	fetchedChat = Chats.query.filter_by(chat_id = chat_id).all()
	return render_template('chattest.html', user = current_user, current_time = datetime.utcnow(), chat_id = chat_id, fetchedChat = fetchedChat)

@socketio.on('joined')
def joined(data):
	print data
	emit('status', data, broadcast = True)

@socketio.on('message')
def handleMessage(message):
	print 'Message : ' + message
	send(message, broadcast = True)

@socketio.on('text')
def text(data):
	print data
	message = data
	time = datetime.utcnow()
	chat = Chats(messages = message, time = time, chat_id = chat_id, sender_name = current_user.firstname)
	db.session.add(chat)
	db.session.commit()
	emit('show', data, broadcast = True)

# @socketio.on('joined')
# def joined(data):
# 	# id = current_user.id
# 	# join_room(id)
# 	emit('status', {'msg' : current_user.firstname + ' has entered the room.' + '\n'})

# @socketio.on('text')
# def text(message):
#     """Sent by a client when the user entered a new message.
#     The message is sent to all people in the room."""
#     # room = session.get('room')
#     emit('message', {'msg': current_user.firstname + ':' + message.msg})
