import logging
logger = logging.getLogger('test')  # 创建日志器对象
# logging.basicConfig() #不用basicConfig 需要手动添加handler
logger.setLevel(logging.DEBUG)  # 输出所有大于DEBUG级别的log
# 设置日志输出格式：格式器
fmt = logging.Formatter('[%(filename)-6s]: [%(levelname)-6s] [%(asctime)s]: %(message)s')
# console打印,级别为warning
stream_hdl = logging.StreamHandler()  # 处理器
stream_hdl.setFormatter(fmt)
stream_hdl.setLevel(logging.DEBUG)
logger.addHandler(stream_hdl)

if __name__ == "__main__":
    for i in range(1):
        logger.debug("This is debug information")
        logger.info("This is info information")
        logger.error("This is error information")
