#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import nose
from nose.tools import *

from GCalendar import *

class TestGCalendar():

	def test_getInfo(self):
		gcal = GCalendar('.\gcaltest.xml')
		assert_equal(
			u'◎ねころびお休み◎',
			gcal.getDateInfo(datetime.date(2010, 12, 31)))
		assert_equal(
			u'通常営業時間　11時から２１時',
			gcal.getDateInfo(datetime.date(2011, 1, 21)))
		assert_equal(
			u'１９時よりモンハンオフ予定',
			gcal.getDateInfo(datetime.date(2011, 2, 27)))

	def test_doubleSchedule(self):
		gcal = GCalendar('.\gcaltest.xml')
		assert_equal(
			u'１９時よりモンハンオフ予定 / 通常営業時間　13時から23時',
			gcal.getDateInfo(datetime.date(2011, 2, 1)))

	def test_NoSchedule(self):
		gcal = GCalendar('.\gcaltest.xml')
		assert_equal(
			u'',
			gcal.getDateInfo(datetime.date(2011, 1, 5)))

def main():
	pass

if __name__ == '__main__':
	main()

