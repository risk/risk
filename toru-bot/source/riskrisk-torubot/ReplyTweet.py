#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import re

import Env
Env.Custom.set()
import Twitter

import Utils
import DataStore
import TweetChecker

# 応答ツイート
class ReplyTweet(Twitter.Twitter):

	# 出力HTMLの格納
	html = []

	# 初期化
	def __init__(self):
		Twitter.Twitter.__init__(self)
		self.html = []

		# クラス名
		self.html.append(u'<hr size="10" noshade>')
		self.html.append(u'<b>Reply Tweet</b><br/>')


	# 返信ツイートを140文字にまとめる
	# msgが138以上の場合正常動作しないはず。
	# 自分できめるメッセージなので未対策（問題なしと判断）
	# また139文字にまとめるのは140ぴったりが怖いから。
	def resTweetTrim(self, msg, original):
		# メッセージをつないで、138文字にまとめる
		s = u''.join([msg, u' (', original])[0:138]
		# 後ろに閉じ括弧
		return u''.join([s, u')'])


	# イヤッホゥ返信機能
	def iyahoTweet(self, mentionList):

		self.html.append(u'<li>iyaho</li>')

		# 発言リストの初期化
		slst = []

		# Mentionの情報を処理
		for m in mentionList:

			# 発言チェッカーに設定
			tc = TweetChecker.TweetChecker(m[2])
			# ペロペロ成分入りなら返信
			if tc.isIyaho():

				tweetlist = [ \
					u'@%(resUser)s イヤッホホゥゥウウゥゥウゥゥ！！！', \
					u'@%(resUser)s イヤッホゥ？イヤッホゥ？イヤッホゥ！！！', \
					u'@%(resUser)s イィィイイィヤアアッホオオオオウウウゥゥウゥゥ！！！' \
					]

				# 呟くメッセージを作成
				msg = self.resTweetTrim( Utils.randomChoice(tweetlist) % {'resUser':m[1]}, m[2])

				slst.append((msg, m[0]))

		# 作成した返信をツイート
		self.html.append(u'<hr/>')
		for s in slst:
			self.update(s[0], s[1])
			self.html.append(u''.join([s[0], u'<br/>']))
		self.html.append(u'<hr/>')

	# ウッヒョウ返信機能
	def uhyouTweet(self, mentionList):

		self.html.append(u'<li>uhyou</li>')

		# 発言リストの初期化
		slst = []

		# Mentionの情報を処理
		for m in mentionList:

			# 発言チェッカーに設定
			tc = TweetChecker.TweetChecker(m[2])
			# ペロペロ成分入りなら返信
			if tc.isUhyou():

				tweetlist = [ \
					u'@%(resUser)s ウッヒョオオウウゥウウゥ！！！', \
					u'@%(resUser)s ウッヒョゥ？ウッヒョゥ？ウッヒョゥ！！！', \
					u'@%(resUser)s ウッヒョオオオォォォゥウウゥゥウウゥウゥゥゥゥ！！！' \
					]

				# 呟くメッセージを作成
				msg = self.resTweetTrim( Utils.randomChoice(tweetlist) % {'resUser':m[1]}, m[2])

				slst.append((msg, m[0]))

		# 作成した返信をツイート
		self.html.append(u'<hr/>')
		for s in slst:
			self.update(s[0], s[1])
			self.html.append(u''.join([s[0], u'<br/>']))
		self.html.append(u'<hr/>')

	# 俺はノンケでもペロペロしちまう機能
	def peroperoTweet(self, mentionList):

		self.html.append(u'<li>peropero</li>')

		# 発言リストの初期化
		slst = []

		# Mentionの情報を処理
		for m in mentionList:

			# 発言チェッカーに設定
			tc = TweetChecker.TweetChecker(m[2])
			# ペロペロ成分入りなら返信
			if tc.isPeropero():

				tweetlist = [ \
					u'@%(resUser)s ﾍﾟﾛﾍﾟﾛﾍﾟﾛﾍﾟﾛﾍﾟﾛﾍﾟﾛﾍﾟﾛﾍﾟﾛﾍﾟﾛﾍﾟﾛﾍﾟﾛﾍﾟﾛ', \
					u'@%(resUser)s ﾍﾟﾛ・・・これは%(resUser)s!!!', \
					u'@%(resUser)s 俺はノンケでもﾍﾟﾛﾍﾟﾛしちまう男なんだぜ ﾍﾟﾛﾍﾟﾛ' \
					]

				# 呟くメッセージを作成
				msg = self.resTweetTrim( Utils.randomChoice(tweetlist) % {'resUser':m[1]}, m[2])

				slst.append((msg, m[0]))

		# 作成した返信をツイート
		self.html.append(u'<hr/>')
		for s in slst:
			self.update(s[0], s[1])
			self.html.append(u''.join([s[0], u'<br/>']))
		self.html.append(u'<hr/>')


	# とおるさんが激しく同意する機能
	def douiTweet(self, mentionList):

		self.html.append(u'<li>doui</li>')

		# 発言リストの初期化
		slst = []

		# Mentionの情報を処理
		for m in mentionList:

			# 発言チェッカーに設定
			tc = TweetChecker.TweetChecker(m[2])
			# 質問なら返信
			if tc.isQuestion():

				tweetlist = [ \
					u'@%(resUser)s ぼくもそう思ってます', \
					u'@%(resUser)s そうですねー', \
					u'@%(resUser)s ぼく、前からそう思ってます！ﾌﾌﾝ', \
					u'@%(resUser)s そうですよ。本当のことですから。', \
					u'@%(resUser)s 間違いないですね。', \
					u'@%(resUser)s %(resUser)sさんも同じだと思ってるんですね', \
					u'@%(resUser)s そうなんですよ！' \
					]

				# 呟くメッセージを作成
				msg = self.resTweetTrim( Utils.randomChoice(tweetlist) % {'resUser':m[1]}, m[2])

				slst.append((msg, m[0]))

		# 作成した返信をツイート
		self.html.append(u'<hr/>')
		for s in slst:
			self.update(s[0], s[1])
			self.html.append(u''.join([s[0], u'<br/>']))
		self.html.append(u'<hr/>')

	# そんなとおるさんで大丈夫か？機能
	def enochTweet(self, mentionList):

		self.html.append(u'<li>enoch</li>')

		# 発言リストの初期化
		slst = []

		# Mentionの情報を処理
		for m in mentionList:

			# 発言チェッカーに設定
			tc = TweetChecker.TweetChecker(m[2])
			# 大丈夫か？だったら
			if tc.isDaijyoubuka():

				tweetlist = [ \
					u'@%(resUser)s 大丈夫だ問題ない。' \
					]
