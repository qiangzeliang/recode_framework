# coding:utf-8
from unitest.common.Logger import *
import unittest
from time import sleep
import time
import requests
import json
from pprint import pprint
from unitest.common.VarConfig import *
from unitest.common.VarConfig import *
from unitest.common.readyaml import yamlread
import xlwings as xw

Reqspon = yamlread()  #实例化 读取yaml


class TestB(unittest.TestCase):

    """doublewin接口"""
    def Accountkit(self):
        """统计包登陆上报请求 https://accountkit.haloapps.com/v1.0/account/trace """
        event=Reqspon.Recode(recode_file="doublewin.har",read_file="doublewin.yml",yaml_name="/v1.0/account/trace", yaml_url="https://accountkit.haloapps.com/v1.0/account/trace")

        """
        同样的地址抓捕的时候抓出很多会话，找出符合条件的请求
        """
        Session = []
        for id, data in enumerate(event[0:]):
            session = event[id]
            Session.append(session)
            #if data["request"]["json"]["eventName"] == "af_purchase":  # 相同地址多个会话的请求
                # pprint(event[id])
                #session = event[id]
                #Session.append(session)
        print(id)
        pprint.pprint(Session)
        idn = 0  # 相同的数据 取数控制器
        revent = Session[idn]  # 取刷选后请求的第一个
        url = revent["request"]["url"]
        data = revent["request"]["data"]
        headers = revent["request"]["headers"]
        method = revent["request"]["method"]
        res = requests.post(url=url, data=data, headers=headers)
        ##############
        # 写入当前时间，下标从1开始
        now = int(time.time())  # 显示为时间戳
        timeArray = time.localtime(now)
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        #########################
        respon_status_code = res.status_code  # 返回状态码
        respon_headers = res.headers  # 返回头
        respon_body = json.loads(res.text)  # 返回体
        respon_cookies = res.cookies
        respon_history = res.history
        print(respon_body)
        print(respon_status_code, respon_headers, respon_cookies, respon_body, respon_history)
        if respon_status_code == 200:
            """处理返回数据解析表格输出数据"""
            idnum = idn + 1  ##序号
            code = respon_status_code  #请求状态返回code
            message = respon_body["message"]   # 返回信息
            vid = respon_body["data"]["vid"]  ##vid
            player_id = data["gameAccountId"]  # 玩家账号 也是用户信息
            userid = data["staToken"]  # userID
            token = data["thirdPartyToken"]  # 三方token
            package_name =data["packageName"]  # 包名
            platform = data["platform"] #平台
            event_list = [idnum, code, message, vid, player_id, userid, token, package_name, platform,currentTime]
            print(event_list)

        return event_list

    def Package_pay(self):
        """统计包支付上报请求 https://ssl08.haloapps.com/p/ggdirect """
        event = Reqspon.Recode(recode_file="doublewin.har",read_file="doublewin.yml",yaml_name="/p/ggdirect", yaml_url="https://ssl08.haloapps.com/p/ggdirect")

        """
        同样的地址抓捕的时候抓出很多会话，找出符合条件的请求
        """
        Session = []
        for id, data in enumerate(event[0:]):
            session = event[id]
            Session.append(session)
            #if data["request"]["json"]["eventName"] == "af_purchase":  # 相同地址多个会话的请求
                # pprint(event[id])
                #session = event[id]
                #Session.append(session)
        pprint.pprint(Session)
        idn = 0  # 相同的数据 取数控制器
        revent = Session[idn]  # 取刷选后请求的第一个
        url = revent["request"]["url"]
        data = revent["request"]["data"]
        headers = revent["request"]["headers"]
        method = revent["request"]["method"]
        res = requests.post(url=url, data=data, headers=headers)
        ##############
        # 写入当前时间，下标从1开始
        now = int(time.time())  # 显示为时间戳
        timeArray = time.localtime(now)
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        #########################
        respon_status_code = res.status_code  # 返回状态码
        respon_headers = res.headers  # 返回头
        respon_body = json.loads(res.text)  # 返回体
        respon_cookies = res.cookies
        respon_history = res.history
        print(respon_body)
        print(respon_status_code, respon_headers, respon_cookies, respon_body, respon_history)
        if respon_status_code ==200:
            """处理返回数据解析表格输出数据"""
            idnum = idn + 1  ##序号
            code = respon_status_code
            message = respon_body["message"]   # 返回信息
            product_id = data["product_id"]  ##产品ID
            player_id = data["cp_player_id"]  # 用户账户
            userid = data["device_id"]  # userID
            game_version = data["product_version"]  # 游戏版本
            sdk_version ="None"  # SDK版本
            androidid= "None" #Android ID

            event_list = [idnum, code, message, product_id, player_id, userid, game_version, sdk_version, androidid,currentTime]
            print(event_list)

        return event_list




    def Appsflyer_t(self):
        """安装归因请求 https://t.appsflyer.com/api/v4/androidevent """
        event = Reqspon.Recode(recode_file="doublewin.har",read_file="doublewin.yml",yaml_name="/api/v4/androidevent", yaml_url="https://t.appsflyer.com/api/v4/androidevent")

        """
        同样的地址抓捕的时候抓出很多会话，找出符合条件的请求
        """
        Session = []
        for id, data in enumerate(event[0:]):
            session = event[id]
            Session.append(session)
            #if data["request"]["json"]["eventName"] == "af_purchase":  # 相同地址多个会话的请求
                # pprint(event[id])
                #session = event[id]
                #Session.append(session)

        pprint.pprint(Session)
        idn = 0  # 相同的数据 取数控制器
        revent = Session[idn]  # 取刷选后请求的第一个
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
        #########################
        respon_status_code = res.status_code  # 返回状态码
        respon_headers = res.headers  # 返回头
        respon_body = json.loads(res.text)  # 返回体
        respon_cookies = res.cookies
        respon_history = res.history
        print(respon_body)
        print(respon_status_code, respon_headers, respon_cookies, respon_body, respon_history)
        if respon_status_code == 200:
            """处理返回数据解析表格输出数据"""
            idnum =idn+1   ##序号
            code = respon_status_code
            message =respon_body #返回信息
            af_version = params["buildnumber"] ##AF版本
            package_version =params["app_id"] #包名
            af_key = data["appsflyerKey"] #AF Key
            af_platform =data["platformextension"]  # AF平台
            gaid =data["advertiserId"]  #GAID
            uid = data["uid"]
            event_list =[idnum,code,message,af_version,package_version,af_key,af_platform,gaid,uid,currentTime]
            print(event_list)
        return event_list




    def Events(self):
        #t.appsflyer.com
        """支付事件请求 https://events.appsflyer.com/api/v4/androidevent? """
        event = Reqspon.Recode(recode_file="doublewin.har",read_file="doublewin.yml",yaml_name="/api/v4/androidevent", yaml_url="https://events.appsflyer.com/api/v4/androidevent")
        """
        同样的地址抓捕的时候抓出很多会话，找出符合条件的请求
        """
        Session =[]
        for id, data in enumerate(event[0:]):
            if data["request"]["json"]["eventName"] =="af_purchase":    #相同地址多个会话的请求
                #pprint(event[id])
                session = event[id]
                Session.append(session)
        pprint.pprint(Session)
        idn = 0  #相同的数据 取数控制器
        revent = Session[idn]  #取刷选后请求的第一个
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
        #########################
        pprint.pprint(res.text) #返回头
        respon_status_code = res.status_code #返回状态码
        respon_headers = res.headers  #返回头
        respon_body = json.loads(res.text)  #返回体
        respon_cookies = res.cookies
        respon_history = res.history
        print(respon_status_code,respon_headers,respon_cookies,respon_body,respon_history)
        if respon_status_code == 200:
            """处理返回数据解析表格输出数据"""
            idnum =idn+1   ##序号
            message =respon_body #返回信息
            af_version=params["buildnumber"] ##AF版本
            package_version =params["app_id"] #包名
            af_key = data["appsflyerKey"] #AF Key
            android_id ="None"  # Android ID
            gaid =data["advertiserId"]  #GAID
            eventName = data["eventName"]
            eventValue = data["eventValue"]
            event_list =[idnum,message,af_version,package_version,af_key,android_id,gaid,eventName,eventValue,currentTime]
            print(event_list)
        return event_list


    def Events_Common(self):
        #t.appsflyer.com
        """Appsflyer普通事件上报--events.appsflyercom"""
        event = Reqspon.Recode(recode_file="doublewin.har",read_file="doublewin.yml",yaml_name="/api/v4/androidevent", yaml_url="https://events.appsflyer.com/api/v4/androidevent")
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


    def test_T001(self):
        """ 统计包登陆上报请求的调用和表格输出"""
        #app.books.open(r"C:\Users\Avidly\Desktop\接口测试\InterfaceTest\unitest\common\avidly.xlsx")
        logging.info("执行控制表读取")
        self.app = xw.App(visible=False, add_book=False)
        wb = self.app.books.open(dataFilePath)
        sht = wb.sheets['执行控制表']
        isExcuteUser = sht.range('E2:E30').value
        dataBookColumn =sht.range('D2:D30').value

        for idx, i in enumerate(isExcuteUser[0:]):
            if i == "y":
                dataBookName = dataBookColumn[idx]
                print(dataBookName)
                if dataBookName =="doublewin":
                    try:
                        data_sht = wb.sheets[dataBookName]
                        print(data_sht)
                        contactNum = 0  # 记录添加成功联系人的个数
                        isExcuteNm = 0  # 记录需要添加联系人的个数
                        isExcuteData = data_sht.range("K3").value
                        print(isExcuteData)
                        for id,data in enumerate(isExcuteData):
                            if data == "y":
                                try:
                                    isExcuteNm += 1
                                    event_list = self.Accountkit() #登录请求调用
                                    print(event_list)
                                    data_sht.range("A3").value=event_list #二维数据输出点 写入表格
                                except Exception as e:
                                    data_sht.range("L3").value = "failed"
                                    data_sht.range("L3").color = (255, 0, 0)
                                    raise e

                                else:
                                    data_sht.range("L3").value = "pass"
                                    data_sht.range("L3").color= (0, 255, 127)
                                    contactNum += 1
                                    logging.info("资源表写入成功")
                            else:

                                print("非y行未输出")
                                logging.info("非y行未输出")
                    except:

                        pass
                    finally:
                        if contactNum == isExcuteNm:
                            logging.info("执行控制表结果返回成功")
                            print("----------------------------------------------------------")
                            print(idx)
                            sht.range(idx+2, 6).value = "pass"    #idx行号控制，开始取值是从第2行开始 +2，6表示第6列
                            sht.range(idx+2, 6).color = (0, 255, 127)  # 成功是绿色
                            print("----------------------------------------------------------")

                        else:
                            logging.info("执行控制表结果返回失败")
                            sht.range(idx+2, 6).value = "failed"
                            sht.range(idx+2, 6).color = (255, 99, 71)   #失败是红色

            else:
                print("执行控制表非y行未读取")
                logging.info("执行控制表非y行未读取")

                #sht = wb.sheets[dataBookName]
                #sht.range('E12').value= 22

        wb.save()
        wb.close()
        self.app.quit()
        sleep(5)

    def test_T003(self):
        """ 统计包支付上报请求的调用和表格输出"""
        #app.books.open(r"C:\Users\Avidly\Desktop\接口测试\InterfaceTest\unitest\common\avidly.xlsx")
        logging.info("执行控制表读取")
        self.app = xw.App(visible=False, add_book=False)
        wb = self.app.books.open(dataFilePath)
        sht = wb.sheets['执行控制表']
        isExcuteUser = sht.range('E2:E5').value
        dataBookColumn =sht.range('D2:D5').value

        for idx, i in enumerate(isExcuteUser[0:]):
            if i == "y":
                dataBookName = dataBookColumn[idx]
                print(dataBookName)
                if dataBookName =="doublewin":
                    try:
                        data_sht = wb.sheets[dataBookName]
                        print(data_sht)
                        contactNum = 0  # 记录添加成功联系人的个数
                        isExcuteNm = 0  # 记录需要添加联系人的个数
                        isExcuteData = data_sht.range("K15").value
                        print(isExcuteData)
                        for id,data in enumerate(isExcuteData):
                            if data == "y":
                                try:
                                    isExcuteNm += 1
                                    event_list = self.Package_pay() #统计包支付上报请求调用
                                    data_sht.range("A15").value= event_list #二维数据输出点 写入表格
                                except Exception as e:
                                    data_sht.range("L15").value = "failed"
                                    data_sht.range("L15").color = (255, 0, 0)
                                    raise e

                                else:
                                    data_sht.range("L15").value = "pass"
                                    data_sht.range("L15").color= (0, 255, 127)
                                    contactNum += 1
                                    logging.info("资源表写入成功")
                            else:

                                print("非y行未输出")
                                logging.info("非y行未输出")
                    except:

                        pass
                    finally:
                        if contactNum == isExcuteNm:
                            logging.info("执行控制表结果返回成功")
                            print("----------------------------------------------------------")
                            print(idx)
                            sht.range(idx+2, 6).value = "pass"    #idx行号控制，开始取值是从第2行开始 +2，6表示第6列
                            sht.range(idx+2, 6).color = (0, 255, 127)  # 成功是绿色
                            print("----------------------------------------------------------")

                        else:
                            logging.info("执行控制表结果返回失败")
                            sht.range(idx+2, 6).value = "failed"
                            sht.range(idx+2, 6).color = (255, 99, 71)   #失败是红色

            else:
                print("执行控制表非y行未读取")
                logging.info("执行控制表非y行未读取")

                #sht = wb.sheets[dataBookName]
                #sht.range('E12').value= 22

        wb.save()
        wb.close()
        self.app.quit()
        sleep(20)

    #@unittest.skip
    def test_T004(self):
        """ 安装归因请求的调用和表格输出"""
        #app.books.open(r"C:\Users\Avidly\Desktop\接口测试\InterfaceTest\unitest\common\avidly.xlsx")
        logging.info("执行控制表读取")
        self.app = xw.App(visible=False, add_book=False)
        wb = self.app.books.open(dataFilePath)
        sht = wb.sheets['执行控制表']
        isExcuteUser = sht.range('E2:E5').value
        dataBookColumn =sht.range('D2:D5').value

        for idx, i in enumerate(isExcuteUser[0:]):
            if i == "y":
                dataBookName = dataBookColumn[idx]
                print(dataBookName)
                if dataBookName =="doublewin":
                    try:
                        data_sht = wb.sheets[dataBookName]
                        print(data_sht)
                        contactNum = 0  # 记录添加成功联系人的个数
                        isExcuteNm = 0  # 记录需要添加联系人的个数
                        isExcuteData = data_sht.range("K30").value
                        print(isExcuteData)
                        for id,data in enumerate(isExcuteData):
                            if data == "y":
                                try:
                                    isExcuteNm += 1
                                    event_list = self.Appsflyer_t() #安装归因请求调用
                                    data_sht.range("A24").value= event_list #二维数据输出点 写入表格
                                except Exception as e:
                                    data_sht.range("L24").value = "failed"
                                    data_sht.range("L24").color = (255, 0, 0)
                                    raise e

                                else:
                                    data_sht.range("L24").value = "pass"
                                    data_sht.range("L24").color= (0, 255, 127)
                                    contactNum += 1
                                    logging.info("资源表写入成功")
                            else:

                                print("非y行未输出")
                                logging.info("非y行未输出")
                    except:

                        pass
                    finally:
                        if contactNum == isExcuteNm:
                            logging.info("执行控制表结果返回成功")
                            print("----------------------------------------------------------")
                            print(idx)
                            sht.range(idx+2, 6).value = "pass"    #idx行号控制，开始取值是从第2行开始 +2，6表示第6列
                            sht.range(idx+2, 6).color = (0, 255, 127)  # 成功是绿色
                            print("----------------------------------------------------------")

                        else:
                            logging.info("执行控制表结果返回失败")
                            sht.range(idx+2, 6).value = "failed"
                            sht.range(idx+2, 6).color = (255, 99, 71)   #失败是红色

            else:
                print("执行控制表非y行未读取")
                logging.info("执行控制表非y行未读取")

                #sht = wb.sheets[dataBookName]
                #sht.range('E12').value= 22

        wb.save()
        wb.close()
        self.app.quit()
        sleep(20)

    #@unittest.skip
    def test_T005(self):
        """ 支付事件请求的调用和表格输出"""
        #app.books.open(r"C:\Users\Avidly\Desktop\接口测试\InterfaceTest\unitest\common\avidly.xlsx")
        logging.info("执行控制表读取")
        self.app = xw.App(visible=False, add_book=False)
        wb = self.app.books.open(dataFilePath)
        sht = wb.sheets['执行控制表']
        isExcuteUser = sht.range('E2:E5').value
        dataBookColumn =sht.range('D2:D5').value

        for idx, i in enumerate(isExcuteUser[0:]):
            if i == "y":
                dataBookName = dataBookColumn[idx]
                print(dataBookName)
                if dataBookName =="doublewin":
                    try:
                        data_sht = wb.sheets[dataBookName]
                        print(data_sht)
                        contactNum = 0  # 记录添加成功联系人的个数
                        isExcuteNm = 0  # 记录需要添加联系人的个数
                        isExcuteData = data_sht.range("K30").value
                        print(isExcuteData)
                        for id,data in enumerate(isExcuteData):
                            if data == "y":
                                try:
                                    isExcuteNm += 1
                                    event_list = self.Events()
                                    data_sht.range("A30").value= event_list #二维数据输出点 写入表格
                                except Exception as e:
                                    data_sht.range("L30").value = "failed"
                                    data_sht.range("L30").color = (255, 0, 0)
                                    raise e

                                else:
                                    data_sht.range("L30").value = "pass"
                                    data_sht.range("L30").color= (0, 255, 127)
                                    contactNum += 1
                                    logging.info("资源表写入成功")
                            else:

                                print("非y行未输出")
                                logging.info("非y行未输出")
                    except:

                        pass
                    finally:
                        if contactNum == isExcuteNm:
                            logging.info("执行控制表结果返回成功")
                            print("----------------------------------------------------------")
                            print(idx)
                            sht.range(idx+2, 6).value = "pass"    #idx行号控制，开始取值是从第2行开始 +2，6表示第6列
                            sht.range(idx+2, 6).color = (0, 255, 127)  # 成功是绿色
                            print("----------------------------------------------------------")

                        else:
                            logging.info("执行控制表结果返回失败")
                            sht.range(idx+2, 6).value = "failed"
                            sht.range(idx+2, 6).color = (255, 99, 71)   #失败是红色

            else:
                print("执行控制表非y行未读取")
                logging.info("执行控制表非y行未读取")

                #sht = wb.sheets[dataBookName]
                #sht.range('E12').value= 22

        wb.save()
        wb.close()
        self.app.quit()
        sleep(5)

    #@unittest.skip
    def test_T006(self):
        """ 普通事件请求的调用和表格输出 """

        logging.info("执行控制表读取")
        self.app = xw.App(visible=False, add_book=False)
        wb = self.app.books.open(dataFilePath)
        sht = wb.sheets['执行控制表']

        isExcuteUser = sht.range('E2:E5').value
        dataBookColumn =sht.range('D2:D5').value

        for idx, i in enumerate(isExcuteUser[0:]):
            if i == "y":
                dataBookName = dataBookColumn[idx]
                print(dataBookName)
                if dataBookName == "doublewin":
                    try:
                        data_sht = wb.sheets[dataBookName]
                        print(data_sht)
                        contactNum = 0  # 记录添加成功联系人的个数
                        isExcuteNm = 0  # 记录需要添加联系人的个数
                        isExcuteData = data_sht.range("K34:K35").value
                        print(isExcuteData)
                        for id,data in enumerate(isExcuteData):
                            if data == "y":
                                try:
                                    isExcuteNm += 1
                                    event_list = self.Events_Common()
                                    data_sht.range("A35").value= event_list #二维数据输出点 写入表格
                                except Exception as e:
                                    data_sht.range("L35").value = "failed"
                                    data_sht.range("L35").color = (255, 0, 0)
                                    raise e

                                else:
                                    data_sht.range("L35").value = "pass"
                                    data_sht.range("L35").color= (0, 255, 127)
                                    contactNum += 1
                                    logging.info("资源表写入成功")
                            else:

                                print("非y行未输出")
                                logging.info("非y行未输出")
                    except:

                        pass
                    finally:
                        if contactNum == isExcuteNm:
                            logging.info("执行控制表结果返回成功")
                            print("----------------------------------------------------------")
                            print(idx)
                            sht.range(idx+2, 6).value = "pass"    #idx行号控制，开始取值是从第2行开始 +2，6表示第6列
                            sht.range(idx+2, 6).color = (0, 255, 127)  # 成功是绿色
                            print("----------------------------------------------------------")

                        else:
                            logging.info("执行控制表结果返回失败")
                            sht.range(idx+2, 6).value = "failed"
                            sht.range(idx+2, 6).color = (255, 99, 71)   #失败是红色

            else:
                print("执行控制表非y行未读取")
                logging.info("执行控制表非y行未读取")

                #sht = wb.sheets[dataBookName]
                #sht.range('E12').value= 22

        wb.save()
        wb.close()
        self.app.quit()
        sleep(5)

if __name__ == "__main__":
    unittest.main()
