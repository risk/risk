#!/usr/bin/env python
# -*- coding: utf-8 -*-


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from private.OAuth import OAuthInfo

from Twitter import *

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(u'Hello world!')
        t=Twitter()
        t.update(u"日本語は？")

def main():
    application = webapp.WSGIApplication([
            ('/', MainHandler)
            ], debug=True )
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
