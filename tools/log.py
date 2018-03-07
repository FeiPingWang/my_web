# import logging
# from logging.handlers import TimedRotatingFileHandler
# import re
#
# formatter = logging.Formatter('%(asctime)s  File "%(filename)s",line %(lineno)s %(levelname)s: %(message)s')
#
# # the old log file will move to my_web_2018_3_7 after day passed
# file_handler = TimedRotatingFileHandler(filename="./static/log/my_web.log", when='D', interval=1, backupCount=30)
# file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
# file_handler.suffix = "%Y-%m-%d_%H-%M.log"
# file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
# file_handler.setLevel(logging.INFO)
#
# logger = logging.getLogger("my_web")
# logger.addHandler(file_handler)


'''
TimedRotatingFileHandler会存在丢失log的情况，具体还要查询
'''
# import logging
#
#
# logger = logging.getLogger("my_web")
# formatter = logging.Formatter('%(asctime)s  File "%(filename)s",line %(lineno)s %(levelname)s: %(message)s')
# file_handler = logging.FileHandler("/static/log/my_web.log")
# file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
#
# logger.addHandler(file_handler)
# logger.setLevel(logging.INFO)


import logging
from logging.handlers import TimedRotatingFileHandler
import time


logger = logging.getLogger("my_web")
level = logging.INFO
format = '%(asctime)s  %(levelname)s  %(module)s.%(funcName)s  Line:%(lineno)d  %(message)s'
hdlr = TimedRotatingFileHandler(filename='./static/log/my_web.log', when="D", interval=1, backupCount=10)
fmt = logging.Formatter(format)
hdlr.setFormatter(fmt)
logger.addHandler(hdlr)
logger.setLevel(level)


if __name__ == '__main__':
    for i in range(1000):
        logger.info('test log, {}'.format(i))
        print('test log, {}'.format(i))
        time.sleep(1)