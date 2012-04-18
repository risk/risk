#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib

from private.UserProfile import BotProfile

class Bitly():

	url_ = None

	apiUrl_ = u'http://api.bitly.com/v3/shorten'

	def __init__(self, url):
		self.url_ = url

	def convert(self):
		if self.url_:
			return urllib.urlopen(u''.join([\
										self.apiUrl_, u'?'
										u'login=', BotProfile.bitlyLogin, u'&', \
										u'apikey=', BotProfile.bitlyApikey, u'&', \
										u'longUrl=', self.url_, u'&', \
										u'format=txt', u'&',
										])).read().rstrip(u'\r\n')
		return u''

def main():
#	b = Bitly('http://google.co.jp')
#	print b.convert()
#	print u'test'
	pass

if __name__ == '__main__':
	main()


