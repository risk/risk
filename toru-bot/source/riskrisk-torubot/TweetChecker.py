#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

# 発言チェッカークラス
class TweetChecker():

	str = u''

	def __init__(self, str):
		self.str = str

	def isIyaho(self):
		r = re.compile(u'[いぃイｲィｨにニﾆあぁアァｱｧやヤﾔ]+[っッｯ]*[ほホﾎ]+.*[おぉオｵォｫうぅウｳゥｩ].*[！!]*')
		m = r.search(self.str)
		if m:
			return True
		else:
			return False

	def isUhyou(self):
		r = re.compile(u'[うぅウゥｳｩ]+[つっッｯ]*[ひヒﾋ]+[よょヨョﾖｮ]+.*[つっッｯほホﾎおぉオｵォｫうぅウｳゥｩ].*[！!]*')
		m = r.search(self.str)
		if m:
			return True
		else:
			return False


	def isPeropero(self):
		r = re.compile(u'[ぺペﾍ]ﾟ*[ろロﾛ][ぺペﾍ]ﾟ*[ろロﾛ]')
		m = r.search(self.str)
		if m:
			return True
		else:
			return False

	def isQuestion(self):
		r = re.compile(u'([ねネﾈ]|[だダ][ろロﾛ]|ﾀﾞ[ろロﾛ]|[すスｽ][かカｶ]|[なナﾅ])[？?！!]+')
		m = r.search(self.str)
		if m:
			return True
		else:
			return False

	def isDaijyoubuka(self):
		r = re.compile(u'(大丈夫か|だいじょうぶか|イーノック|いーのっく)[？?]')
		m = r.search(self.str)
		if m:
			return True
		else:
			return False

	def isOmikuji(self):
		r = re.compile(u'おみくじ|お御籤|御神籤|占って')
		m = r.search(self.str)
		if m:
			return True
		else:
			return False

	def isOmikujiAdd(self):
		r = re.compile(u'くじ追加')
		m = r.search(self.str)
		if m:
			return True
		else:
			return False

def main():
	pass

if __name__ == '__main__':
	main()

