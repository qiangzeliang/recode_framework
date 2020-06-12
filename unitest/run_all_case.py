import unittest
from HTMLTestReportCN import HTMLTestRunner
import time
from unitest.common.Logger import *
from unitest.common.send_email import *
from tomorrow import threads
current_path = os.getcwd()  #设置当前路径
import unittest
import os
from unitest.readConfig import *
semail = ReadConfig()

#加载用例

def Run_all_test():

    # 实例化覆盖对象，匹配test*.py的文件
    case_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))  # 获取当前工作目录（用例也放在该目录下）
    discover = unittest.defaultTestLoader.discover(case_dir, "test*.py", top_level_dir=None)

    return discover  # 返回实例化对象（用例集）


def start():

    logging.info("================================== 测试开始 ==================================")
    #runner = unittest.TextTestRunner()  # 实例化运行类
    #runner.run(Run_all_test())  # 执行所有的匹配用例集

    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())

    filename = "./report/" + now + "_api_report.html"

    with open(filename, 'wb+') as f:
        runner = HTMLTestRunner(stream=f,
                                title='测试报告',
                                description='接口测试.',
                                verbosity=2,
                                )

        runner.run(Run_all_test())
        f.close()

        logging.info("================================== 测试结束 ==================================")

    # 发送邮件
    if int(semail.get_email("on_off")) == 1:
        # Report配置
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 工程目录
        report_path = root_path + "\\unitest\\Report\\" + now + "_api_report.html"  # report输出目录
        print("报告目录：")
        report_file = report_path
        print(report_file)
        send_email(report_file)  # 发送邮件
        logging.info("================================== 发送邮件完成 ==================================")

if __name__ == "__main__":
    start()

























