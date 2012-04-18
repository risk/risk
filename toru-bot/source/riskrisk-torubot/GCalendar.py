#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import feedparser
import Timezone

import datetime

class GCalendar():

	# 予定の読み込み
	data = None

	def __init__(self, url):
		self.data = feedparser.parse(url)

	def getDateInfo(self, date):
		# 現在の日付を作成
		nd = u'%(y)04d/%(m)02d/%(d)02d' % {'y':date.year, 'm':date.month, 'd':date.day}

		nowDate = datetime.datetime(date.year, date.month, date.day)

		rJa = re.compile(u'開始日: (.*) .*<br')
		rEn = re.compile(u'When: (.*)<br')

		# 結果文字列を初期化
		rlist = []

		# 指定日時の予定を取得(Ja)
		for entry in self.data['entries']:
			m = rJa.match(entry.content[0].value)
			try:
				if m:
					d = datetime.datetime.strptime(m.group(1), u'%Y/%m/%d')
					if( nowDate == d ):
						rlist.append(entry.title)

				m = rEn.match(entry.content[0].value)
				if m:
					d = datetime.datetime.strptime(m.group(1), u'%a %b %d, %Y')
					if( nowDate == d ):
						rlist.append(entry.title)
			except ValueError:
				pass

		if(len(rlist)==0):
			return u''
		return u' / '.join(rlist)

	# すべての予定を羅列する
	def output(self):
		
		html = u'--- output start ---' + u'<br/>\r\n'

		html += u'title: ' + self.data.feed.title + u'<br/>\r\n'
		html += u'link : ' + self.data.feed.link + u'<br/>\r\n'

		rJa = re.compile(u'開始日: (.*) .*<br')
		rEn = re.compile(u'When: (.*)<br')

		for entry in self.data['entries']:
			html += 'title: ' + entry.title + u'<br/>\r\n'
			html += u'-- content start --<br/>\r\n'
			html += u'<pre>' + entry.content[0].value + u'</pre>' + u'<br/>\r\n'
			html += u'-- content end -- <br/>\r\n'

			m = rJa.match(entry.content[0].value)
			indicate = False
			if m:
				html +=  u'date: ' + m.group(1) + u'<br/>\r\n'
				indicate = True

			m = rEn.match(entry.content[0].value)
			if m:
				html +=  u'date: ' + m.group(1) + u'<br/>\r\n'
				indicate = True

			if not indicate:
				html +=  u'date: unknown<br/>\r\n'

		html += u'--- output end ---' + u'<br/>\r\n'

		return html

def main():
#	gCalender = GCalendar('http://www.google.com/calendar/feeds/nekorobi%40gmail.com/public/basic')
	pass

if __name__ == '__main__':
	main()


