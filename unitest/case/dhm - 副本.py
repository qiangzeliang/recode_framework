# coding:utf-8
from requests import Request, Session
from unitest.common.Logger import *
import unittest
from time import sleep
from tomorrow import threads
import requests
import json
from unitest.common.VarConfig import *
from unitest.common.ParseExcel import ParseExcel


#创建 excel数据文件的解析对象
excelObj = ParseExcel()
#将EXCEL数据文件加载到内存
# excelObj.loadWorkBook(u'D:\\TestFbs\\DataDrivenFrameWork\\testData\\126邮箱联系人.xlsx')
excelObj.loadWorkBook(dataFilePath)


class TestB(unittest.TestCase):

    def Accountkit(self):
        """登录上报请求https://accountkit.haloapps.com/v1.0/account/trace"""
        url = "https://accountkit.haloapps.com/v1.0/account/trace"
        data = {
            "platform": "android",
            "androidId": "",
            "gameAccountId": 1335,
            "staToken": "c8119026c634492688a4a88972d8e343",
            "packageName": "com.dreamhomematch.casual.free",
            "accountKitVersion": 0.0,
            "Host": "accountkit.haloapps.com",
            "gameVersio": 2689,
            "gaid": "9ce56836-90e2-4b44-b281-00067d396d5f",
            "thirdPartyToken": "EAAEmquxZApv8BAEZAW1QjW3wzalDvfPdAfHPEdP4tnBBwLnZAIpm89HuXasoZC30yZCn1RlqUmUGrpPUuMx99B1NF4IavqK8ZBCADsmpVxjhn7ICy2a781pyOYp2W6zz1PCTxi06hAJDEtZC1eHUtpBcxpNlUwGw66ZAdz2axdqehywg4tymatAjZChAenxaArQLACkSZAb7YxBAZAXE7skwRRub9F2vVSE2ocZD",
            "thirdPartyName": "facebook",

        }  # 字典格式，方便添加
        headers = {"Content-Type": "application/x-www-form-urlencoded;text/plain;application/json;charset=UTF-8",
                   "Accept": "*/*",
                   "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G9200 Build/MMB29K)",
                   "Connection": "Keep-Alive",
                   "Content-Encoding": "gzip"

                   }

        param = {""}
        cookies = {}

        res = requests.post(url=url, data=data)
        print(res.text)
        rsn = json.loads(res.text)

        if rsn["code"] == 200:
            return [json.loads(res.text), data]






    def test_A001(self):
        acoountkit =self.Accountkit()
        print(acoountkit[0]["code"])
        print(acoountkit[1])
        print(acoountkit[1]["platform"])




    def test_A002(self):
        logging.info("执行控制表读取")
        userSheet = excelObj.getSheetByName(u"执行控制表")
        # 获取126账号sheet中是否是执行列
        isExcuteUser = excelObj.getColumn(userSheet, account_isExcute)   #控制表是否执行行
        dataBookColumn = excelObj.getColumn(userSheet, account_dataBook)

        for idx, i in enumerate(isExcuteUser[1:]):

            if i.value == "y": #表示执行

                # 获取为第i行中用户联系人数据表sheet名
                dataBookName = dataBookColumn[idx + 1].value
                # 获取对应数据表对象
                dataSheet = excelObj.getSheetByName(dataBookName)

                isExcuteData = excelObj.getColumn(dataSheet, DHM_isExcute)
                contactNum = 0  # 记录添加成功联系人的个数
                isExcuteNm = 0  # 记录需要添加联系人的个数
                logging.info("资源表写入")
                for id, data in enumerate(isExcuteData[2:4]):
                    #登录上报写入
                    print(id)
                    print(data)
                    if data.value == "y":
                        ##解析区域
                        acoountkit = self.Accountkit()
                        code =acoountkit[0]["code"]
                        message =acoountkit[0]["message"]
                        vid = acoountkit[0]["data"]["vid"]
                        platform = acoountkit[1]["platform"]
                        androidId = acoountkit[1]["androidId"]
                        gameAccountId = acoountkit[1]["gameAccountId"]
                        staToken =acoountkit[1]["staToken"]
                        packageName = acoountkit[1]["packageName"]
                        accountKitVersion = acoountkit[1]["accountKitVersion"]
                        gaid = acoountkit[1]["gaid"]
                        thirdPartyToken = acoountkit[1]["thirdPartyToken"]
                        thirdPartyName = acoountkit[1]["thirdPartyName"]
                        ###行控制区域#########
                        isExcuteNm += 1  #是否执行行
                        excelid =3  #输出行号控制

                        ###写文件区域#########
                        try:
                            #登录上报信息

                            excelObj.writeCellCurrentTime(dataSheet, rowNo=id + excelid, colNo=DHM_runTime) #请求时间
                            logging.info("返回code写入")
                            excelObj.writeCell(dataSheet, str(code), rowNo=id + excelid, colNo=DHM_code,style="black")
                            logging.info("返回message写入")
                            excelObj.writeCell(dataSheet, str(message), rowNo=id + excelid, colNo=DHM_message,style="black")
                            logging.info("返回vid写入")
                            excelObj.writeCell(dataSheet, str(vid), rowNo=id + excelid, colNo=DHM_vid,style="black")
                            logging.info("返回gameAccountId写入")
                            excelObj.writeCell(dataSheet, str(gameAccountId), rowNo=id + excelid, colNo=DHM_gameAccountId,style="black")
                            logging.info("返回staTokend写入")
                            excelObj.writeCell(dataSheet, str(staToken), rowNo=id + excelid, colNo=DHM_staToken,style="black")
                            logging.info("返回thirdPartyToken写入")
                            excelObj.writeCell(dataSheet, str(thirdPartyToken), rowNo=id + excelid, colNo=DHM_thirdPartyToken,style="black")
                            logging.info("返回thirdPartyToken写入")
                            excelObj.writeCell(dataSheet, str(packageName), rowNo=id + excelid,colNo=DHM_packagename, style="black")
                            logging.info("返回thirdPartyToken写入")
                            excelObj.writeCell(dataSheet, str(platform), rowNo=id + excelid, colNo=DHM_platform,style="black")

                        except AssertionError as e:

                            excelObj.writeCell(dataSheet,"failed",rowNo= id+excelid,colNo= contacts_testResult,style="red")
                            raise e

                        else:
                            excelObj.writeCell(dataSheet,"pass",rowNo=id+excelid,colNo=contacts_testResult,style="green")
                            contactNum += 1
                            logging.info("资源表写入成功")

                    else:
                        print("登陆上报不规范行未执行")
                        logging.info("登陆上报不规范行未执行")

                print(contactNum)
                print(isExcuteNm)
                if contactNum == isExcuteNm:
                    logging.info("执行控制表结果返回成功")
                    excelObj.writeCell(userSheet,"pass",rowNo=idx+2,colNo=account_testResult,style="green")

                else:
                    logging.info("执行控制表结果返回失败")
                    excelObj.writeCell(userSheet,"failed",rowNo= idx+2,colNo=account_testResult,style= "red")


            else:
                print("控制表不执行未见异常")
                logging.info("控制表不执行未见异常")


if __name__ == "__main__":
    unittest.main()