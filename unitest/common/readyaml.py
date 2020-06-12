import pprint
import yaml
import os
from unitest.common.VarConfig import *
from unitest.common.Logger import *
from time import sleep

class yamlread():

    """解析及录制文件功能，设置读取文件参数，neme参数，url参数，必填"""

    def yaml_hdm(self,yaml_url, yaml_name):
        yml = os.system("har2case  C:\\Users\\Avidly\\Desktop\\接口测试\\InterfaceTest\\unitest\\Record_lib\\dhm.har -2y")
        file = "C:\\Users\\Avidly\\Desktop\\接口测试\\InterfaceTest\\unitest\\Record_lib\\dhm.yml"  # 解析文件
        if yml == 0:
            with open(file, encoding='utf-8') as fs:
                data = yaml.load(fs, Loader=yaml.FullLoader)
            fs.close()
            config = data["config"]  # yaml配置信息
            teststeps = data["teststeps"]  # yaml请求信息
            for id, data in enumerate(teststeps[0:]):
                #pprint.pprint(id)
                name = data["name"]
                url = data["request"]["url"]
                #print(teststeps[id])
                liso = []
                if (name == yaml_name and url == yaml_url):
                    # print(teststeps[id])
                    return {"index": id, "respon": teststeps[id]}

        else:
            print("test.har文件转换失败")
            logging.info("test.har文件转换失败")

    def Recode(self,recode_file, read_file, yaml_url, yaml_name):
        """解析文件升级版，将符合的地址以列表返回。在使用的请求数据中，以索引锁定，或者进一步以某个条件锁定"""
        parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        Inputfilelib = parentDirPath + u"\\Record_lib\\"
        print(Inputfilelib)
        ymlr = "har2case " + Inputfilelib + recode_file + " -2y"   ##转换命令
        readyaml = os.system(ymlr)       #转换har文件
        if readyaml == 0:
            file = Inputfilelib + read_file  # 读取aml文件件目录
            with open(file, encoding='utf-8') as fs:
                data = yaml.load(fs, Loader=yaml.FullLoader)
            fs.close()
            config = data["config"]  # yaml配置信息
            teststeps = data["teststeps"]  # yaml请求会话信息
            liso = []
            for id, data in enumerate(teststeps[0:]):
                # pprint.pprint(id)
                name = data["name"]
                url = data["request"]["url"]
                # print(teststeps[id])
                if (name == yaml_name and url == yaml_url):
                    name = data["name"]
                    url = data["request"]["url"]
                    respon = teststeps[id]
                    liso.append(respon)
            return liso

        else:
            print("har文件转换失败")
            logging.info("har文件转换失败")


if __name__ == "__main__":

    ya = yamlread()
    pprint.pprint(ya.Recode(recode_file="doublewin.har",read_file="doublewin.yml",yaml_name="/v1.0/account/trace", yaml_url="https://accountkit.haloapps.com/v1.0/account/trace"))








