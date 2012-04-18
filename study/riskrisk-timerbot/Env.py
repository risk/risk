#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

class Custom:

	@staticmethod
	def set():
		for arch in os.listdir('eggs'):
			sys.path.insert(0, os.path.join('eggs', arch))
