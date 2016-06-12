import os.path
import os
import logging
import sys


class DataLossError(Exception):
	pass


if __name__ == '__main__':
	program = os.path.basename(sys.argv[0])
	logger = logging.getLogger(program)
	logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')

	# create model dir
	if not os.path.isdir('../../model'):
		os.mkdir('../../model/')

	if not os.path.isdir('../../data'):
		raise DataLossError('data directory NOT found')