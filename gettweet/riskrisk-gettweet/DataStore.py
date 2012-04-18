#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from google.appengine.ext import db

class Settings(db.Model):
	latestId = db.IntegerProperty(name="latestId")

class Tweet(db.Model):
	tag = db.StringProperty(name="tag")
	user = db.StringProperty(name="user")
	id = db.StringProperty(name="id")
	created_at = db.DateTimeProperty(name="created_at")

	def __eq__(self, rhs):
		return (self.id == rhs.id)

class DataStore():

	def setLatestId(self, id):
		query = Settings.all()
		s = query.get()
		if s:
			if s.latestId < id :
				s.latestId = id
				s.put()
		else:
			s = Settings()
			s.latestId = id
			s.put()

	def getLatestId(self):
		query = Settings.all()
		s = query.get()
		if s:
			return s.latestId
		else:
			return 0

	def addTweet(self, tag, user, id, created_at):
		query = Tweet.all()
		query.filter('tag =', tag)

		newTweet = Tweet(
			tag=tag,
			user=user,
			id=id,
			created_at=created_at)

		newTweet.put()

	def deleteTweet(self, tag):
		query = Tweet.all()
		query.filter('tag =', tag)
		query.order('id')
		slst = []
		while True:
			slst = query.fetch(1000)
			if len(slst) == 0:
				break

			for s in slst:
				s.delete()

	def getTweets(self, tag = None):
		query = Tweet.all()
		if tag:
			query.filter('tag =', tag)
		query.order('id')
		ret = []
		slst = []
		while len(slst) == 1000 or len(ret) == 0:
			slst = query.fetch(1000)
			if len(slst) == 0:
				break

			for s in slst:
				ret.append((s.user, s.id))

		return ret

def main():
	pass

if __name__ == '__main__':
	main()


