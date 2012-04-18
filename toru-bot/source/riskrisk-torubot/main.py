#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import ToruBot

class TweetHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.tweet())

class MentionHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.mention())

class UserControlHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.userControl())

class TweetEnableHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.tweetEnableUI())

	def post(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.tweetEnableExec(self.request))
		self.redirect('/tweetenable')

class ResetStoreHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.resetStore())

class AddStatusHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.addStatusUI())

	def post(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.addStatusExec(self.request))
		self.redirect('/addstatus')

class DelStatusHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.delStatusUI())

	def post(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.delStatusExec(self.request))
		self.redirect('/delstatus')

class AddOmikujiHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.addOmikujiUI())

	def post(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.addOmikujiExec(self.request))
		self.redirect('/addomikuji')

class DelOmikujiHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.delOmikujiUI())

	def post(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.delOmikujiExec(self.request))
		self.redirect('/delomikuji')

class PrioStatusHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.prioStatusUI())

	def post(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.prioStatusExec(self.request))
		self.redirect('/priostatus')

class PrioStatusResetHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.prioStatusReset())

class StatusListHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.statusList())

class MergeStoreHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.mergeStore())

class LogicTestHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.logicTest())

class TweetTestHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.tweetTest())

class StoreTestHandler(webapp.RequestHandler):
	def get(self):
		tb = ToruBot.ToruBot()
		self.response.out.write(tb.storeTest())


def main():
	application = webapp.WSGIApplication(
		[	('/tweet', TweetHandler), \
			('/mention', MentionHandler), \
			('/usercontrol', UserControlHandler), \
			('/tweetenable', TweetEnableHandler), \
			('/resetstore', ResetStoreHandler), \
			('/mergestore', MergeStoreHandler), \
			('/addstatus', AddStatusHandler), \
			('/delstatus', DelStatusHandler), \
			('/addomikuji', AddOmikujiHandler), \
			('/delomikuji', DelOmikujiHandler), \
			('/priostatus', PrioStatusHandler), \
			('/priostatusreset', PrioStatusResetHandler), \
			('/statuslist', StatusListHandler), \
			('/logictest', LogicTestHandler), \
			('/tweettest', TweetTestHandler), \
			('/storetest', StoreTestHandler) \
		], debug=True)
	util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
