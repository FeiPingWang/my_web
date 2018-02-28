import logging


logger = logging.getLogger("my_web")
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
file_handler = logging.FileHandler("my_web.log")
file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

