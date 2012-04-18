#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import Env
Env.Custom.set()

import nose
from nose.tools import *
import mox
import BaseGAETest

from Twitter import *
import tweepy
import DataStore

class TestTweetChecker(BaseGAETest.BaseGAETest):

	# mox���쐬
	mocker = mox.Mox()

	def setUp(self):
		BaseGAETest.BaseGAETest.setUp(self)

		# �c�C�[�g�\�ɐݒ�
		ds = DataStore.DataStore()
		ds.setTweetEnable(True)

	def test_MakeApi(self):
		twitter = Twitter()
		assert_true(twitter.api)

	def test_TweetEnableDisable(self):

		# Twitter����N���X�̍쐬
		twitter = Twitter()

		assert_true(twitter.isEnable)
		twitter.setDisable()
		assert_false(twitter.isEnable)
		twitter.setEnable()
		assert_true(twitter.isEnable)

	def test_TweetControl(self):

		# API�̃��b�N���쐬
		apiMock = self.mocker.CreateMock(tweepy.API)

		# Twitter����N���X�̍쐬
		twitter = Twitter()

		# ���b�N�̃C���^�t�F�[�X��ݒ�
		twitter.api = apiMock

		# Enable���
		twitter.setEnable()

		# ����L�^�����Z�b�g
		self.mocker.ResetAll()

		# [����L�^]�X�e�[�^�X�̃A�b�v�f�[�g
		apiMock.update_status(u'test')

		# ���쌟�؂̊J�n
		self.mocker.ReplayAll()

		twitter.update(u'test')

		# ������̊m�F(�������Ȃ��ƃG���[���o���)
		self.mocker.VerifyAll()

		# Disable���
		twitter.setDisable()

		# ����L�^�����Z�b�g
		self.mocker.ResetAll()

		# ���쌟�؂̊J�n
		self.mocker.ReplayAll()

		twitter.update(u'test')

		# ������̊m�F(�������Ȃ��ƃG���[���o���)
		self.mocker.VerifyAll()

	def test_GetMention(self):
		# ���b�N�̃C���^�t�F�[�X���쐬
		apiMock = self.mocker.CreateMock(tweepy.API)

		# ���b�N�̖߂�l�N���X���쐬
		userMock = self.mocker.CreateMock(tweepy.models.User)
		userMock.screen_name = u'testuser'
		statusMock = self.mocker.CreateMock(tweepy.models.Status)
		statusMock.id=100
		statusMock.text=u'test status'
		statusMock.user=userMock

		# Twitter�N���X���쐬
		twitter = Twitter()

		# �ΏۃN���X��Mock�C���^�t�F�[�X�̐ݒ�
		twitter.api = apiMock

		# ����L�^�����Z�b�g
		self.mocker.ResetAll()

		# ����̋L�^
		apiMock.mentions().AndReturn([statusMock])

		# ���쌟�؂̊J�n
		self.mocker.ReplayAll()

		lst = twitter.getMentions()

		# ������̊m�F(�������Ȃ��ƃG���[���o���)
		self.mocker.VerifyAll()

		# �߂�l��1���ł��邱��
		assert_equal(1, len(lst))

		# �������f�[�^���擾�ł��邱��
		assert_equal(100, lst[0][0])
		assert_equal(u'testuser', lst[0][1])
		assert_equal(u'test status', lst[0][2])

	def test_GetMentions(self):
		# ���b�N�̃C���^�t�F�[�X���쐬
		apiMock = self.mocker.CreateMock(tweepy.API)

		# ���b�N�̖߂�l�N���X���쐬1
		userMock1 = self.mocker.CreateMock(tweepy.models.User)
		userMock1.screen_name = u'testuser1'
		statusMock1 = self.mocker.CreateMock(tweepy.models.Status)
		statusMock1.id=100
		statusMock1.text=u'test1 status'
		statusMock1.user=userMock1

		# ���b�N�̖߂�l�N���X���쐬2
		userMock2 = self.mocker.CreateMock(tweepy.models.User)
		userMock2.screen_name = u'testuser2'
		statusMock2 = self.mocker.CreateMock(tweepy.models.Status)
		statusMock2.id=200
		statusMock2.text=u'test2 status'
		statusMock2.user=userMock2

		# Twitter�N���X���쐬
		twitter = Twitter()

		# �ΏۃN���X��Mock�C���^�t�F�[�X�̐ݒ�
		twitter.api = apiMock

		# ����L�^�����Z�b�g
		self.mocker.ResetAll()

		# ����̋L�^
		apiMock.mentions().AndReturn([statusMock1, statusMock2])

		# ���쌟�؂̊J�n
		self.mocker.ReplayAll()

		lst = twitter.getMentions()

		# ������̊m�F(�������Ȃ��ƃG���[���o���)
		self.mocker.VerifyAll()

		# �߂�l��2���ł��邱��
		assert_equal(2, len(lst))

		# �������f�[�^���擾�ł��邱��
		assert_equal(100, lst[0][0])
		assert_equal(u'testuser1', lst[0][1])
		assert_equal(u'test1 status', lst[0][2])

		assert_equal(200, lst[1][0])
		assert_equal(u'testuser2', lst[1][1])
		assert_equal(u'test2 status', lst[1][2])

	def test_GetUserTimeline(self):
		# ���b�N�̃C���^�t�F�[�X���쐬
		apiMock = self.mocker.CreateMock(tweepy.API)

		# ���b�N�̖߂�l�N���X���쐬
		statusMock = self.mocker.CreateMock(tweepy.models.Status)
		statusMock.id=100
		statusMock.text=u'test status'

		# Twitter�N���X���쐬
		twitter = Twitter()

		# �ΏۃN���X��Mock�C���^�t�F�[�X�̐ݒ�
		twitter.api = apiMock

		# ����L�^�����Z�b�g
		self.mocker.ResetAll()

		# ����̋L�^
		apiMock.user_timeline(id=u'test').AndReturn([statusMock])

		# ���쌟�؂̊J�n
		self.mocker.ReplayAll()

		lst = twitter.getUserTL(u'test')

		# ������̊m�F(�������Ȃ��ƃG���[���o���)
		self.mocker.VerifyAll()

		# �߂�l��1���ł��邱��
		assert_equal(1, len(lst))

		# �������f�[�^���擾�ł��邱��
		assert_equal(100, lst[0][0])
		assert_equal(u'test status', lst[0][1])

	def test_GetUserTimelines(self):
		# ���b�N�̃C���^�t�F�[�X���쐬
		apiMock = self.mocker.CreateMock(tweepy.API)

		# ���b�N�̖߂�l�N���X���쐬
		statusMock1 = self.mocker.CreateMock(tweepy.models.Status)
		statusMock1.id=100
		statusMock1.text=u'test1 status'

		# ���b�N�̖߂�l�N���X���쐬
		statusMock2 = self.mocker.CreateMock(tweepy.models.Status)
		statusMock2.id=200
		statusMock2.text=u'test2 status'

		# Twitter�N���X���쐬
		twitter = Twitter()

		# �ΏۃN���X��Mock�C���^�t�F�[�X�̐ݒ�
		twitter.api = apiMock

		# ����L�^�����Z�b�g
		self.mocker.ResetAll()

		# ����̋L�^
		apiMock.user_timeline(id=u'test').AndReturn([statusMock1, statusMock2])

		# ���쌟�؂̊J�n
		self.mocker.ReplayAll()

		lst = twitter.getUserTL(u'test')

		# ������̊m�F(�������Ȃ��ƃG���[���o���)
		self.mocker.VerifyAll()

		# �߂�l��2���ł��邱��
		assert_equal(2, len(lst))

		# �������f�[�^���擾�ł��邱��
		assert_equal(100, lst[0][0])
		assert_equal(u'test1 status', lst[0][1])

		assert_equal(200, lst[1][0])
		assert_equal(u'test2 status', lst[1][1])

	def test_Update(self):
		# ���b�N�̃C���^�t�F�[�X���쐬
		apiMock = self.mocker.CreateMock(tweepy.API)

		# Twitter�N���X���쐬
		twitter = Twitter()

		# �ΏۃN���X��Mock�C���^�t�F�[�X�̐ݒ�
		twitter.api = apiMock

		# ����L�^�����Z�b�g
		self.mocker.ResetAll()

		# ����̋L�^
		apiMock.update_status('test')

		# ����L�^
		self.mocker.ReplayAll()

		twitter.update("test");

		# ������̊m�F(�������Ȃ��ƃG���[���o���)
		self.mocker.VerifyAll()

	def test_UpdateDisableProperty(self):
		# ���b�N�̃C���^�t�F�[�X���쐬
		apiMock = self.mocker.CreateMock(tweepy.API)

		# Twitter�N���X���쐬
		twitter = Twitter()

		# �ΏۃN���X��Mock�C���^�t�F�[�X�̐ݒ�
		twitter.api = apiMock

		# �c�C�[�g�s�ɐݒ�
		twitter.setDisable()

		# ����L�^�����Z�b�g
		self.mocker.ResetAll()

		# ����L�^
		self.mocker.ReplayAll()

		twitter.update("test");

		# ������̊m�F(�������Ȃ��ƃG���[���o���)
		self.mocker.VerifyAll()

	def test_UpdateDisableDataStore(self):
		# ���b�N�̃C���^�t�F�[�X���쐬
		apiMock = self.mocker.CreateMock(tweepy.API)

		# Twitter�N���X���쐬
		twitter = Twitter()

		# �ΏۃN���X��Mock�C���^�t�F�[�X�̐ݒ�
		twitter.api = apiMock

		# �c�C�[�g�s�ɐݒ�
		ds = DataStore.DataStore()
		ds.setTweetEnable(False)

		# ����L�^�����Z�b�g
		self.mocker.ResetAll()

		# ����L�^
		self.mocker.ReplayAll()

		twitter.update("test");

		# ������̊m�F(�������Ȃ��ƃG���[���o���)
		self.mocker.VerifyAll()

	def test_UpdateReply(self):
		# ���b�N�̃C���^�t�F�[�X���쐬
		apiMock = self.mocker.CreateMock(tweepy.API)

		# Twitter�N���X���쐬
		twitter = Twitter()

		# �ΏۃN���X��Mock�C���^�t�F�[�X�̐ݒ�
		twitter.api = apiMock

		# ����L�^�����Z�b�g
		self.mocker.ResetAll()

		# ����̋L�^
		apiMock.update_status('test', 12345)

		# ���쌟�؂̊J�n
		self.mocker.ReplayAll()

		twitter.update('test', 12345);

		# ������̊m�F(�������Ȃ��ƃG���[���o���)
		self.mocker.VerifyAll()

	def test_Refollow(self):

		# ���b�N�̃C���^�t�F�[�X���쐬
		apiMock = self.mocker.CreateMock(tweepy.API)

		# ���[�U�[�̃��b�N���쐬
		userMock = self.mocker.CreateMock(tweepy.models.User)
		userMock.id = 10

		userLockMock = self.mocker.CreateMock(tweepy.models.User)
		userLockMock.id =400
		userLockMock.protected = True

		userUnlockMock = self.mocker.CreateMock(tweepy.models.User)
		userUnlockMock.id = 500
		userUnlockMock.protected = False

		# Twitter�N���X���쐬
		twitter = Twitter()

		# �ΏۃN���X��Mock�C���^�t�F�[�X�̐ݒ�
		twitter.api = apiMock

		# ����L�^�����Z�b�g
		self.mocker.ResetAll()

		# ����̋L�^
		apiMock.me().AndReturn(userMock)
		apiMock.friends_ids(id=10).AndReturn([100, 200, 300, 1000])
		apiMock.followers_ids(id=10).AndReturn([200, 300, 400, 500])


		apiMock.get_user(id=400).AndReturn(userLockMock)
		apiMock.get_user(id=500).AndReturn(userUnlockMock)
		apiMock.create_friendship(id=500)

		# ���쌟�؂̊J�n
		self.mocker.ReplayAll()

		# ���t�H���[�@�\
		twitter.refollow();

		# ������̊m�F(�������Ȃ��ƃG���[���o���)
		self.mocker.VerifyAll()



def main():
	pass

if __name__ == '__main__':
	main()

