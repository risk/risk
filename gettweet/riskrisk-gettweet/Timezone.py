#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

# タイムゾーンUTC
class UTC(datetime.tzinfo):
	def utcoffset(self, dt):
		return datetime.timedelta(0)
	def tzname(self, dt):
		return 'UTC'
	def dst(self, dt):
		return datetime.timedelta(0)

# タイムゾーンJST
class JST(datetime.tzinfo):
	def utcoffset(self,dt):
		return datetime.timedelta(hours=9)
	def dst(self,dt):
		return datetime.timedelta(0)
	def tzname(self,dt):
		return 'JST'

def main():
	pass

if __name__ == '__main__':
	main()

