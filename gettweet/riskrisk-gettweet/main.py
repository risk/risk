# -*- Coding: utf-8-unix -*-
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

import datetime

import Timezone

import Twitter
import DataStore

class MainHandler(webapp.RequestHandler):
    def get(self):
        pass

class TweetStore(webapp.RequestHandler):

    def get(self):
        
        tags = [u'#devsumi',
                u'#devsumiA',u'#devsumiB',u'#devsumiC', u'#devsumiD', u'#devsumiE',
                u'#devsumiLC']

        twitter = Twitter.Twitter()
        ds = DataStore.DataStore()

        latestId = ds.getLatestId()
        updateLatestId = latestId
        for tag in tags:
            tweets = twitter.search(tag, 1)

            if len(tweets):
                for tweet in tweets:
                    if latestId < tweet[0]:
                        ds.addTweet( tag, tweet[1], tweet[2], tweet[3])
                        if updateLatestId < tweet[0]:
                            updateLatestId = tweet[0]
                
        ds.setLatestId(updateLatestId)


class TweetStoreD(webapp.RequestHandler):

    def get(self):
        tag = u'#devsumiD'

        twitter = Twitter.Twitter()
        ds = DataStore.DataStore()

        ds.deleteTweet(tag)

        checkpoint = datetime.datetime.strptime('2012/2/15 15:00','%Y/%m/%d %H:%M')

        loop = True
        page = 1
        while loop:

            tweets = twitter.search(tag, page)

            if tweets:
                for tweet in tweets:
                    d = tweet[3].replace(tzinfo=Timezone.UTC()).astimezone(Timezone.JST())
                    c = checkpoint.replace(tzinfo=Timezone.UTC()).astimezone(Timezone.JST())
                    if d > c:
                         ds.addTweet(tag, tweet[1], tweet[2], tweet[3])
                    else:
                        loop = False
                        break
 
                page += 1
            else:                
                loop = False

        return

class TweetStoreE(webapp.RequestHandler):

    def get(self):
        tag = u'#devsumiE'

        twitter = Twitter.Twitter()
        ds = DataStore.DataStore()

        ds.deleteTweet(tag)

        checkpoint = datetime.datetime.strptime('2012/2/15 15:00','%Y/%m/%d %H:%M')

        loop = True
        page = 1
        while loop:

            tweets = twitter.search(tag, page)

            if tweets:
                for tweet in tweets:
                    d = tweet[3].replace(tzinfo=Timezone.UTC()).astimezone(Timezone.JST())
                    c = checkpoint.replace(tzinfo=Timezone.UTC()).astimezone(Timezone.JST())
                    if d > c:
                        ds.addTweet(tag, tweet[1], tweet[2], tweet[3])
                    else:
                        loop = False
                        break
 
                page += 1
            else:                
                loop = False

        return

class ShowTweetDevsumi(webapp.RequestHandler):
    def get(self):
        ds = DataStore.DataStore()
        tweets = ds.getTweets(u'#devsumi')
        for tweet in tweets:
            self.response.out.write(
                u''.join([u'http://www.twitter.com/', tweet[0], u'/status/', tweet[1], u'<br/>\r\n']))

class ShowTweetDevsumiA(webapp.RequestHandler):
    def get(self):
        ds = DataStore.DataStore()
        tweets = ds.getTweets(u'#devsumiA')
        for tweet in tweets:
            self.response.out.write(
                u''.join([u'http://www.twitter.com/', tweet[0], u'/status/', tweet[1], u'<br/>\r\n']))

class ShowTweetDevsumiB(webapp.RequestHandler):
    def get(self):
        ds = DataStore.DataStore()
        tweets = ds.getTweets(u'#devsumiB')
        for tweet in tweets:
            self.response.out.write(
                u''.join([u'http://www.twitter.com/', tweet[0], u'/status/', tweet[1], u'<br/>\r\n']))

class ShowTweetDevsumiC(webapp.RequestHandler):
    def get(self):
        ds = DataStore.DataStore()
        tweets = ds.getTweets(u'#devsumiC')
        for tweet in tweets:
            self.response.out.write(
                u''.join([u'http://www.twitter.com/', tweet[0], u'/status/', tweet[1], u'<br/>\r\n']))

class ShowTweetDevsumiD(webapp.RequestHandler):
    def get(self):
        ds = DataStore.DataStore()
        tweets = ds.getTweets(u'#devsumiD')
        for tweet in tweets:
            self.response.out.write(
                u''.join([u'http://www.twitter.com/', tweet[0], u'/status/', tweet[1], u'<br/>\r\n']))

class ShowTweetDevsumiE(webapp.RequestHandler):
    def get(self):
        ds = DataStore.DataStore()
        tweets = ds.getTweets(u'#devsumiE')
        for tweet in tweets:
            self.response.out.write(
                u''.join([u'http://www.twitter.com/', tweet[0], u'/status/', tweet[1], u'<br/>\r\n']))

class ShowTweetDevsumiLC(webapp.RequestHandler):
    def get(self):
        ds = DataStore.DataStore()
        tweets = ds.getTweets(u'#devsumiLC')
        for tweet in tweets:
            self.response.out.write(
                u''.join([u'http://www.twitter.com/', tweet[0], u'/status/', tweet[1], u'<br/>\r\n']))


def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/devsumi', ShowTweetDevsumi),
                                          ('/devsumiA', ShowTweetDevsumiA),
                                          ('/devsumiB', ShowTweetDevsumiB),
                                          ('/devsumiC', ShowTweetDevsumiC),
                                          ('/devsumiD', ShowTweetDevsumiD),
                                          ('/devsumiE', ShowTweetDevsumiE),
                                          ('/devsumiLC', ShowTweetDevsumiLC),
                                          ('/storeD', TweetStoreD),
                                          ('/storeE', TweetStoreE),
                                          ('/store', TweetStore)],
                                         debug=True)
    util.run_wsgi_app(application)



if __name__ == '__main__':
    main()

