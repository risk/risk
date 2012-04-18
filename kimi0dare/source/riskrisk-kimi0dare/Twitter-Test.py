#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import Env
Env.Custom.set()

import nose
from nose.tools import *
import mox
import BaseGAETest

from Twitter import *
import tweepy

class TestTweetChecker(BaseGAETest.BaseGAETest):

	# moxを作成
	mocker = mox.Mox()

	def setUp(self):
		BaseGAETest.BaseGAETest.setUp(self)

	def test_MakeApi(self):
		twitter = Twitter()
		assert_true(twitter.api)

	def test_TweetEnableDisable(self):

		# Twitter制御クラスの作成
		twitter = Twitter()

		assert_true(twitter.isEnable)
		twitter.setDisable()
		assert_false(twitter.isEnable)
		twitter.setEnable()
		assert_true(twitter.isEnable)

	def test_TweetControl(self):

		# APIのモックを作成
		apiMock = self.mocker.CreateMock(tweepy.API)

		# Twitter制御クラスの作成
		twitter = Twitter()

		# モックのインタフェースを設定
		twitter.api = apiMock

		# Enable状態
		twitter.setEnable()

		# 動作記録をリセット
		self.mocker.ResetAll()

		# [動作記録]ステータスのアップデート
		apiMock.update_status(u'test')

		# 動作検証の開始
		self.mocker.ReplayAll()

		twitter.update(u'test')

		# 実動作の確認(正しくないとエラーが出るよ)
		self.mocker.VerifyAll()

		# Disable状態
		twitter.setDisable()

		# 動作記録をリセット
		self.mocker.ResetAll()

		# 動作検証の開始
		self.mocker.ReplayAll()

		twitter.update(u'test')

		# 実動作の確認(正しくないとエラーが出るよ)
		self.mocker.VerifyAll()

	def test_GetMention(self):
		# モックのインタフェースを作成
		apiMock = self.mocker.CreateMock(tweepy.API)

		# モックの戻り値クラスを作成
		userMock = self.mocker.CreateMock(tweepy.models.User)
		userMock.screen_name = u'testuser'
		statusMock = self.mocker.CreateMock(tweepy.models.Status)
		statusMock.id=100
		statusMock.text=u'test status'
		statusMock.user=userMock

		# Twitterクラスを作成
		twitter = Twitter()

		# 対象クラスにMockインタフェースの設定
		twitter.api = apiMock

		# 動作記録をリセット
		self.mocker.ResetAll()

		# 動作の記録
		apiMock.mentions().AndReturn([statusMock])

		# 動作検証の開始
		self.mocker.ReplayAll()

		lst = twitter.getMentions()

		# 実動作の確認(正しくないとエラーが出るよ)
		self.mocker.VerifyAll()

		# 戻り値が1件であること
		assert_equal(1, len(lst))

		# 正しいデータが取得できること
		assert_equal(100, lst[0][0])
		assert_equal(u'testuser', lst[0][1])
		assert_equal(u'test status', lst[0][2])

	def test_GetMentions(self):
		# モックのインタフェースを作成
		apiMock = self.mocker.CreateMock(tweepy.API)

		# モックの戻り値クラスを作成1
		userMock1 = self.mocker.CreateMock(tweepy.models.User)
		userMock1.screen_name = u'testuser1'
		statusMock1 = self.mocker.CreateMock(tweepy.models.Status)
		statusMock1.id=100
		statusMock1.text=u'test1 status'
		statusMock1.user=userMock1

		# モックの戻り値クラスを作成2
		userMock2 = self.mocker.CreateMock(tweepy.models.User)
		userMock2.screen_name = u'testuser2'
		statusMock2 = self.mocker.CreateMock(tweepy.models.Status)
		statusMock2.id=200
		statusMock2.text=u'test2 status'
		statusMock2.user=userMock2

		# Twitterクラスを作成
		twitter = Twitter()

		# 対象クラスにMockインタフェースの設定
		twitter.api = apiMock

		# 動作記録をリセット
		self.mocker.ResetAll()

		# 動作の記録
		apiMock.mentions().AndReturn([statusMock1, statusMock2])

		# 動作検証の開始
		self.mocker.ReplayAll()

		lst = twitter.getMentions()

		# 実動作の確認(正しくないとエラーが出るよ)
		self.mocker.VerifyAll()

		# 戻り値が2件であること
		assert_equal(2, len(lst))

		# 正しいデータが取得できること
		assert_equal(100, lst[0][0])
		assert_equal(u'testuser1', lst[0][1])
		assert_equal(u'test1 status', lst[0][2])

		assert_equal(200, lst[1][0])
		assert_equal(u'testuser2', lst[1][1])
		assert_equal(u'test2 status', lst[1][2])

	def test_GetUserTimeline(self):
		# モックのインタフェースを作成
		apiMock = self.mocker.CreateMock(tweepy.API)

		# モックの戻り値クラスを作成
		statusMock = self.mocker.CreateMock(tweepy.models.Status)
		statusMock.id=100
		statusMock.text=u'test status'

		# Twitterクラスを作成
		twitter = Twitter()

		# 対象クラスにMockインタフェースの設定
		twitter.api = apiMock

		# 動作記録をリセット
		self.mocker.ResetAll()

		# 動作の記録
		apiMock.user_timeline(id=u'test').AndReturn([statusMock])

		# 動作検証の開始
		self.mocker.ReplayAll()

		lst = twitter.getUserTL(u'test')

		# 実動作の確認(正しくないとエラーが出るよ)
		self.mocker.VerifyAll()

		# 戻り値が1件であること
		assert_equal(1, len(lst))

		# 正しいデータが取得できること
		assert_equal(100, lst[0][0])
		assert_equal(u'test status', lst[0][1])

	def test_GetUserTimelines(self):
		# モックのインタフェースを作成
		apiMock = self.mocker.CreateMock(tweepy.API)

		# モックの戻り値クラスを作成
		statusMock1 = self.mocker.CreateMock(tweepy.models.Status)
		statusMock1.id=100
		statusMock1.text=u'test1 status'

		# モックの戻り値クラスを作成
		statusMock2 = self.mocker.CreateMock(tweepy.models.Status)
		statusMock2.id=200
		statusMock2.text=u'test2 status'

		# Twitterクラスを作成
		twitter = Twitter()

		# 対象クラスにMockインタフェースの設定
		twitter.api = apiMock

		# 動作記録をリセット
		self.mocker.ResetAll()

		# 動作の記録
		apiMock.user_timeline(id=u'test').AndReturn([statusMock1, statusMock2])

		# 動作検証の開始
		self.mocker.ReplayAll()

		lst = twitter.getUserTL(u'test')

		# 実動作の確認(正しくないとエラーが出るよ)
		self.mocker.VerifyAll()

		# 戻り値が2件であること
		assert_equal(2, len(lst))

		# 正しいデータが取得できること
		assert_equal(100, lst[0][0])
		assert_equal(u'test1 status', lst[0][1])

		assert_equal(200, lst[1][0])
		assert_equal(u'test2 status', lst[1][1])

	def test_Update(self):
		# モックのインタフェースを作成
		apiMock = self.mocker.CreateMock(tweepy.API)

		# Twitterクラスを作成
		twitter = Twitter()

		# 対象クラスにMockインタフェースの設定
		twitter.api = apiMock

		# 動作記録をリセット
		self.mocker.ResetAll()

		# 動作の記録
		apiMock.update_status('test')

		# 動作記録
		self.mocker.ReplayAll()

		twitter.update("test");

		# 実動作の確認(正しくないとエラーが出るよ)
		self.mocker.VerifyAll()

	def test_UpdateDisableProperty(self):
		# モックのインタフェースを作成
		apiMock = self.mocker.CreateMock(tweepy.API)

		# Twitterクラスを作成
		twitter = Twitter()

		# 対象クラスにMockインタフェースの設定
		twitter.api = apiMock

		# ツイート不可に設定
		twitter.setDisable()

		# 動作記録をリセット
		self.mocker.ResetAll()

		# 動作記録
		self.mocker.ReplayAll()

		twitter.update("test");

		# 実動作の確認(正しくないとエラーが出るよ)
		self.mocker.VerifyAll()

	def test_UpdateReply(self):
		# モックのインタフェースを作成
		apiMock = self.mocker.CreateMock(tweepy.API)

		# Twitterクラスを作成
		twitter = Twitter()

		# 対象クラスにMockインタフェースの設定
		twitter.api = apiMock

		# 動作記録をリセット
		self.mocker.ResetAll()

		# 動作の記録
		apiMock.update_status('test', 12345)

		# 動作検証の開始
		self.mocker.ReplayAll()

		twitter.update('test', 12345);

		# 実動作の確認(正しくないとエラーが出るよ)
		self.mocker.VerifyAll()

	def test_Refollow(self):

		# モックのインタフェースを作成
		apiMock = self.mocker.CreateMock(tweepy.API)

		# ユーザーのモックを作成
		userMock = self.mocker.CreateMock(tweepy.models.User)
		userMock.id = 10

		userLockMock = self.mocker.CreateMock(tweepy.models.User)
		userLockMock.id =400
		userLockMock.protected = True

		userUnlockMock = self.mocker.CreateMock(tweepy.models.User)
		userUnlockMock.id = 500
		userUnlockMock.protected = False

		# Twitterクラスを作成
		twitter = Twitter()

		# 対象クラスにMockインタフェースの設定
		twitter.api = apiMock

		# 動作記録をリセット
		self.mocker.ResetAll()

		# 動作の記録
		apiMock.me().AndReturn(userMock)
		apiMock.friends_ids(id=10).AndReturn([100, 200, 300, 1000])
		apiMock.followers_ids(id=10).AndReturn([200, 300, 400, 500])


		apiMock.get_user(id=400).AndReturn(userLockMock)
		apiMock.get_user(id=500).AndReturn(userUnlockMock)
		apiMock.create_friendship(id=500)

		# 動作検証の開始
		self.mocker.ReplayAll()

		# リフォロー機能
		twitter.refollow();

		# 実動作の確認(正しくないとエラーが出るよ)
		self.mocker.VerifyAll()



def main():
	pass

if __name__ == '__main__':
	main()

