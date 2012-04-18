#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from google.appengine.ext import db
import Env
Env.Custom.set()
import tweepy

from private.UserProfile import BotProfile

class DataStore(db.Model):

	isTweet = db.BooleanProperty(name="is_tweet")

	tweetTime = db.DateTimeProperty(name="tweet_time")
	oldTime = db.DateTimeProperty(name="old_time")

	def isUpdate(self, nowTime):
		ret = False
		if not self.isTweet and nowTime.minute >= 50:
			ret = True
		return ret

	def tweetReset(self):
		if self.oldTime and self.tweetTime:
			if self.oldTime.hour != self.tweetTime.hour:
				isTweet = False

class TimerBot():

	def __init__(self):
		pass

	def run(self):

		html = u"--- run --- <br/>"

		currentTime = datetime.datetime.now()
		html += "Current time : " + str(currentTime) + "<br/>"

		query = DataStore.all()
		elem = query.get()
		html += "DataStore time : " + str(elem.oldTime) + "<br/>"
		if elem.isUpdate(nowTime = currentTime):

			# create OAuth handler
			auth = tweepy.OAuthHandler(BotProfile.consumer_key, BotProfile.consumer_secret)

			# set access token to OAuth handler
			auth.set_access_token(BotProfile.access_key, BotProfile.access_secret)

			# create API
			api = tweepy.API(auth_handler=auth)

			d = currentTime + datetime.timedelta(hours=9)
			s = u'%(mo)d月%(d)d日 %(h)d時 50分頃をお知らせします。' % \
				{'mo':d.month, 'd':d.day, 'h':d.hour}

			html += s
			api.update_status(s)

			elem.isTweet = True
			elem.tweetTime = currentTime

		elem.oldTime = currentTime
		elem.tweetReset()
		elem.put()

		return html

	def default(self):
		html = u"--- set default --- <br/>"

		currentTime = datetime.datetime.now()

		query = DataStore.all()
		elem = query.get()
		if not elem:
			elem = DataStore()

		elem.isTweet = False
		elem.tweetTime = currentTime
		elem.oldTime = currentTime

		elem.put()

		html += self.test()
		return html

	def test(self):

		html = u"--- test --- <br/>"

		currentTime = datetime.datetime.now()
		html += "Current time : " + str(currentTime) + "<br/>"

		query = DataStore.all()
		elem = query.get()
		if elem:
			html += "DataStore time : " + str(elem.oldTime) + "<br/>"
			if elem.isUpdate(nowTime = currentTime):
				html += "update : enable<br/>"
			else:
				html += "update : disable<br/>"

			html += "Tweet time : " + str(elem.tweetTime) + "<br/>"
			if elem.isTweet:
				html += "tweet : enable<br/>"
			else:
				html += "tweet : disable<br/>"
		else:
			html += "please set default : <a href=\"./default\">call default</a><br/>"

		import sys
		html += "<br/>"
		html += "sys.path" + "<br/>"
		for path in sys.path:
			html += path + "<br/>"

		return html


