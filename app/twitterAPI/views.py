from flask import Blueprint,render_template,request,flash,redirect,url_for,session,g,jsonify
from app import models,login_manager
from app import db,mail
import os
import oauth2 as oauth
import json

API_KEY = 'qh8KZMh6n0SlxMeNwrmmwD8YT'
API_SECRET = 'uCEBWLveGDawdIml4j5X9VgE9LlovFXQnNkRU8T0kWJfZo4YVx'
ACCESS_TOKEN = '324935612-1YsYKKUD2mufGw24ZWFjNUQs7KBjIPrl0Wuw1Oeq'
ACCESS_TOKEN_SECRET = 'WKQoBx0dj2uMquLxy7C9eG86AQhbdrkFAZwVzypCZiOaa'

api = Blueprint('twitter',__name__, template_folder = "templates", static_folder = "static")

@api.route('/tweets')
def getTweets():
	# chat_id = request.args.get('chat_id')
	# print chat_id
	# query = models.Question.query(filter_by = chat_id).first()
	# user = query.topic
	user = 'ammaji'
	consumer = oauth.Consumer( key = API_KEY, secret = API_SECRET)
	access_token = oauth.Token( key = ACCESS_TOKEN, secret = ACCESS_TOKEN_SECRET)
	client = oauth.Client( consumer, access_token)

	endpoint = 'https://api.twitter.com/1.1/search/tweets.json?' + 'q=' + user + '&count=10' + '&src=typd'

	response, data = client.request(endpoint)

	tweets = json.loads(data)			#tweets object
	statuses = tweets['statuses']		#list of statuses
	# for tweet in tweets:
	listOfTweets = []
	for status in statuses:
		listOfTweets.append(status['text'])
		print status['text']
		print '\n'
	return render_template('tweets.html', tweets = listOfTweets)