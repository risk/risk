#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import nose
from nose.tools import *

from TweetChecker import *

class TestTweetChecker:

	def test_Iyaho(self):
		tc = TweetChecker(u'イィイイイヤッホォオオオオォオォォォォウ！！！！！')
		assert_true(tc.isIyaho())

		tc = TweetChecker(u'ニャアアアアホオオオオゥゥゥゥ！！！！')
		assert_true(tc.isIyaho())

		tc = TweetChecker(u'ｲﾔﾎｩ!')
		assert_true(tc.isIyaho())

	def test_NotIyaho(self):
		tc = TweetChecker(u'ﾌﾞﾎﾎﾌｷﾞｨ!!')
		assert_false(tc.isIyaho())

	def test_Uhyou(self):
		tc = TweetChecker(u'ウッヒョォオオオォオォォォウ！！！')
		assert_true(tc.isUhyou())

		tc = TweetChecker(u'ｳｯﾋｮｵｵｵｵｫｫｩ!！！！！')
		assert_true(tc.isUhyou())

	def test_NotUhyou(self):
		tc = TweetChecker(u'ﾌﾞﾎﾎﾌｷﾞｨ!!')
		assert_false(tc.isUhyou())

	def test_Peropero(self):
		tc = TweetChecker(u'ペロペロ')
		assert_true(tc.isPeropero())

		tc = TweetChecker(u'ﾍﾟﾛﾍﾟﾛ')
		assert_true(tc.isPeropero())

		tc = TweetChecker(u'ペロペロ')
		assert_true(tc.isPeropero())

		tc = TweetChecker(u'ﾍﾟﾛペロ')
		assert_true(tc.isPeropero())

		tc = TweetChecker(u'これにﾍﾟﾛﾍﾟﾛ機能つける')
		assert_true(tc.isPeropero())

	def test_NotPeropero(self):

		tc = TweetChecker(u'ﾚﾛﾚﾛ')
		assert_false(tc.isPeropero())

		tc = TweetChecker(u'ぺ')
		assert_false(tc.isPeropero())

		tc = TweetChecker(u'ﾌﾞﾎﾎﾌｷﾞｨ!!')
		assert_false(tc.isPeropero())

	def test_Question(self):
		tc = TweetChecker(u'だろ？')
		assert_true(tc.isQuestion())

		tc = TweetChecker(u'そう思うよね？')
		assert_true(tc.isQuestion())

		tc = TweetChecker(u'美味しいんだろ？')
		assert_true(tc.isQuestion())

		tc = TweetChecker(u'BLなんですか？')
		assert_true(tc.isQuestion())

		tc = TweetChecker(u'ﾛﾎﾞｯﾄﾅﾝﾀﾞﾛ?')
		assert_true(tc.isQuestion())

		tc = TweetChecker(u'ﾈ? ｿｳﾀﾞﾖﾈ?')
		assert_true(tc.isQuestion())

		tc = TweetChecker(u'だろ！')
		assert_true(tc.isQuestion())

		tc = TweetChecker(u'な！')
		assert_true(tc.isQuestion())

		tc = TweetChecker(u'ﾀﾞﾛ!')
		assert_true(tc.isQuestion())

		tc = TweetChecker(u'大丈夫ですか？')
		assert_true(tc.isQuestion())

	def test_NotQuestion(self):
		tc = TweetChecker(u'そうにきまてる')
		assert_false(tc.isQuestion())

		tc = TweetChecker(u'そんなきがしてた')
		assert_false(tc.isQuestion())

		tc = TweetChecker(u'君はBLなのかな')
		assert_false(tc.isQuestion())

		tc = TweetChecker(u'そんな装備で大丈夫か？')
		assert_false(tc.isQuestion())

	def test_Daijyoubuka(self):

		tc = TweetChecker(u'そんな装備で大丈夫か？')
		assert_true(tc.isDaijyoubuka())

		tc = TweetChecker(u'あたま大丈夫か？')
		assert_true(tc.isDaijyoubuka())

		tc = TweetChecker(u'大丈夫か？ほんとに')
		assert_true(tc.isDaijyoubuka())

		tc = TweetChecker(u'それで大丈夫か？まじで？')
		assert_true(tc.isDaijyoubuka())

		tc = TweetChecker(u'そんな装備で、イーノック？')
		assert_true(tc.isDaijyoubuka())

		tc = TweetChecker(u'そんな装備で、いーのっく？')
		assert_true(tc.isDaijyoubuka())

	def test_Omikuji(self):

		tc = TweetChecker(u'おみくじくれ')
		assert_true(tc.isOmikuji())

		tc = TweetChecker(u'御神籤ください')
		assert_true(tc.isOmikuji())

		tc = TweetChecker(u'おねがい、お御籤ちょうだい')
		assert_true(tc.isOmikuji())

		tc = TweetChecker(u'僕のこと占って！')
		assert_true(tc.isOmikuji())

	def test_Omikuji(self):

		tc = TweetChecker(u'くじ追加')
		assert_true(tc.isOmikujiAdd())

		tc = TweetChecker(u'このくじ追加して')
		assert_true(tc.isOmikujiAdd())

def main():
	pass

if __name__ == '__main__':
	main()

