# __author:  Administrator
# __date:  2018/8/9/009

import sys
import hashlib
import time
import logging

# ms = hashlib.md5()
# print(hashlib)
# print(time.gmtime())

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a %d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='w')
#
# logging.error('err message')
# logging.warning('warnmessage')
# logging.debug('debug 1111')
# logging.info('info message')
# logging.critical('cri message')
# logging.debug('debug 1111')

logger = logging.getLogger()
# 创建一个handler，用于写入日志文件
th = logging.FileHandler('test1.log')
# 用于输出到控制台的handler
ch = logging.StreamHandler()
fmt = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s - %(message)s')
th.setFormatter(fmt)
ch.setFormatter(fmt)


logger.addHandler(th)
logger.addHandler(ch)
logger.info('info msg')
logger.debug('debug msg')
logger.warning('warning msg')
