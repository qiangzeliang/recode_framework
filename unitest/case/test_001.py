# coding:utf-8
from unitest.common.Logger import *
import unittest
from time import sleep
import time
import requests
import json
from pprint import pprint
from unitest.common.VarConfig import *
from unitest.common.readyaml import yamlread
import xlwings as xw

Reqspon = yamlread()  #实例化 读取yaml


class TestA(unittest.TestCase):

    def Events_Common(self):
        #t.appsflyer.com
        """Appsflyer普通事件上报--events.appsflyercom"""
        event = Reqspon.Recode(yaml_name="/api/v4/androidevent", yaml_url="https://events.appsflyer.com/api/v4/androidevent")
        """
        同样的地址抓捕的时候抓出很多会话，找出符合条件的请求
        """
        Session = []
        for id, data in enumerate(event[0:]):
            if data["request"]["json"]["eventName"] != "af_purchase":   #相同地址多个会话的请求循环请求一次
                session = event[id]
                #pprint(session)
                revent = session # 取刷选后请求的第一个
                url = revent["request"]["url"]
                params = revent["request"]["params"]
                data = revent["request"]["json"]
                headers = revent["request"]["headers"]
                method = revent["request"]["method"]
                res = requests.post(url=url, params=params, data=json.dumps(data), headers=headers)

                ##############
                # 写入当前时间，下标从1开始
                now = int(time.time())  # 显示为时间戳
                timeArray = time.localtime(now)
                currentTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                #################
                print(res.status_code)
                print(res.text)
                if res.status_code == 200:
                    """处理返回数据解析表格输出数据"""
                    idnum = id+1  #序号
                    res_message =res.text #返回信息
                    af_version =params["buildnumber"]
                    package_version = params["app_id"] #包名
                    af_key= data["appsflyerKey"]  #AF Key
                    androidi_d ="None"  #androidi_d
                    gaid = data["advertiserId"] #GAID
                    eventName = data["eventName"] #事件名
                    eventValue =data["eventValue"] #事件值
                    use_event =[idnum, res_message,af_version, package_version,af_key,androidi_d,gaid,eventName,eventValue,currentTime]  #生成列表
                    print(use_event)
                    logging.info(use_event)
                    Session.append(use_event) #将列表数据加载到列表里
        return Session


    def test_a(self):
        self.app = xw.App(visible=False, add_book=False)
        wb = self.app.books.open(dataFilePath)
        wb.save()
        wb.close()
        self.app.quit()

    def test_b(self):
        self.app = xw.App(visible=False, add_book=False)
        wb = self.app.books.open(dataFilePath)
        wb.save()
        wb.close()
        self.app.quit()

    def test_c(self):
        self.app = xw.App(visible=False, add_book=False)
        wb = self.app.books.open(dataFilePath)
        wb.save()
        wb.close()
        self.app.quit()

if __name__ == "__main__":
    unittest.main()