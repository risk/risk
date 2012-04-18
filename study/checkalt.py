# -*- coding:utf-8 -*-

import re
#from __future__ import with_statement

def checkAlt(strlines):

	r = re.compile('alt')
	for s in strlines:
		re_ser = r.search(s)
		if not re_ser:
			print s,


def main():
	with open('altdata.txt', 'r') as f:
		rl = f.readlines()
		checkAlt(rl)
	

if __name__ == '__main__':
	main()



