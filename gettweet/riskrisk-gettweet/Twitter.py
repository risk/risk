#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Env
Env.Custom.set()
import tweepy
from private.OAuth import OAuthInfo
import re

# TwitterAPI制御
class Twitter():

	# TwitterアクセスのAPI
	api = None

	# 通信制御の停止フラグ
	isEnable = True

	def __init__(self):
		self.api = None
		self.Enable = True

		self.auth()

	# Update不可設定
	def setDisable(self):
		self.isEnable = False

	# Update可能設定
	def setEnable(self):
		self.isEnable = True

	# 認証
	def auth(self):
		# create OAuth handler
		auth = tweepy.OAuthHandler(OAuthInfo.consumerKey, OAuthInfo.consumerSecret)

		# set access token to OAuth handler
		auth.set_access_token(OAuthInfo.accessToken, OAuthInfo.accessTokenSecret)

		# create API
		self.api = tweepy.API(auth_handler=auth)

	# Update
	def update(self, status, replyId=0):
		if self.isEnable:
			if replyId:
				self.api.update_status(status, replyId)
			else:
				self.api.update_status(status)

	# メンションの取得
	def getMentions(self):
		userTL = self.api.mentions()
		slist=[]
		for s in userTL:
			slist.append((s.id, s.user.screen_name, s.text))
		return slist

	# ユーザー別タイムラインの取得
	def getUserTL(self, user):
		userTL = self.api.user_timeline(id=user)
		slist=[]
		for s in userTL:
			slist.append((s.id, s.text))
		return slist

	# リフォロー機能
	def refollow(self):
		# 自分の情報を取得
		meid = self.api.me().id

		# 友達（フォロー）リストの取得
		friendLst = self.api.friends_ids(id=meid)

		# フォロワーリストの取得
		# 友達（フォロー）リストの取得
		followerLst = self.api.followers_ids(id=meid)

		#フォロワーのリストから、フォロー済みの人を外す
		for id in friendLst:
			if id in followerLst:
				followerLst.remove(id)

		# フォローしていない人をフォローする
		for id in followerLst:
			if not self.api.get_user(id=id).protected:
				self.api.create_friendship(id=id)

	# 検索
	def search(self, tag, page):
		
		results = self.api.search(tag, rpp=100, page=page)

		ret = []
		p = re.compile(u'RT.*')
		for result in results:
			rtCheck = p.match( result.text )
			if( not rtCheck ):
				ret.append((result.id,
					    result.from_user, result.id_str,
					    result.created_at))
		return ret

def main():
	pass

if __name__ == '__main__':
	main()
