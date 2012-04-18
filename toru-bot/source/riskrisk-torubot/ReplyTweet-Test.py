#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import datetime

import nose
from nose.tools import *
import mox

import BaseGAETest

from ReplyTweet import *

import DataStore

import GCalendar

import Env
Env.Custom.set()

import tweepy

class TestReplyTweet(BaseGAETest.BaseGAETest):

	mocker = mox.Mox()

	def test_MakeTweet(self):
		# 元のメッセージを作成
		msg = u'Tweet Message'
		org_msg = u'Original Message'

		# 返信制御クラスを作成
		rt = ReplyTweet()

		# メッセージを作成
		tweet_msg = rt.resTweetTrim(msg, org_msg)

		# 予想通りのメッセージが作成されること
		assert_equal(u''.join([msg, u' (', org_msg, u')']), tweet_msg)

	def test_TweetTrim(self):

		# 元になる文字列を作成（とりあえず100文字)
		s = u'0123456789'
		slst= []
		for i in range(0, 10):
			slst.append(s)

		# 返信元文字列を作成（とりあえず100文字）
		org_s = u'0123456789'
		org_slst= []
		for i in range(0, 10):
			org_slst.append(org_s)

		# 返信制御クラスを作成
		rt = ReplyTweet()

		# トリムを実行（計200文字なので、139文字にトリムされる））
		msg = rt.resTweetTrim(u''.join(slst), u''.join(org_slst))

		m = re.match(u'.*\(.*\)', msg)

		assert_true(m)
		assert_equal(139, len(msg))

	def test_Iyaho(self):

		# 返信制御クラスを作成
		rt = ReplyTweet()

		# updateをモック
		self.mocker.StubOutWithMock(rt, "update")

		# 再現を初期化
		self.mocker.ResetAll()

		# 動作を記録
		rt.update(mox.Regex(u'@user1 .* \(1イヤッホウ！\)'), 100)
		rt.update(mox.Regex(u'@user2 .* \(2イヤッホウ！\)'), 200)
		rt.update(mox.Regex(u'@user3 .* \(3イヤッホウ！\)'), 300)

		# 再現を開始
		self.mocker.ReplayAll()

		mlist =[\
			(100, u'user1', u'1イヤッホウ！'), \
			(200, u'user2', u'2イヤッホウ！'), \
			(300, u'user3', u'3イヤッホウ！') \
			]
		rt.iyahoTweet(mlist)

		# 再現を検証
		self.mocker.VerifyAll()

	def test_Uhyou(self):

		# 返信制御クラスを作成
		rt = ReplyTweet()

		# updateをモック
		self.mocker.StubOutWithMock(rt, "update")

		# 再現を初期化
		self.mocker.ResetAll()

		# 動作を記録
		rt.update(mox.Regex(u'@user1 .* \(1ウッヒョウ！\)'), 100)
		rt.update(mox.Regex(u'@user2 .* \(2ウッヒョウ！\)'), 200)
		rt.update(mox.Regex(u'@user3 .* \(3ウッヒョウ！\)'), 300)

		# 再現を開始
		self.mocker.ReplayAll()

		mlist =[\
			(100, u'user1', u'1ウッヒョウ！'), \
			(200, u'user2', u'2ウッヒョウ！'), \
			(300, u'user3', u'3ウッヒョウ！') \
			]
		rt.uhyouTweet(mlist)

		# 再現を検証
		self.mocker.VerifyAll()

	def test_Peroepero(self):

		# 返信制御クラスを作成
		rt = ReplyTweet()

		# updateをモック
		self.mocker.StubOutWithMock(rt, "update")

		# 再現を初期化
		self.mocker.ResetAll()

		# 動作を記録
		rt.update(mox.Regex(u'@user1 .* \(1ペロペロ！\)'), 100)
		rt.update(mox.Regex(u'@user2 .* \(2ペロペロ！\)'), 200)
		rt.update(mox.Regex(u'@user3 .* \(3ペロペロ！\)'), 300)

		# 再現を開始
		self.mocker.ReplayAll()

		mlist =[\
			(100, u'user1', u'1ペロペロ！'), \
			(200, u'user2', u'2ペロペロ！'), \
			(300, u'user3', u'3ペロペロ！') \
			]
		rt.peroperoTweet(mlist)

		# 再現を検証
		self.mocker.VerifyAll()

	def test_Doui(self):

		# 返信制御クラスを作成
		rt = ReplyTweet()

		# updateをモック
		self.mocker.StubOutWithMock(rt, "update")

		# 再現を初期化
		self.mocker.ResetAll()

		# 動作を記録
		rt.update(mox.Regex(u'@user1 .* \(1そうですか？\)'), 100)
		rt.update(mox.Regex(u'@user2 .* \(2そうですか？\)'), 200)
		rt.update(mox.Regex(u'@user3 .* \(3そうですか？\)'), 300)

		# 再現を開始
		self.mocker.ReplayAll()

		mlist =[\
			(100, u'user1', u'1そうですか？'), \
			(200, u'user2', u'2そうですか？'), \
			(300, u'user3', u'3そうですか？') \
			]
		rt.douiTweet(mlist)

		# 再現を検証
		self.mocker.VerifyAll()

	def test_enoch(self):

		# 返信制御クラスを作成
		rt = ReplyTweet()

		# updateをモック
		self.mocker.StubOutWithMock(rt, "update")

		# 再現を初期化
		self.mocker.ResetAll()

		# 動作を記録
		rt.update(mox.Regex(u'@user1 .* \(1そんな装備で大丈夫か？\)'), 100)
		rt.update(mox.Regex(u'@user2 .* \(2そんな装備で大丈夫か？\)'), 200)
		rt.update(mox.Regex(u'@user3 .* \(3そんな装備でイーノック？\)'), 300)

		# 再現を開始
		self.mocker.ReplayAll()

		mlist =[\
			(100, u'user1', u'1そんな装備で大丈夫か？'), \
			(200, u'user2', u'2そんな装備で大丈夫か？'), \
			(300, u'user3', u'3そんな装備でイーノック？') \
			]
		rt.enochTweet(mlist)

		# 再現を検証
		self.mocker.VerifyAll()

	def test_Omikuji(self):

		ds = DataStore.DataStore()

		ds.addStatus(DataStore.Type.omikuji, u'大吉')
		ds.addStatus(DataStore.Type.omikuji, u'中吉')
		ds.addStatus(DataStore.Type.omikuji, u'小吉')

		# 返信制御クラスを作成
		rt = ReplyTweet()

		# updateをモック
		self.mocker.StubOutWithMock(rt, "update")

		# 再現を初期化
		self.mocker.ResetAll()

		# 動作を記録
		rt.update(mox.Regex(u'@user1 .* \(1おみくじちょうだい！\)'), 100)
		rt.update(mox.Regex(u'@user2 .* \(2おみくじちょうだい！\)'), 200)
		rt.update(mox.Regex(u'@user3 .* \(3おみくじちょうだい！\)'), 300)

		# 再現を開始
		self.mocker.ReplayAll()

		mlist =[\
			(100, u'user1', u'1おみくじちょうだい！'), \
			(200, u'user2', u'2おみくじちょうだい！'), \
			(300, u'user3', u'3おみくじちょうだい！') \
			]
		rt.omikujiTweet(mlist)

		# 再現を検証
		self.mocker.VerifyAll()


	def test_OmikujiAdd(self):

		ds = DataStore.DataStore()

		# 返信制御クラスを作成
		rt = ReplyTweet()

		# updateをモック
		self.mocker.StubOutWithMock(rt, "update")

		mlist =[\
			(100, u'user1', u'くじ追加「大吉」'), \
			(200, u'user2', u'くじ追加「中吉」'), \
			(300, u'user3', u'くじ追加「小吉」') \
			]
		rt.omikujiAdd(mlist)

		lst = ds.getStatuses(DataStore.Type.omikuji)

		assert_equal(u'大吉', lst[0][1])
		assert_equal(u'中吉', lst[1][1])
		assert_equal(u'小吉', lst[2][1])

	def test_OmikujiAddEmpty(self):

		ds = DataStore.DataStore()

		# 返信制御クラスを作成
		rt = ReplyTweet()

		mlist =[\
			(100, u'user1', u'くじ追加「」'), \
			(200, u'user2', u'くじ追加'), \
			]
		rt.omikujiAdd(mlist)

		lst = ds.getStatuses(DataStore.Type.omikuji)

		assert_equal(0, len(lst))

	def test_createMentionList(self):

		# 返信制御クラスの作成
		rt = ReplyTweet()

		# メンション取得をモック
		self.mocker.StubOutWithMock(rt, "getMentions")

		# 再現を初期化
		self.mocker.ResetAll()

		rt.getMentions().AndReturn([ \
			(300, u'test3', u'message3'), \
			(200, u'test2', u'message2'), \
			(100, u'test1', u'message1') \
			])

		# 再現を開始
		self.mocker.ReplayAll()

		lst = rt.createMentionList()

		assert_equal((300, u'test3', u'message3'), lst[0])
		assert_equal((200, u'test2', u'message2'), lst[1])
		assert_equal((100, u'test1', u'message1'), lst[2])

		# 再現を検証
		self.mocker.VerifyAll()

	def test_createMentionListCheckId(self):

		# 返信制御クラスの作成
		rt = ReplyTweet()

		# チェック済みIDに200を設定
		ds = DataStore.DataStore()
		ds.setMentionId(200)

		# メンション取得をモック
		self.mocker.StubOutWithMock(rt, "getMentions")

		# 再現を初期化
		self.mocker.ResetAll()

		rt.getMentions().AndReturn([ \
			(300, u'test3', u'message3'), \
			(200, u'test2', u'message2'), \
			(100, u'test1', u'message1') \
			])

		# 再現を開始
		self.mocker.ReplayAll()

		lst = rt.createMentionList()

		assert_equal((300, u'test3', u'message3'), lst[0])

		# 再現を検証
		self.mocker.VerifyAll()

	def test_createMentionListMyself(self):

		# 返信制御クラスの作成
		rt = ReplyTweet()

		# メンション取得をモック
		self.mocker.StubOutWithMock(rt, "getMentions")

		# 再現を初期化
		self.mocker.ResetAll()

		rt.getMentions().AndReturn([ \
			(300, u'test3', u'message3'), \
			(200, u'ToruBot', u'message2'), \
			(100, u'test1', u'message1') \
			])

		# 再現を開始
		self.mocker.ReplayAll()

		lst = rt.createMentionList()

		assert_equal((300, u'test3', u'message3'), lst[0])
		assert_equal((100, u'test1', u'message1'), lst[1])

		# 再現を検証
		self.mocker.VerifyAll()

	def test_createMentionListRT(self):

		# 返信制御クラスの作成
		rt = ReplyTweet()

		# メンション取得をモック
		self.mocker.StubOutWithMock(rt, "getMentions")

		# 再現を初期化
		self.mocker.ResetAll()

		rt.getMentions().AndReturn([ \
			(300, u'test3', u'message3'), \
			(200, u'test2', u'message2 RT RTMessage!'), \
			(201, u'test4', u'よかった。RT @ToruBot: @riskrisk 大丈夫だ問題ない。 (そろそろ@torubotの件でひっぱたかれる予感があるが大丈夫か？)'), \
			(100, u'test1', u'message1') \
			])

		# 再現を開始
		self.mocker.ReplayAll()

		lst = rt.createMentionList()

		assert_equal((300, u'test3', u'message3'), lst[0])
		assert_equal((200, u'test2', u'message2'), lst[1])
		assert_equal((201, u'test4', u'よかった。'), lst[2])
		assert_equal((100, u'test1', u'message1'), lst[3])

		# 再現を検証
		self.mocker.VerifyAll()


	def test_MentionReplyHandler(self):

		# 返信制御クラスの作成
		rt = ReplyTweet()

		mlist =[\
			(100, u'user1', u'1ハンドラ'), \
			(200, u'user2', u'2ハンドラ'), \
			(300, u'user3', u'3ハンドラ') \
			]

		# 各エントリをモック
		self.mocker.StubOutWithMock(rt, "createMentionList")
		self.mocker.StubOutWithMock(rt, "iyahoTweet")
		self.mocker.StubOutWithMock(rt, "uhyouTweet")
		self.mocker.StubOutWithMock(rt, "peroperoTweet")
		self.mocker.StubOutWithMock(rt, "douiTweet")
		self.mocker.StubOutWithMock(rt, "enochTweet")
		self.mocker.StubOutWithMock(rt, "omikujiTweet")
		self.mocker.StubOutWithMock(rt, "omikujiAdd")

		# 再現を初期化
		self.mocker.ResetAll()

		# 動作を記録
		rt.createMentionList().AndReturn(mlist)
		rt.iyahoTweet(mlist)
		rt.uhyouTweet(mlist)
		rt.peroperoTweet(mlist)
		rt.douiTweet(mlist)
		rt.enochTweet(mlist)
		rt.omikujiTweet(mlist)
		rt.omikujiAdd(mlist)

		# 再現を開始
		self.mocker.ReplayAll()

		rt.mentionReplyHandler()

		# 再現を検証
		self.mocker.VerifyAll()


	def test_Handler(self):

		# 周期ツイート制御のインスタンスを生成
		rt = ReplyTweet()

		# 各ハンドラをモックする
		self.mocker.StubOutWithMock(rt, "mentionReplyHandler")

		# 記録をリセット
		self.mocker.ResetAll()

		# 呼び出しの記録
		rt.mentionReplyHandler()

		# 再現動作の開始
		self.mocker.ReplayAll()

		# ツイート
		rt.handler()

		# 実動作の検証
		self.mocker.VerifyAll()


def main():
	pass

if __name__ == '__main__':
	main()

