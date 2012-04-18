#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import random

import Env
Env.Custom.set()
import Twitter

import Utils

import GCalendar
import DataStore
import Twitpic

# 周期ツイート
class CycleTweet(Twitter.Twitter):

	# 現在時刻
	ct = None

	# ねころびカレンダーのURL
	calUrl = 'http://www.google.com/calendar/feeds/nekorobi%40gmail.com/public/basic'

	# 出力HTMLの格納
	html = []

	# 初期化
	def __init__(self, currentTime):
		Twitter.Twitter.__init__(self)
		# 現在時刻
		self.ct = currentTime
		self.html = []

		# クラス名
		self.html.append(u'<hr size="10" noshade>')
		self.html.append(u'<b>Cycle Tweet</b><br/>')

		# 現在時刻
		self.html.append(u'<b>%(mo)d月%(d)d日 %(h)02d:%(m)02d</b><br/>' % \
			{'mo':self.ct.month, 'd':self.ct.day, 'h':self.ct.hour, 'm':self.ct.minute})


	# 開店ハンドラ
	def nekorobiOpen(self):
		s = u'%(mo)d月%(day)d日です！今日も一日がんばりましィィヤッホォォォォゥ！' % \
			{'mo':self.ct.month, 'day':self.ct.day}
		return s

	# 閉店ハンドラ
	def nekorobiClose(self):
		s = u'%(mo)d月%(day)d日でした！今日も一日お疲れさまでしィィヤッホォォォォゥ！' % \
			{'mo':self.ct.month, 'day':self.ct.day}
		return s

	# 本日の予定呟き
	def todaySchedule(self, gcal):
		s = []
		info = gcal.getDateInfo(self.ct)
		if( info != u''):
			s = [u'きなこちゃん、今日は「',	info, u'」だよぉ ﾌﾋﾋﾋﾋﾋ']

		return u''.join(s)

	# 明日の予定呟き
	def tomorrowSchedule(self, gcal):
		# カレンダー情報の取得
		s = []
		info = gcal.getDateInfo(self.ct + datetime.timedelta(days=1))
		if( info != u''):
			s = [u'きなこちゃん、明日は「', info, u'」だよぉ ｸﾞﾍﾍﾍﾍ']

		return u''.join(s)

	# 通常(優先)呟き
	def otherTweet(self):

		# DataStoreクラスの生成
		ds = DataStore.DataStore()

		# 優先発言の取得
		ps =ds.popStatus(DataStore.Type.priority)

		s = []

		# 優先発言がある場合
		if ps:
			s = [ps[1]]
		# 優先が無い場合は、通常の発言
		else:
			# 発言リストを取得
			statusList = ds.getStatuses(DataStore.Type.normal)
			status = self.tweetChoice([(s[1], s[3]) for s in statusList])

			# ツイート回数を増加
			ds.tweetCountup(DataStore.Type.normal, status)

			# 発言を設定
			s = [status]

		# 表示用の時間を取得
		s.append(u'(%(h)d:%(m)02dの心の声)' % {'h':self.ct.hour, 'm':self.ct.minute})

		return u''.join(s)

	def tweetChoice(self, lst):

		# カウント回数の最大値を取得
		countMax = lst[0][1]
		for status in lst:
			if countMax < status[1]:
				countMax = status[1]

		choicelst = []
		for status in lst:
			for i in range(0, ((countMax - status[1] )*2+1)):
				choicelst.append(status[0])

		# 発言をランダムに選択
		s = Utils.randomChoice(choicelst)

		return s

	# 店舗予定tweet
	def scheduleHandler(self):
		self.html.append(u'<li>schedule</li>')

		s = u''

		# 開店時間10分前
		if self.ct.hour == 10 and self.ct.minute == 50:
			self.html.append(u'Today schedule<br/>')
			s = self.todaySchedule(GCalendar.GCalendar(self.calUrl))
		# 閉店時間10分前
		elif self.ct.hour == 22 and self.ct.minute == 50:
			self.html.append(u'Tomorrow schedule<br/>')
			s = self.tomorrowSchedule(GCalendar.GCalendar(self.calUrl))

		# tweetの実行
		self.tweet(s)

	# 定周期tweet
	def cycleHandler(self):
		self.html.append(u'<li>cycle</li>')

		s = u''

		# 開店時間
		if self.ct.hour == 11 and self.ct.minute==0:
			self.html.append(u'Nekorobi open<br/>')
			s = self.nekorobiOpen()
		# 閉店時間
		elif self.ct.hour == 23 and self.ct.minute == 0:
			self.html.append(u'Nekorobi close<br/>')
			s = self.nekorobiClose()
		# キリのいい時間
		elif self.ct.minute == 0:
			self.html.append(u'normal<br/>')
			s = self.otherTweet()

		# tweetの実行
		self.tweet(s)

	# まとめtweet
	def togetherHandler(self):
		# 閉店時間
		if self.ct.hour == 23 and self.ct.minute == 5:
			self.html.append(u'<li>together</li>')

			tp = Twitpic.Twitpic(u'catcafenekorobi')

			urlList = tp.getUserPicList(self.ct)

			tweetList = []

			if len(urlList):
				tweetdef = u'本日のねころび画像'
				tweetstr = tweetdef
				for url in urlList:
					if len(u''.join([tweetstr, u' ' , url])) >= 138:
						tweetList.append(tweetstr)
						tweetstr = tweetdef

					tweetstr = u''.join([tweetstr, u' ' , url])

				if tweetdef!=tweetstr:
					tweetList.append(tweetstr)

				for s in tweetList:
					# tweetの実行
					self.tweet(s)


	# 記念日カスタムのtweet
	def anniversaryHandler(self):
		self.html.append(u'<li>anniversary</li>')

		s = u''

		# ねころび誕生日(2/13 - 2時間に一回(30分))
		if self.ct.month == 2 and self.ct.day == 13 and (self.ct.hour%2) == 0 and self.ct.minute == 30:
			y = self.ct.year - 2008
			p = (self.ct.hour/2) + 1
			s = u'ねころび『%(year)d周年』記念だぜ！ｲｲｲｲﾔｯﾎｵｵｵｩｩｩ！！！(%(p)d/12)' % \
				{ 'year':y, 'p':p }

		# tweetの実行
		self.tweet(s)

	# 緊急時のtweet
	def emergencyHandler(self):
		pass

	# 呟く
	def tweet(self, status):
		self.html.append(u'<hr/>')

		if(status != u''):
			# 呟き実行
			self.update(status)
			# 呟き表示
			self.html.append(u''.join([u'status: ', status, u'<br/>']))
			self.html.append(u'<font color="blue">tweeting!</font><br/>')
		else:
			self.html.append(u'<font color="red">not tweeting!</font><br/>')

		self.html.append(u'<hr/>')

	# メインハンドラ
	def handler(self):

		self.html.append(u'<b>tweet handler start</b><br/>')

		# ツイート内容の初期化
		s = u''

		# 予定ツイート
		self.scheduleHandler()

		# 定周期
		self.cycleHandler()

		# まとめ
		self.togetherHandler()

		# 記念日
		self.anniversaryHandler()

		# 緊急事態
		self.emergencyHandler()

		self.html.append(u'<b>tweet handler end</b><br/>')

# 単体エントリ
def main():
	pass

if __name__ == '__main__':
	print main()

