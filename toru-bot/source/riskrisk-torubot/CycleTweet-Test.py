#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import datetime

import nose
from nose.tools import *
import mox

import BaseGAETest

from CycleTweet import *

import DataStore

import GCalendar

import Env
Env.Custom.set()

import tweepy

class TestCycleTweet(BaseGAETest.BaseGAETest):

	mocker = mox.Mox()
	tweetList = [u'test1', u'test2', u'test3', u'test4', u'test5']

	def setUp(self):
		BaseGAETest.BaseGAETest.setUp(self)

		# ダミーデータの設定
		ds = DataStore.DataStore()

		# ツイートを有効に設定
		ds.setTweetEnable(True)

		# 通常ツイートの設定
		for s in self.tweetList:
			ds.addStatus(DataStore.Type.normal, s)

	def test_OtherTweet(self):

		# 周期ツイート制御のインスタンスを生成
		ct = CycleTweet(datetime.datetime(2011, 2, 23, 10, 0))

		# 呟きの取得
		s = ct.otherTweet()

		# 何か呟きが取得できていること
		m = re.match(u'(.*)\d\(.*\)', s)
		if m: s = m.group(1)
		assert_equals(u'test', s)

		ds = DataStore.DataStore()
		detect = False
		lst = ds.getStatuses(DataStore.Type.normal)
		for st in lst:
			if st[3] != 0:
				detect = True
		assert_true(detect)

	def test_OtherTweetChoice(self):

		# 周期ツイート制御のインスタンスを生成
		ct = CycleTweet(datetime.datetime(2011, 2, 23, 10, 0))

		# 呟きの取得
		s = ct.otherTweet()

		# 呟きの取得
		s = ct.otherTweet()

		# 呟きの取得
		s = ct.otherTweet()

	def test_PriorityTweet(self):

		# ダミーデータの設定
		ds = DataStore.DataStore()

		# 優先ツイートの設定
		ds.addStatus(DataStore.Type.priority, u'prio1')

		# 周期ツイート制御のインスタンスを生成
		ct = CycleTweet(datetime.datetime(2011, 2, 23, 8, 0))

		# 優先ツイートが取得できること
		s = ct.otherTweet()
		m = re.match(u'(.*)\(.*\)', s)
		if m: s = m.group(1)
		assert_equal(u'prio1', s)

		# 通常ツイートに戻ること
		s = ct.otherTweet()
		m = re.match(u'(.*)\(.*\)', s)
		if m: s = m.group(1)
		assert_not_equal(u'prio1', s)

	def test_NekorobiOpen(self):
		# 周期ツイート制御のインスタンスを生成
		ct = CycleTweet(datetime.datetime(2011, 1, 2, 0, 0))

		# 開店メッセージの取得
		s = ct.nekorobiOpen()

		# 開店用メッセージが取得できること
		assert_equal(u'1月2日です！今日も一日がんばりましィィヤッホォォォォゥ！', s)

	def test_NekorobiClone(self):
		# 周期ツイート制御のインスタンスを生成
		ct = CycleTweet(datetime.datetime(2011, 3, 4, 0, 0))

		# 閉店メッセージの取得
		s = ct.nekorobiClose()

		# 閉店用メッセージが取得できること
		assert_equal(u'3月4日でした！今日も一日お疲れさまでしィィヤッホォォォォゥ！', s)

	def test_todaySchedule(self):
		# 周期ツイート制御のインスタンスを生成
		ct = CycleTweet(datetime.datetime(2011, 5, 6, 0, 0))

		# カレンダー制御のモックを作成
		gcalMock = self.mocker.CreateMockAnything()

		# 記録をリセット
		self.mocker.ResetAll()

		# 呼び出しの記録
		gcalMock.getDateInfo(mox.IsA(datetime.datetime.now())).AndReturn(u'test')

		# 再現動作の開始
		self.mocker.ReplayAll()

		# 当日スケジュール取得
		s = ct.todaySchedule(gcalMock)

		# 実動作の検証
		self.mocker.VerifyAll()

		# 当日用イベントメッセージが取得できること
		assert_equal(u'きなこちゃん、今日は「test」だよぉ ﾌﾋﾋﾋﾋﾋ', s)

	def test_TomorrowSchedule(self):
		# 周期ツイート制御のインスタンスを生成
		ct = CycleTweet(datetime.datetime(2011, 7, 8, 0, 0))

		# カレンダー制御のモックを作成
		gcalMock = self.mocker.CreateMockAnything()

		# 記録をリセット
		self.mocker.ResetAll()

		# 呼び出しの記録
		gcalMock.getDateInfo(mox.IsA(datetime.datetime.now())).AndReturn(u'test')

		# 再現動作の開始
		self.mocker.ReplayAll()

		# 翌日スケジュールの取得
		s = ct.tomorrowSchedule(gcalMock)

		# 実動作の検証
		self.mocker.VerifyAll()

		# 翌日用イベントメッセージ
		assert_equal(u'きなこちゃん、明日は「test」だよぉ ｸﾞﾍﾍﾍﾍ', s)

	def test_ScheduleHandlerToday(self):

		# 周期ツイート制御のインスタンスを生成
		ct = CycleTweet(datetime.datetime(2011, 9, 10, 10, 50))
		# カレンダーのダミーファイルを指定
		ct.calUrl = u'./gcaltest.xml'

		# tweepyAPIのモックを作成
		apiMock = self.mocker.CreateMock(tweepy.API)

		# モックをテスト対象に設定
		ct.api = apiMock

		# スケジュール取得関数をモック化
		self.mocker.StubOutWithMock(ct, "todaySchedule")
		self.mocker.StubOutWithMock(ct, "tomorrowSchedule")

		# 記録をリセット
		self.mocker.ResetAll()

		# 呼び出しの記録
		ct.todaySchedule(mox.IsA(GCalendar.GCalendar)).AndReturn(u'today')
		apiMock.update_status(u'today')

		# 再現動作の開始
		self.mocker.ReplayAll()

		# スケジュール制御のハンドラ呼び出し
		ct.scheduleHandler()

		# 実動作の検証
		self.mocker.VerifyAll()

	def test_ScheduleHandlerTomorrow(self):

		# 周期ツイート制御のインスタンスを生成
		ct = CycleTweet(datetime.datetime(2011, 11, 12, 22, 50))
		# カレンダーのダミーファイルを指定
		ct.calUrl = u'./gcaltest.xml'

		# tweepyAPIのモックを作成
		apiMock = self.mocker.CreateMock(tweepy.API)

		# モックをテスト対象に設定
		ct.api = apiMock

		# スケジュール取得関数をモック化
		self.mocker.StubOutWithMock(ct, "todaySchedule")
		self.mocker.StubOutWithMock(ct, "tomorrowSchedule")

		# 記録をリセット
		self.mocker.ResetAll()

		# 呼び出しの記録
		ct.tomorrowSchedule(mox.IsA(GCalendar.GCalendar)).AndReturn(u'tomorrow')
		apiMock.update_status(u'tomorrow')

		# 再現動作の開始
		self.mocker.ReplayAll()

		# スケジュール制御のハンドラ呼び出し
		ct.scheduleHandler()

		# 実動作の検証
		self.mocker.VerifyAll()

	def test_CycleHandlerOpen(self):
		# 周期ツイート制御のインスタンスを生成
		ct = CycleTweet(datetime.datetime(2012, 1, 2, 11, 00))

		# tweepyAPIのモックを作成
		apiMock = self.mocker.CreateMock(tweepy.API)

		# モックをテスト対象に設定
		ct.api = apiMock

		# ツイート生成関数をモック化
		self.mocker.StubOutWithMock(ct, "nekorobiOpen")
		self.mocker.StubOutWithMock(ct, "nekorobiClose")
		self.mocker.StubOutWithMock(ct, "otherTweet")

		# 記録をリセット
		self.mocker.ResetAll()

		# 呼び出しの記録
		ct.nekorobiOpen().AndReturn(u'open')
		apiMock.update_status(u'open')

		# 再現動作の開始
		self.mocker.ReplayAll()

		# 周期制御のハンドラ呼び出し
		ct.cycleHandler()

		# 実動作の検証
		self.mocker.VerifyAll()

	def test_CycleHandlerClose(self):
		# 周期ツイート制御のインスタンスを生成
		ct = CycleTweet(datetime.datetime(2012, 3, 4, 23, 00))

		# tweepyAPIのモックを作成
		apiMock = self.mocker.CreateMock(tweepy.API)

		# モックをテスト対象に設定
		ct.api = apiMock

		# スケジュール取得関数をモック化
		self.mocker.StubOutWithMock(ct, "nekorobiOpen")
		self.mocker.StubOutWithMock(ct, "nekorobiClose")
		self.mocker.StubOutWithMock(ct, "otherTweet")

		# 記録をリセット
		self.mocker.ResetAll()

		# 呼び出しの記録
		ct.nekorobiClose().AndReturn(u'close')
		apiMock.update_status(u'close')

		# 再現動作の開始
		self.mocker.ReplayAll()

		# 周期制御のハンドラ呼び出し
		ct.cycleHandler()

		# 実動作の検証
		self.mocker.VerifyAll()

	def test_CycleHandlerOther(self):
		# 周期ツイート制御のインスタンスを生成
		ct = CycleTweet(datetime.datetime(2012, 3, 4, 13, 00))

		# tweepyAPIのモックを作成
		apiMock = self.mocker.CreateMock(tweepy.API)

		# モックをテスト対象に設定
		ct.api = apiMock

		# スケジュール取得関数をモック化
		self.mocker.StubOutWithMock(ct, "nekorobiOpen")
		self.mocker.StubOutWithMock(ct, "nekorobiClose")
		self.mocker.StubOutWithMock(ct, "otherTweet")

		# 記録をリセット
		self.mocker.ResetAll()

		# 呼び出しの記録
		ct.otherTweet().AndReturn(u'Other')
		apiMock.update_status(u'Other')

		# 再現動作の開始
		self.mocker.ReplayAll()

		# 周期制御のハンドラ呼び出し
		ct.cycleHandler()

		# 実動作の検証
		self.mocker.VerifyAll()

	def test_AnniversaryHandler(self):
		# 周期ツイート制御のインスタンスを生成
		ct = CycleTweet(datetime.datetime(2012, 2, 13, 0, 30))

		# tweepyAPIのモックを作成
		apiMock = self.mocker.CreateMock(tweepy.API)

		# モックをテスト対象に設定
		ct.api = apiMock

		# 記録をリセット
		self.mocker.ResetAll()

		# 呼び出しの記録
		apiMock.update_status(u'ねころび『4周年』記念だぜ！ｲｲｲｲﾔｯﾎｵｵｵｩｩｩ！！！(1/12)')
		apiMock.update_status(u'ねころび『5周年』記念だぜ！ｲｲｲｲﾔｯﾎｵｵｵｩｩｩ！！！(6/12)')
		apiMock.update_status(u'ねころび『6周年』記念だぜ！ｲｲｲｲﾔｯﾎｵｵｵｩｩｩ！！！(12/12)')

		# 再現動作の開始
		self.mocker.ReplayAll()

		# 記念日制御のハンドラ呼び出し
		ct.ct = datetime.datetime(2012, 2, 13, 0, 30)
		ct.anniversaryHandler()

		# 記念日制御のハンドラ呼び出し
		ct.ct = datetime.datetime(2013, 2, 13, 10, 30)
		ct.anniversaryHandler()

		# 記念日制御のハンドラ呼び出し
		ct.ct = datetime.datetime(2014, 2, 13, 22, 30)
		ct.anniversaryHandler()

		# 実動作の検証
		self.mocker.VerifyAll()

	def test_TweetTest(self):
		# 周期ツイート制御のインスタンスを生成
		ct = CycleTweet(datetime.datetime(2012, 5, 6, 0, 0))

		# updateをモック
		self.mocker.StubOutWithMock(ct, "update")

		# 記録をリセット
		self.mocker.ResetAll()

		# 呼び出しの記録
		ct.update(u'test')

		# 再現動作の開始
		self.mocker.ReplayAll()

		# ツイート
		ct.tweet(u'test')

		# 実動作の検証
		self.mocker.VerifyAll()

		# 記録をリセット
		self.mocker.ResetAll()

		# 再現動作の開始
		self.mocker.ReplayAll()

		# 空文字はツイートしない
		ct.tweet(u'')

		# 実動作の検証
		self.mocker.VerifyAll()

	def test_MainHandler(self):

		# 周期ツイート制御のインスタンスを生成
		ct = CycleTweet(datetime.datetime(2012, 5, 6, 0, 0))

		# 各ハンドラをモックする
		self.mocker.StubOutWithMock(ct, "scheduleHandler")
		self.mocker.StubOutWithMock(ct, "cycleHandler")
		self.mocker.StubOutWithMock(ct, "anniversaryHandler")

		# 記録をリセット
		self.mocker.ResetAll()

		# 呼び出しの記録
		ct.scheduleHandler()
		ct.cycleHandler()
		ct.anniversaryHandler()

		# 再現動作の開始
		self.mocker.ReplayAll()

		# ツイート
		ct.handler()

		# 実動作の検証
		self.mocker.VerifyAll()


def main():
	pass

if __name__ == '__main__':
	main()

