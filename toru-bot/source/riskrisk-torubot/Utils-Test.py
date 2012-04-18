#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import nose
from nose.tools import *

import Utils

class TestUtils:

	def test_RandomChoice(self):
		s = Utils.randomChoice([u'test'])
		assert_equal(u'test', s)

	def test_RandomChoiceMultipleNo(self):
		no = Utils.randomChoice([1, 2, 3, 4, 5])
		assert_true(no)

	def test_RandomChoiceCount0(self):

		s = Utils.randomChoice([])
		assert_false(s)

def main():
	pass

if __name__ == '__main__':
	main()