#					u'@%(resUser)s 大丈夫じゃない問題ある。' \


				# 呟くメッセージを作成
				msg = self.resTweetTrim(Utils.randomChoice(tweetlist) % {'resUser':m[1]}, m[2])

				slst.append((msg, m[0]))

		# 作成した返信をツイート
		self.html.append(u'<hr/>')
		for s in slst:
			self.update(s[0], s[1])
			self.html.append(u''.join([s[0], u'<br/>']))
		self.html.append(u'<hr/>')

	# おみくじ機能
	def omikujiTweet(self, mentionList):

		self.html.append(u'<li>omikuji</li>')

		# 発言リストの初期化
		slst = []

		# Mentionの情報を処理
		for m in mentionList:

			# 発言チェッカーに設定
			tc = TweetChecker.TweetChecker(m[2])
			# おみくじだったら
			if tc.isOmikuji():

				ds = DataStore.DataStore()

				lst = ds.getStatuses(DataStore.Type.omikuji)
				tweetList = [s[1] for s in lst]
				# 呟くメッセージを作成
				msg = self.resTweetTrim( u' '.join([u'@%(resUser)s',Utils.randomChoice(tweetList)]) % {'resUser':m[1]}, m[2])
				slst.append((msg, m[0]))

		# 作成した返信をツイート
		self.html.append(u'<hr/>')
		for s in slst:
			self.update(s[0], s[1])
			self.html.append(u''.join([s[0], u'<br/>']))
		self.html.append(u'<hr/>')

	# おみくじ追加機能
	def omikujiAdd(self, mentionList):

		self.html.append(u'<li>omikujiAdd</li>')

		# 発言リストの初期化
		slst = []

		# Mentionの情報を処理
		for m in mentionList:

			# 発言チェッカーに設定
			tc = TweetChecker.TweetChecker(m[2])
			# おみくじだったら
			if tc.isOmikujiAdd():

				ds = DataStore.DataStore()

				se = re.search(u'「(.*)」', m[2])

				if se and se.group(1) != u'':
					omikuji = se.group(1)
					ds.addStatus(DataStore.Type.omikuji, omikuji)

					# 呟くメッセージを作成
					msg = self.resTweetTrim(u'@%(resUser)s 「%(omikuji)s」を追加したよ！' % {'resUser':m[1], 'omikuji':omikuji}, m[2])
					slst.append((msg, m[0]))

		# 作成した返信をツイート
		self.html.append(u'<hr/>')
		for s in slst:
			self.update(s[0], s[1])
			self.html.append(u''.join([s[0], u'<br/>']))
		self.html.append(u'<hr/>')

	# 処理するMentionのリストを作成する
	def createMentionList(self):
		# DataStore制御を生成
		ds = DataStore.DataStore()

		# 処理済のMentionIDを取得
		id = ds.getMentionId()
		updateId = 0

		# Mentionの情報を取得
		mlstOrg = self.getMentions()
		mlst = []

		for m in mlstOrg:

			# チェック開始時のIDをチェック完了位置として記憶
			if updateId == 0:
				updateId = m[0]

			# 処理済IDの場合、終了
			if id == m[0]:
				break

			# 自分のステータスは処理しない
			if u'ToruBot' == m[1]:
				continue

			# RT以降をを勘違いしないように外す
			match = re.match(u'(.*)RT .*', m[2])
			if match:
				m = (m[0], m[1], match.group(1).rstrip())

			mlst.append(m)

		if len(mlstOrg):
			# チェック済みのIDを更新
			ds.setMentionId(mlstOrg[0][0])

		return mlst

	# Mentionからの返信
	def mentionReplyHandler(self):

		# 処理するMentionのリストを作成
		mlst = self.createMentionList()

		# イヤッホゥ機能
		self.iyahoTweet(mlst)

		# ウッヒョウ機能
		self.uhyouTweet(mlst)

		# 俺はノンケでもペロペロしちまう機能
		self.peroperoTweet(mlst)

		# とおるさんが激しく同意する機能
		self.douiTweet(mlst)

		# そんなとおるさんで大丈夫か？機能
		self.enochTweet(mlst)

		# おみくじ機能
		self.omikujiTweet(mlst)

		# おみくじ追加機能
		self.omikujiAdd(mlst)

	def handler(self):
		self.html.append(u'<b>reply handler start</b><br/>')

		# Mentionからの返信
		self.mentionReplyHandler()

		self.html.append(u'<b>mention handler end</b><br/>')

# 単体エントリ
def main():
	pass

if __name__ == '__main__':
	print main()

