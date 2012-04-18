#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import unittest

# 環境設定
# これをしないと GAE のモジュールをインポートできない。
# テスト対象のクラスも同様。
# GAE-SDKのインストールパス(下記は、全部nextインストール時)
GAE_HOME = 'C:\Program Files\Google\google_appengine'
# プロジェクトのHOMEパス(下記は、このスクリプトのおいてあるパス)
PROJECT_HOME = os.path.abspath(os.path.dirname(__file__))

# テストで使う GAE のモジュールのパスを作成
EXTRA_PATHS = [
    GAE_HOME,
    PROJECT_HOME,
    os.path.join(GAE_HOME, 'google', 'appengine', 'api'),
    os.path.join(GAE_HOME, 'google', 'appengine', 'ext'),
    os.path.join(GAE_HOME, 'lib', 'yaml', 'lib'),
    os.path.join(GAE_HOME, 'lib', 'webob'),
    os.path.join(GAE_HOME, 'lib', 'fancy_urllib'),
]

# パスを追加する。
for p in EXTRA_PATHS: sys.path.append(p)

from google.appengine.api import apiproxy_stub_map
from google.appengine.api import datastore_file_stub
from google.appengine.api import mail_stub
from google.appengine.api import urlfetch_stub
from google.appengine.api import user_service_stub
from google.appengine.ext import db, search

from google.appengine.api import users

APP_ID = u'test'
AUTH_DOMAIN = 'gmail.com'
LOGGED_IN_USER = 'test@example.com' 

# 初期化関数
def doSetup():

	# API Proxyを登録する
	apiproxy_stub_map.apiproxy = apiproxy_stub_map.APIProxyStubMap()

	# ダミーのDatastoreを登録する
	stub = datastore_file_stub.DatastoreFileStub(APP_ID,'/dev/null', '/dev/null')
	apiproxy_stub_map.apiproxy.RegisterStub('datastore_v3', stub)

	# APPLICATION_ID の設定
	# これを忘れると Datastore がエラーを出す
	os.environ["APPLICATION_ID"] = APP_ID

	# ダミーのユーザ認証用サービスを登録する
	apiproxy_stub_map.apiproxy.RegisterStub(
		'user', user_service_stub.UserServiceStub())
	os.environ['AUTH_DOMAIN'] = AUTH_DOMAIN
	os.environ['USER_EMAIL'] = LOGGED_IN_USER

	# ダミーのurlfetchを登録
	apiproxy_stub_map.apiproxy.RegisterStub(
		'urlfetch', urlfetch_stub.URLFetchServiceStub())

	# ダミーのメール送信サービスを登録
	apiproxy_stub_map.apiproxy.RegisterStub(
		'mail', mail_stub.MailServiceStub())

# 終了関数
def doTeardown():
	pass

# GAEテスト用ベースクラス
class BaseGAETest(unittest.TestCase):

	def setUp(self):
		doSetup()

	def tearDown(self):
		doTeardown()


