#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import nose
from nose.tools import *

from BaseGAETest import *

from DataStore import *

class TestDataStore(BaseGAETest):

	def test_MentionId(self):
		ds = DataStore()
		ds.setMentionId(100)

		# 登録したMentionIdが取得できること
		assert_equal(100, ds.getMentionId())

	def test_tweetEnable(self):
		ds = DataStore()

		ds.setTweetEnable(True)

		assert_equal(True, ds.getTweetEnable())

		ds.setTweetEnable(False)

		assert_equal(False, ds.getTweetEnable())

	def test_DeleteSettings(self):
		ds = DataStore()
		ds.setMentionId(100)

		ds.deleteSettings()

		# MentionIdがクリア値(0)に戻ること
		assert_equal(0, ds.getMentionId())

	def test_AddStatus(self):
		ds = DataStore()
		ds.addStatus(Type.normal, u'abc')

		lst = ds.getStatuses(Type.normal)
		detect = False
		for s in lst:
			if s[1] == u'abc':
				detect = True

		# ステータスが登録されること
		assert_true(detect)

	def test_DeleteStatus(self):
		ds = DataStore()
		ds.addStatus(Type.normal, u'abc')
		ds.removeStatus(Type.normal, u'abc')

		lst = ds.getStatuses(Type.normal)
		detect = False
		for s in lst:
			if s[1] == u'abc':
				detect = True

		# 登録したステータスが削除されること
		assert_false(detect)

	def test_DeleteAllStatus(self):
		ds = DataStore()
		ds.addStatus(Type.normal, u'abc')
		ds.addStatus(Type.normal, u'def')
		ds.addStatus(Type.normal, u'ghi')
		ds.addStatus(Type.priority, u'abc')
		ds.addStatus(Type.priority, u'def')
		ds.addStatus(Type.priority, u'ghi')

		ds.removeStatuses()

		# リストが0件であること
		lst = ds.getStatuses()
		assert_equal(0, len(lst))

	def test_setPrioStatus(self):
		ds = DataStore()
		ds.addStatus(Type.priority, u'prioAbc')

		lst = ds.getStatuses(Type.priority)
		detect = False
		for s in lst:
			if s[1] == u'prioAbc':
				detect = True

		# 優先ステータスが登録されること
		assert_true(detect)

	def test_getPrioStatus(self):
		ds = DataStore()
		ds.addStatus(Type.priority, u'prioAbc')

		# 優先ステータスが取得できること
		assert_equal(u'prioAbc', ds.popStatus(Type.priority)[1])
		# 取得でステータスが削除されること
		assert_false(ds.popStatus(Type.priority))

	def test_AddStatusSelectType(self):

		ds = DataStore()

		ds.addStatus(Type.normal, u'status1')
		ds.addStatus(Type.normal, u'status2')
		ds.addStatus(Type.normal, u'status3')

		ds.addStatus(Type.priority, u'priority1')
		ds.addStatus(Type.priority, u'priority2')
		ds.addStatus(Type.priority, u'priority3')

		ds.addStatus(Type.omikuji, u'omikuji1')
		ds.addStatus(Type.omikuji, u'omikuji2')
		ds.addStatus(Type.omikuji, u'omikuji3')

		normallst = ds.getStatuses(Type.normal)
		assert_true((Type.normal==normallst[0][0] and normallst[0][1]==u'status1'))
		assert_true((Type.normal==normallst[1][0] and normallst[1][1]==u'status2'))
		assert_true((Type.normal==normallst[2][0] and normallst[2][1]==u'status3'))

		prioritylst = ds.getStatuses(Type.priority)
		assert_true((Type.priority==prioritylst[0][0] and prioritylst[0][1]==u'priority1'))
		assert_true((Type.priority==prioritylst[1][0] and prioritylst[1][1]==u'priority2'))
		assert_true((Type.priority==prioritylst[2][0] and prioritylst[2][1]==u'priority3'))

		omikujilst = ds.getStatuses(Type.omikuji)
		assert_true((Type.omikuji==omikujilst[0][0] and omikujilst[0][1]==u'omikuji1'))
		assert_true((Type.omikuji==omikujilst[1][0] and omikujilst[1][1]==u'omikuji2'))
		assert_true((Type.omikuji==omikujilst[2][0] and omikujilst[2][1]==u'omikuji3'))

	def test_removeStatuses(self):
		ds = DataStore()

		ds.addStatus(Type.normal, u'status1')
		ds.addStatus(Type.normal, u'status2')
		ds.addStatus(Type.normal, u'status3')

		ds.addStatus(Type.priority, u'priority1')
		ds.addStatus(Type.priority, u'priority2')
		ds.addStatus(Type.priority, u'priority3')

		ds.addStatus(Type.omikuji, u'omikuji1')
		ds.addStatus(Type.omikuji, u'omikuji2')
		ds.addStatus(Type.omikuji, u'omikuji3')

		ds.removeStatuses()

		normallst = ds.getStatuses(Type.normal)
		assert_equal(0, len(normallst))

		prioritylst = ds.getStatuses(Type.priority)
		assert_equal(0, len(prioritylst))

		omikujilst = ds.getStatuses(Type.omikuji)
		assert_equal(0, len(omikujilst))

	def test_removeStatusesSelectType(self):
		ds = DataStore()

		ds.addStatus(Type.normal, u'status1')
		ds.addStatus(Type.normal, u'status2')
		ds.addStatus(Type.normal, u'status3')

		ds.addStatus(Type.priority, u'priority1')
		ds.addStatus(Type.priority, u'priority2')
		ds.addStatus(Type.priority, u'priority3')

		ds.addStatus(Type.omikuji, u'omikuji1')
		ds.addStatus(Type.omikuji, u'omikuji2')
		ds.addStatus(Type.omikuji, u'omikuji3')

		ds.removeStatuses(Type.normal)

		normallst = ds.getStatuses(Type.normal)
		assert_equal(0, len(normallst))

		prioritylst = ds.getStatuses(Type.priority)
		assert_true((Type.priority==prioritylst[0][0] and prioritylst[0][1]==u'priority1'))
		assert_true((Type.priority==prioritylst[1][0] and prioritylst[1][1]==u'priority2'))
		assert_true((Type.priority==prioritylst[2][0] and prioritylst[2][1]==u'priority3'))

		omikujilst = ds.getStatuses(Type.omikuji)
		assert_true((Type.omikuji==omikujilst[0][0] and omikujilst[0][1]==u'omikuji1'))
		assert_true((Type.omikuji==omikujilst[1][0] and omikujilst[1][1]==u'omikuji2'))
		assert_true((Type.omikuji==omikujilst[2][0] and omikujilst[2][1]==u'omikuji3'))


	def test_TweetCountup(self):
		ds = DataStore()

		ds.addStatus(Type.normal, u'status1')


		ds.tweetCountup(Type.normal, u'status1')
		normallst = ds.getStatuses(Type.normal)
		assert_true((normallst[0][1]==u'status1' and normallst[0][3]==1))

		ds.tweetCountup(Type.normal, u'status1')
		normallst = ds.getStatuses(Type.normal)
		assert_true((normallst[0][1]==u'status1' and normallst[0][3]==2))

	def test_TweetCountup(self):
		ds = DataStore()

		ds.addStatus(Type.normal, u'status1')
		ds.addStatus(Type.normal, u'status2')
		ds.addStatus(Type.normal, u'status3')


		for i in range(0,5):
			ds.tweetCountup(Type.normal, u'status1')
		for i in range(0,4):
			ds.tweetCountup(Type.normal, u'status2')
		for i in range(0,3):
			ds.tweetCountup(Type.normal, u'status3')

		normallst = ds.getStatuses(Type.normal)
		assert_true((normallst[0][1]==u'status1' and normallst[0][3]==5))
		assert_true((normallst[1][1]==u'status2' and normallst[1][3]==4))
		assert_true((normallst[2][1]==u'status3' and normallst[2][3]==3))

		ds.tweetCountAdjust(Type.normal)

		normallst = ds.getStatuses(Type.normal)
		assert_true((normallst[0][1]==u'status1' and normallst[0][3]==2))
		assert_true((normallst[1][1]==u'status2' and normallst[1][3]==1))
		assert_true((normallst[2][1]==u'status3' and normallst[2][3]==0))

		ds.tweetCountAdjust(Type.normal)

		normallst = ds.getStatuses(Type.normal)
		assert_true((normallst[0][1]==u'status1' and normallst[0][3]==2))
		assert_true((normallst[1][1]==u'status2' and normallst[1][3]==1))
		assert_true((normallst[2][1]==u'status3' and normallst[2][3]==0))


def main():
	pass

if __name__ == '__main__':
	main()

