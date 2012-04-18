#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def randomChoice(lst):

	if len(lst) == 0:
		return None

	# リストからランダムに選択
	r = random.randint(0, len(lst)-1)
	return lst[r]

# 単体エントリ
def main():
	pass

if __name__ == '__main__':
	print main()

