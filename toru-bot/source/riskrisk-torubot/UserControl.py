#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Env
Env.Custom.set()
import Twitter


# ユーザー制御
class UserControl(Twitter.Twitter):

	# 出力HTMLの格納
	html = []

	# 初期化
	def __init__(self):
		Twitter.Twitter.__init__(self)
		self.html = []

		# クラス名
		self.html.append(u'<hr size="10" noshade>')
		self.html.append(u'<b>User Control</b><br/>')


	# リフォロー制御
	def refollowHandler(self):

		# リフォローを実行する
		self.refollow()

	# メインのハンドラ
	def handler(self):
		self.html.append(u'<b>UserControl handler start</b><br/>')

		# Mentionからの返信
		self.refollowHandler()

		self.html.append(u'<b>UserControl handler end</b><br/>')

# 単体エントリ
def main():
	pass

if __name__ == '__main__':
	print main()

