#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from google.appengine.ext import db

class Settings(db.Model):
	mentionId = db.IntegerProperty(name="MentionId")
	tweetEnable = db.BooleanProperty(name="TweetEnable")

class const():
	def __setattr__(self, elem, value):
		pass

class Type(const):
	normal = u'normal'
	priority = u'priority'
	omikuji = u'omikuji'

class StatusNode(db.Model):
	type = db.StringProperty(name="type")
	status = db.StringProperty(name="status")
	registeredDate = db.DateTimeProperty(name="registeredDate")
	tweetCount = db.IntegerProperty(name="tweetCount")

	def __eq__(self, rhs):
		return (self.type == rhs.type and self.status == rhs.status)

class DataStore():

	def setMentionId(self, id):
		query = Settings.all()
		s = query.get()
		if s:
			s.mentionId = id
		else:
			s = Settings()
			s.mentionId = id
		s.put()

	def getMentionId(self):
		query = Settings.all()
		s = query.get()
		if s:
			return s.mentionId
		else:
			return 0

	def setTweetEnable(self, enable):
		query = Settings.all()
		s = query.get()
		if s:
			s.tweetEnable = enable
		else:
			s = Settings()
			s.tweetEnable = enable
		s.put()

	def getTweetEnable(self):
		query = Settings.all()
		s = query.get()
		if s:
			return s.tweetEnable
		else:
			return False

	def deleteSettings(self):
		query = Settings.all()
		s = query.get()
		if s:
			s.delete()

	def addStatus(self, type, status):
		query = StatusNode.all()
		query.filter('type =', type)
		slst = query.fetch(1000)

		newNode = StatusNode(
			type=type,
			status=status,
			registeredDate=datetime.datetime.now(),
			tweetCount=0)

		if not newNode in slst:
			# ツイートカウントを補正
			self.tweetCountAdjust(type)
			newNode.put()

	def getStatuses(self, type = None):
		query = StatusNode.all()
		if type:
			query.filter('type =', type)
		query.order('registeredDate')
		slst = query.fetch(1000)
		return [(s.type,s.status,s.registeredDate,s.tweetCount) for s in slst]

	def popStatus(self, type):
		query = StatusNode.all()
		if type:
			query.filter('type =', type)
		query.order('registeredDate')
		slst = query.fetch(1000)

		rtn = None
		if len(slst) != 0:
			rtn = (slst[0].type,slst[0].status,slst[0].registeredDate,slst[0].tweetCount)
			slst[0].delete()
		return rtn

	def tweetCountup(self, type, status):
		query = StatusNode.all()
		query.filter('type =', type)
		query.filter('status =', status)
		s = query.get()
		s.tweetCount += 1
		s.put()

	def tweetCountAdjust(self, type):
		query = StatusNode.all()
		query.filter('type =', type)
		query.order('tweetCount')
		slst = query.fetch(1000)

		if len(slst) != 0:
			base = slst[0].tweetCount
			for s in slst:
				s.tweetCount -= base
				s.put()

	def removeStatus(self, type, status):
		if not status:
			return
		query = StatusNode.all()
		query.filter('type =', type)
		query.filter('status =', status)
		slst = query.fetch(1000)
		for s in slst:
			s.delete()


	def removeStatuses(self, type = None):
		query = StatusNode.all()
		if type:
			query.filter('type =', type)
		query.order('registeredDate')
		slst = query.fetch(1000)
		for s in slst:
			s.delete()

def main():
	pass

if __name__ == '__main__':
	main()


