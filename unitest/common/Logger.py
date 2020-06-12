import logging
import os

# log配置
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #工程目录
log_path = root_path + "./log/" + "log.txt"   # 日志输出目录
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_path,  # 日志输出文件
                    filemode='a+')  # 追加模式

if __name__ == '__main__':
    logging.info("hello")
    print(log_path)
