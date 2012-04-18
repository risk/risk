#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import feedparser

class SChecker():

	data = None

	def __init__(self):
		self.data = feedparser.parse('http://twitter.com/statuses/user_timeline/47354052.rss')

	# すべての予定を羅列する
	def output(self):
		
		html = u'--- output start ---' + u'<br/>\r\n'

		html += u'title: ' + self.data.feed.title + u'<br/>\r\n'
		html += u'title: ' + self.data.feed.link + u'<br/>\r\n'

		html += u' - All -' + u'<br/>\r\n'
		for entry in self.data['entries']:
			html += 'title: ' + entry.title + u'<br/>\r\n'

		html += u' - pickup -' + u'<br/>\r\n'
		mension = re.compile('@[a-zA-z]+')
		rt = re.compile('RT')

		for entry in self.data['entries']:
			m = mension.match(entry.title)
			if m:
				html += 'title: ' + entry.title + u'<br/>\r\n'


		html += u'--- output end ---' + u'<br/>\r\n'

		return html

if __name__ == '__main__':

	checker = SChecker()
	print checker.output()


