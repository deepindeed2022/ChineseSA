# -*- encoding: utf-8 -*-
import os.path
if os.path.exists('transchinese.txt.simple'):
	os.remove('transchinese.txt.simple')
if not os.path.isfile('transchinese.txt.simpletarget'):
	raise Exception('Please prepare the target file for test')