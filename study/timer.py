
# -*- coding:utf-8 -*-

import datetime

sec = 0
sTime = datetime.datetime.now()
while True:
	
	nTime = datetime.datetime.now()

	if nTime.second != sec:
		showTime = nTime - sTime
		print str(showTime)
		sec = nTime.second

