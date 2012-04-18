#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import nose
from nose.tools import *
import mox

import BaseGAETest

from UserControl import *

import Env
Env.Custom.set()

import tweepy

class TestUserControl(BaseGAETest.BaseGAETest):

	mocker = mox.Mox()

	# リフォローを行う
	def test_Refollow(self):
		# 周期ツイート制御のインスタンスを生成
		uc = UserControl()

		# 各ハンドラをモックする
		self.mocker.StubOutWithMock(uc, "refollow")

		# 記録をリセット
		self.mocker.ResetAll()

		# 呼び出しの記録
		uc.refollow()

		# 再現動作の開始
		self.mocker.ReplayAll()

		# ツイート
		uc.refollowHandler()

		# 実動作の検証
		self.mocker.VerifyAll()

	# メインのハンドラ
	def test_Handler(self):

		# 周期ツイート制御のインスタンスを生成
		uc = UserControl()

		# 各ハンドラをモックする
		self.mocker.StubOutWithMock(uc, "refollowHandler")

		# 記録をリセット
		self.mocker.ResetAll()

		# 呼び出しの記録
		uc.refollowHandler()

		# 再現動作の開始
		self.mocker.ReplayAll()

		# ツイート
		uc.handler()

		# 実動作の検証
		self.mocker.VerifyAll()


def main():
	pass

if __name__ == '__main__':
	main()

