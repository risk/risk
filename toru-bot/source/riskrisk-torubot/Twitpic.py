#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import datetime
from xml.etree.ElementTree import *

import Timezone
import Bitly

class Twitpic():

	username = u''

	tree = None
	rootElem = None

	twitpic = u'http://twitpic.com/'
	twitpicUsersShow = u'http://api.twitpic.com/2/users/show.xml'

	def __init__(self, name):
		self.username = name

	def xmlOpen(self, page=1):
		site = urllib.urlopen(u''.join([self.twitpicUsersShow,u'?',u'username=',self.username,u'&',u'page=',str(page)]))

		# XMLのパース
		self.tree  = parse(site)
		self.rootElem = self.tree.getroot()

	def getUserPicList(self, now):

		# XMLを開く
		self.xmlOpen()

		# 戻り値
		rtnList = []

		# イメージのURLを取得する
		images = self.rootElem.find(u'./images')
		if images:
			# イメージ一覧を取得
			imgList = images.findall(u'./image')

			if imgList:

				# 基準を前日の23時に以降に設定する
				checkDate = now - datetime.timedelta(days=1)
				checkDate = checkDate.replace(hour=23, minute=0, second=0, microsecond=0)

				done = False

				for i in range(1, 20):
					for elem in imgList:

						timeStamp = datetime.datetime.strptime( \
							elem.find(u'./timestamp').text,'%Y-%m-%d %H:%M:%S')

						timeStamp = timeStamp.replace(tzinfo=Timezone.UTC()).astimezone(Timezone.JST())
						# 基準範囲をチェック
						if(timeStamp < checkDate):
							# 取得範囲外になった場合は、終了
							done = True
							break

						# リストに追加
						#b = Bitly.Bitly(u''.join([self.twitpic, elem.find(u'./short_id').text]))
						rtnList.append(u''.join([self.twitpic, elem.find(u'./short_id').text]))
					if done:
						break

					# 次のページを開く
					self.xmlOpen(page=i)

		return rtnList

def main():
	tp = Twitpic(u'catcafenekorobi')
	tp.xmlOpen()
	lst = tp.getUserPicList(datetime.datetime.now(Timezone.JST()))
	for s in lst:
		print s
	pass

if __name__ == '__main__':
	main()


