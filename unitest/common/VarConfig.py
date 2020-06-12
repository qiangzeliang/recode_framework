# coding = utf-8
import os
from unitest.common.readyaml import *

#获取当前文件所在目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#获取126账号工作表，每列对应的数字序号
dataFilePath = parentDirPath + u"\\Output\\avidly.xlsx"
######yaml文件配置区域#######
Inputfile = parentDirPath + u"\\Record_lib\\"


