#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import random

import Timezone

import Twitter
import GCalendar
import DataStore
import TweetChecker

import CycleTweet
import ReplyTweet
import UserControl

# とおるさんbot本体
class ToruBot():

	# ツイート抑止
	noTweet = False

	# 出力HTMLの格納
	html = []

	# コンストラクタ
	def __init__(self):
		self.noTweet = False
		self.html = []

	# tweetエントリ
	def tweet(self):
		return self.doTweet(currentTime=datetime.datetime.now(Timezone.JST()))

	# mentionエントリ
	def mention(self):
		return self.doMention()

	# ユーザー制御エントリ
	def userControl(self):
		return self.doUserControl()

	# tweet処理
	def doTweet(self, currentTime):

		# 周期ハンドラを実行
		ctweet = CycleTweet.CycleTweet(currentTime)
		if self.noTweet:
			ctweet.setDisable()
		ctweet.handler()
		return u'\r\n'.join(ctweet.html)

	# mention処理
	def doMention(self):

		# 返信ハンドラを実行
		rtweet = ReplyTweet.ReplyTweet()
		if self.noTweet:
			rtweet.setDisable()
		rtweet.handler()
		return u'\r\n'.join(rtweet.html)


	# ユーザー制御処理
	def doUserControl(self):
		uc = UserControl.UserControl()
		uc.handler()
		return u'\r\n'.join(uc.html)

	def tweetEnableUI(self):
		ds = DataStore.DataStore()

		html = u''
		html += u'<head>' + u'\r\n'
		html += u'<meta http-epuiv="Content-Type" content="text/html;charset=utf-8" />' + u'\r\n'
		html += u'<title>ツイートの有効・無効</title>' + u'\r\n'
		html += u'</head>' + u'\r\n'

		html += u'<body>' + u'<br />\r\n'
		html += u'ツイートの有効・無効を設定します。' + u'<br />\r\n'
		html += u'現在の状態は「'
		if ds.getTweetEnable():
			html += u'有効'
		else:
			html += u'無効'
		html += u'」です' + u'<br />\r\n'

		html += u'<form method="post">' + '\r\n'
		html += u'<input type="radio" name="enable" value="enable" />有効'
		html += u'<input type="radio" name="enable" value="disable" />無効'
		html += u'<br />\r\n'
		html += u'<input type="submit" />' + u'<br />\r\n'
		html += u'</form>'

		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		html += u'</body>' + u'\r\n'

		return html

	def tweetEnableExec(self, request):
		ds = DataStore.DataStore()
		enable = request.get('enable')

		if enable == u'enable':
			ds.setTweetEnable(True)
		else:
			ds.setTweetEnable(False)

	# DataStoreの全リセット
	def resetStore(self):

		ds = DataStore.DataStore()

		ds.deleteSettings()
		ds.removeStatuses()

		html = u''
		html += u'<head>' + u'\r\n'
		html += u'<meta http-epuiv="Content-Type" content="text/html;charset=utf-8" />' + u'\r\n'
		html += u'<title>DataStoreのリセット</title>' + u'\r\n'
		html += u'</head>' + u'\r\n'

		html += u'<body>' + u'<br />\r\n'
		html += u'DataStoreの内容をクリアしました。' + u'<br />\r\n'
		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'
		html += u'</body>' + u'\r\n'

		return html

	# Statusの追加(UI)
	def addStatusUI(self):

		ds = DataStore.DataStore()

		html = u''
		html += u'<head>' + u'\r\n'
		html += u'<meta http-epuiv="Content-Type" content="text/html;charset=utf-8" />' + u'\r\n'
		html += u'<title>ステータスの追加</title>' + u'\r\n'
		html += u'</head>' + u'\r\n'

		html += u'<body>' + u'<br />\r\n'
		html += u'Statusの追加を行います。' + u'<br />\r\n'
		html += u'追加したい発言を入力欄にいれてsubmitしてください。' + u'<br />\r\n'
		html += u'複数行の入力が可能です' + u'<br />\r\n'

		html += u'<form method="post">' + '\r\n'
		html += u'<textarea name="status" cols="60" rows="5"></textarea>' + '<br />\r\n'
		html += u'<input type="submit" />' + u'<br />\r\n'
		html += u'</form>'

		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		html += u'--- 登録メッセージ一覧 ---' + u'<br />\r\n'
		lst = ds.getStatuses(DataStore.Type.normal)
		html += u'<table border=1>'
		html += u'<tr><td>No</td><td>TweetCount</td><td>status</td><td>RegisterDate</td></tr>'
		no = 0
		for s in lst:
			html += u'<tr><td>%(no)d</td><td>%(count)d</td><td>%(status)s</td><td>%(regDate)s</td></tr>\r\n' % \
				{'no':no, 'count':s[3], 'status':s[1], 'regDate':str(s[2]) }
			no += 1
		html += u'</table>'
		html += u'--------------------------' + u'<br />\r\n'

		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		html += u'</body>' + u'\r\n'

		return html

	# Statusの追加(実行)
	def addStatusExec(self, request):
		ds = DataStore.DataStore()
		lst = request.get('status').splitlines()
		for status in lst:
			ds.addStatus(DataStore.Type.normal, status)


	# Statusの削除(UI)
	def delStatusUI(self):

		ds = DataStore.DataStore()

		html = u''
		html += u'<head>' + u'\r\n'
		html += u'<meta http-epuiv="Content-Type" content="text/html;charset=utf-8" />' + u'\r\n'
		html += u'<title>ステータスの削除</title>' + u'\r\n'
		html += u'</head>' + u'\r\n'

		html += u'<body>' + u'\r\n'
		html += u'Statusの削除を行います。' + u'<br />\r\n'
		html += u'削除したい発言を入力欄にいれてsubmitしてください。' + u'<br />\r\n'
		html += u'複数行の入力が可能です' + u'<br />\r\n'

		html += u'<form method="post">' + '\r\n'
		html += u'<textarea name="status" cols="60" rows="5"></textarea>' + '<br />\r\n'
		html += u'<input type="submit" />' + u'<br />\r\n'
		html += u'</form>'
		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		html += u'--- 登録メッセージ一覧 ---' + u'<br />\r\n'
		lst = ds.getStatuses(DataStore.Type.normal)
		html += u'<table border=1>'
		html += u'<tr><td>No</td><td>TweetCount</td><td>status</td><td>RegisterDate</td></tr>'
		no = 0
		for s in lst:
			html += u'<tr><td>%(no)d</td><td>%(count)d</td><td>%(status)s</td><td>%(regDate)s</td></tr>\r\n' % \
				{'no':no, 'count':s[3], 'status':s[1], 'regDate':str(s[2]) }
			no += 1
		html += u'</table>'
		html += u'--------------------------' + u'<br />\r\n'

		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		html += u'</body>' + u'\r\n'

		return html

	# Statusの削除(実行)
	def delStatusExec(self, request):
		ds = DataStore.DataStore()
		lst = request.get('status').splitlines()
		for status in lst:
			ds.removeStatus(DataStore.Type.normal, status)



	# おみくじの追加(UI)
	def addOmikujiUI(self):

		ds = DataStore.DataStore()

		html = u''
		html += u'<head>' + u'\r\n'
		html += u'<meta http-epuiv="Content-Type" content="text/html;charset=utf-8" />' + u'\r\n'
		html += u'<title>おみくじの追加</title>' + u'\r\n'
		html += u'</head>' + u'\r\n'

		html += u'<body>' + u'<br />\r\n'
		html += u'おみくじの追加を行います。' + u'<br />\r\n'
		html += u'追加したいおみくじを入力欄にいれてsubmitしてください。' + u'<br />\r\n'
		html += u'複数行の入力が可能です' + u'<br />\r\n'

		html += u'<form method="post">' + '\r\n'
		html += u'<textarea name="status" cols="60" rows="5"></textarea>' + '<br />\r\n'
		html += u'<input type="submit" />' + u'<br />\r\n'
		html += u'</form>'

		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		html += u'--- 登録おみくじ一覧 ---' + u'<br />\r\n'
		lst = ds.getStatuses(DataStore.Type.omikuji)
		html += u'<table border=1>'
		html += u'<tr><td>No</td><td>status</td><td>RegisterDate</td></tr>'
		no = 0
		for s in lst:
			html += u'<tr><td>%(no)d</td><td>%(status)s</td><td>%(regDate)s</td></tr>\r\n' % \
				{'no':no, 'count':s[3], 'status':s[1], 'regDate':str(s[2]) }
			no += 1
		html += u'</table>'
		html += u'--------------------------' + u'<br />\r\n'

		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		html += u'</body>' + u'\r\n'

		return html

	# おみくじの追加(実行)
	def addOmikujiExec(self, request):
		ds = DataStore.DataStore()
		lst = request.get('status').splitlines()
		for status in lst:
			ds.addStatus(DataStore.Type.omikuji, status)


	# Statusの削除(UI)
	def delOmikujiUI(self):

		ds = DataStore.DataStore()

		html = u''
		html += u'<head>' + u'\r\n'
		html += u'<meta http-epuiv="Content-Type" content="text/html;charset=utf-8" />' + u'\r\n'
		html += u'<title>ステータスの削除</title>' + u'\r\n'
		html += u'</head>' + u'\r\n'

		html += u'<body>' + u'\r\n'
		html += u'おみくじの削除を行います。' + u'<br />\r\n'
		html += u'削除したいおみくじを入力欄にいれてsubmitしてください。' + u'<br />\r\n'
		html += u'複数行の入力が可能です' + u'<br />\r\n'

		html += u'<form method="post">' + '\r\n'
		html += u'<textarea name="status" cols="60" rows="5"></textarea>' + '<br />\r\n'
		html += u'<input type="submit" />' + u'<br />\r\n'
		html += u'</form>'
		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		html += u'--- 登録おみくじ一覧 ---' + u'<br />\r\n'
		lst = ds.getStatuses(DataStore.Type.omikuji)
		html += u'<table border=1>'
		html += u'<tr><td>No</td><td>status</td><td>RegisterDate</td></tr>'
		no = 0
		for s in lst:
			html += u'<tr><td>%(no)d</td><td>%(status)s</td><td>%(regDate)s</td></tr>\r\n' % \
				{'no':no, 'count':s[3], 'status':s[1], 'regDate':str(s[2]) }
			no += 1
		html += u'</table>'
		html += u'--------------------------' + u'<br />\r\n'

		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		html += u'</body>' + u'\r\n'

		return html

	# おみくじの削除(実行)
	def delOmikujiExec(self, request):
		ds = DataStore.DataStore()
		lst = request.get('status').splitlines()
		for status in lst:
			ds.removeStatus(DataStore.Type.omikuji, status)


	# 優先Statusの追加(UI)
	def prioStatusUI(self):

		ds = DataStore.DataStore()

		html = u''
		html += u'<head>' + u'\r\n'
		html += u'<meta http-epuiv="Content-Type" content="text/html;charset=utf-8" />' + u'\r\n'
		html += u'<title>優先ステータスの追加</title>' + u'\r\n'
		html += u'</head>' + u'\r\n'

		html += u'<body>' + u'<br />\r\n'
		html += u'優先して呟かせたいステータスを設定します。' + u'<br />\r\n'
		html += u'追加したい発言を入力欄にいれてsubmitしてください。' + u'<br />\r\n'
		html += u'複数行の入力が可能です' + u'<br />\r\n'

		html += u'<form method="post">' + '\r\n'
		html += u'<textarea name="status" cols="60" rows="5"></textarea>' + '<br />\r\n'
		html += u'<input type="submit" />' + u'<br />\r\n'
		html += u'</form>'

		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		html += u'--- 登録メッセージ一覧 ---' + u'<br />\r\n'
		lst = ds.getStatuses(DataStore.Type.priority)
		html += u'<table border=1>'
		html += u'<tr><td>No</td><td>TweetCount</td><td>status</td><td>RegisterDate</td></tr>'
		no = 0
		for s in lst:
			html += u'<tr><td>%(no)d</td><td>%(count)d</td><td>%(status)s</td><td>%(regDate)s</td></tr>\r\n' % \
				{'no':no, 'count':s[3], 'status':s[1], 'regDate':str(s[2]) }
			no += 1

		html += u'</table>'
		html += u'--------------------------' + u'<br />\r\n'

		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		html += u'</body>' + u'\r\n'

		return html

	# 優先Statusの追加(実行)
	def prioStatusExec(self, request):
		ds = DataStore.DataStore()
		lst = request.get('status').splitlines()
		for status in lst:
			ds.addStatus(DataStore.Type.priority, status)

	# 優先Statusのリセット
	def prioStatusReset(self):
		ds = DataStore.DataStore()

		# 優先ステータスのクリア
		ds.removeStatuses(DataStore.Type.priority)

		html = u''
		html += u'<head>' + u'\r\n'
		html += u'<meta http-epuiv="Content-Type" content="text/html;charset=utf-8" />' + u'\r\n'
		html += u'<title>優先ステータスのリセット</title>' + u'\r\n'
		html += u'</head>' + u'\r\n'

		html += u'<body>' + u'<br />\r\n'
		html += u'優先ステータスをリセットしました。' + u'<br />\r\n'
		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'
		html += u'</body>' + u'\r\n'

		return html

	# Statusの一覧表示
	def statusList(self):
		ds = DataStore.DataStore()
		lst = ds.getStatuses(DataStore.Type.normal)

		html = u''
		html += u'<head>' + u'\r\n'
		html += u'<meta http-epuiv="Content-Type" content="text/html;charset=utf-8" />' + u'\r\n'
		html += u'<title>ステータスの削除</title>' + u'\r\n'
		html += u'</head>' + u'\r\n'

		html += u'<body>' + u'\r\n'
		html += u'Statusの一覧を表示します。' + u'<br />\r\n'
		html += u'現在の登録数は %d個です。' % len(lst) + u'<br />\r\n'

		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		html += u'<br />\r\n'

		html += u'--- 登録メッセージ一覧 ---' + u'<br />\r\n'
		html += u'<br />\r\n'
		no = 1

		html += u'<table border=1>'
		html += u'<tr><td>No</td><td>TweetCount</td><td>status</td><td>RegisterDate</td></tr>'
		for s in lst:
			html += u'<tr><td>%(no)d</td><td>%(count)d</td><td>%(status)s</td><td>%(regDate)s</td></tr>\r\n' % \
				{'no':no, 'count':s[3], 'status':s[1], 'regDate':str(s[2]) }
			no += 1

		html += u'</table>'
		html += u'--------------------------' + u'<br />\r\n'

		html += u'<br />\r\n'

		html += u'ステータスのバックアップは、下記のｷﾘﾄﾘｾﾝの中身をメモ帳にでもいれといて。' + u'<br />\r\n'

		html += u'<br />\r\n'
		html += u'----- ｷﾘﾄﾘｾﾝ -----' + u'<br />\r\n'

		html += u'normal<br />\r\n'
		lst = ds.getStatuses(DataStore.Type.normal)
		for s in lst:
			html += s[1] + u'<br />\r\n'

		html += u'<br />\r\n'

		html += u'omikuji<br />\r\n'
		lst = ds.getStatuses(DataStore.Type.omikuji)
		for s in lst:
			html += s[1] + u'<br />\r\n'

		html += u'----- ｷﾘﾄﾘｾﾝ -----' + u'<br />\r\n'
		html += u'<br />\r\n'

		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		html += u'</body>' + u'<br />\r\n'

		return html

	# 旧データベースから新データベースへの移行
	def mergeStore(self):
		
		html = u''
		html += u'<head>' + u'\r\n'
		html += u'<meta http-epuiv="Content-Type" content="text/html;charset=utf-8" />' + u'\r\n'
		html += u'<title>データストアのマージ</title>' + u'\r\n'
		html += u'</head>' + u'\r\n'

		ds = DataStore.DataStore()

		ds.removeStatuses()

		lst = ds.getList()
		for s in lst:
			ds.addStatus(DataStore.Type.normal, s)

		html += u'<body>' + u'\r\n'
		html += u'マージ完了' + u'<br />\r\n'
		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		html += u'</body>' + u'<br />\r\n'

		return html

	# ロジックテスト
	def logicTest(self):

		# 発言しないように設定
		self.noTweet = True

		# idを更新しないように保持
		ds = DataStore.DataStore()
		id = ds.getMentionId()
		ds.setMentionId(0)

		self.html.append(u'<a href="/manage.html">戻る</a>' + u'<br />')

		self.html.append(u'<b>logictest start<b><br/>')

		self.html.append(u'<hr size="20" noshade>')
		self.html.append(u'<font size="15" color="green"><b>normal tweet</font>')
		self.html.append(u'<hr size="20" noshade>')
		self.html.append(self.doTweet(datetime.datetime.strptime('10:50','%H:%M')))
		self.html.append(self.doTweet(datetime.datetime.strptime('11:00','%H:%M')))
		self.html.append(self.doTweet(datetime.datetime.strptime('23:00','%H:%M')))
		self.html.append(self.doTweet(datetime.datetime.strptime('11:01','%H:%M')))
		self.html.append(self.doTweet(datetime.datetime.strptime('22:50','%H:%M')))
		self.html.append(self.doTweet(datetime.datetime.strptime('23:01','%H:%M')))
		self.html.append(self.doTweet(datetime.datetime.strptime('01:00','%H:%M')))
		self.html.append(self.doTweet(datetime.datetime.strptime('00:00','%H:%M')))
		self.html.append(self.doTweet(datetime.datetime.strptime('10:00','%H:%M')))
		self.html.append(self.doTweet(datetime.datetime.strptime('12:00','%H:%M')))
		self.html.append(self.doTweet(datetime.datetime.strptime('22:00','%H:%M')))
		self.html.append(self.doTweet(datetime.datetime.strptime('15:30','%H:%M')))
		self.html.append(self.doTweet(datetime.datetime.strptime('17:30','%H:%M')))

		self.html.append(self.doTweet(currentTime=datetime.datetime.now(Timezone.JST())))

		self.html.append(u'<hr size="20" noshade>')
		self.html.append(u'<font size="15" color="green">mention tweet</font>')
		self.html.append(u'<hr size="20" noshade>')
		self.html.append(self.doMention())

		self.html.append(u'<hr size="20" noshade>')
		self.html.append(u'<font size="15" color="green">anniversary tweet</font>')
		self.html.append(u'<hr size="20" noshade>')
		self.html.append(self.doTweet(currentTime=datetime.datetime.strptime('2011/2/13 0:30','%Y/%m/%d %H:%M')))
		self.html.append(self.doTweet(currentTime=datetime.datetime.strptime('2011/2/13 1:30','%Y/%m/%d %H:%M')))
		self.html.append(self.doTweet(currentTime=datetime.datetime.strptime('2011/2/13 12:30','%Y/%m/%d %H:%M')))
		self.html.append(self.doTweet(currentTime=datetime.datetime.strptime('2012/2/13 13:30','%Y/%m/%d %H:%M')))
		self.html.append(self.doTweet(currentTime=datetime.datetime.strptime('2013/2/13 22:30','%Y/%m/%d %H:%M')))
		self.html.append(self.doTweet(currentTime=datetime.datetime.strptime('2013/2/13 23:30','%Y/%m/%d %H:%M')))

		self.html.append(self.doTweet(currentTime=datetime.datetime.strptime('2011/12/30 22:50','%Y/%m/%d %H:%M')))
		self.html.append(self.doTweet(currentTime=datetime.datetime.strptime('2011/12/31 10:50','%Y/%m/%d %H:%M')))

		gcal = GCalendar.GCalendar('http://www.google.com/calendar/feeds/nekorobi%40gmail.com/public/basic')
		self.html.append(gcal.output())

		self.html.append(u'<hr size="20" noshade>')
		self.html.append(u'<font size="15" color="green">togther tweet</font>')
		self.html.append(u'<hr size="20" noshade>')

		now = datetime.datetime.now()
		datestr = u''.join([str(now.year), u'/', str(now.month), u'/', str(now.day), u' ', u'23:05'])
		chkdate = datetime.datetime.strptime(datestr,'%Y/%m/%d %H:%M').replace(tzinfo=Timezone.JST())
		self.html.append(self.doTweet(currentTime=chkdate))

		self.html.append(u'<li>logictest end</li>')

		self.html.append(u'<a href="/manage.html">戻る</a><br/>')

		# IDを戻す
		ds.setMentionId(id)

		return u'\r\n'.join(self.html)

	# ツイートテスト
	def tweetTest(self):

		html = u''

		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		html += u'--- tweettest start ---<br/>\r\n'

		d = datetime.datetime.now(Timezone.JST())
		ds = u'%(h)d:%(m)02d' % {'h':d.hour, 'm':d.minute}
		r = random.randint(0, 3)
		if( r == 0 ):
			s = u'きなこちゃん、いま' + ds + u'だよぉぐへへへへ'
		elif( r == 1 ):
			s = ds + u'だよぉ、きーなこちゃん'
		elif( r == 2 ):
			s = u'もう' + ds + u'だねぇ、かわいいねぇきなこちゃん'
		else:
			s = u'きなこおおおきなこおおお、え？あぁいまは' + ds + u'ですよ。'

		twitter = Twitter.Twitter()
		twitter.update(s)
		html += s + u'<br/>\r\n'

		html += u'--- tweettest end ---<br/>\r\n'

		html += u'<a href=\'/manage.html\'>戻る</a>' + u'<br />\r\n'

		return html

# 単体エントリ
def main():
	pass

if __name__ == '__main__':
	print main()

