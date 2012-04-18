#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import nose
from nose.tools import *

import datetime

from Timezone import *

class TestTimezone():

	def test_UtcName(self):
		utc = UTC()
		assert_equal('UTC', utc.tzname(None))

	def test_UtcOffset(self):
		utc = UTC()
		assert_equal(datetime.timedelta(hours=0), utc.utcoffset(None))

	def test_JstName(self):
		jst = JST()
		assert_equal('JST', jst.tzname(None))

	def test_JstOffset(self):
		jst = JST()
		assert_equal(datetime.timedelta(hours=9), jst.utcoffset(None))

def main():
	pass

if __name__ == '__main__':
	main()

