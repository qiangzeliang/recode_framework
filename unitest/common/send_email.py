import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
from unitest.common.Logger import *
from unitest.readConfig import *
semail = ReadConfig()

def send_email(report_file):

    logging.info("报告添加邮件")
    msg = MIMEMultipart()  # 混合MIME格式
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）

    logging.info("邮件头设置")
    msg['From'] = semail.get_email("From")  # 发件人
    msg['To'] = semail.get_email("To")  # 收件人
    msg['Subject'] = Header('接口测试报告', 'utf-8')  # 中文邮件主题，指定utf-8编码

    logging.info("上传附件")
    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'  # filename为邮件中附件显示的名字
    msg.attach(att1)

    try:
        logging.info("登录邮箱")
        smtp = smtplib.SMTP_SSL(semail.get_email("mail_host"))  # smtp服务器地址 使用SSL模式
        smtp.login(semail.get_email("mail_user"), semail.get_email("mail_pass"))  # 用户名和密码
        smtp.sendmail(semail.get_email("sender"), semail.get_email("receiver"), msg.as_string())
        # smtp.sendmail("test_results@sina.com", "superhin@126.com", msg.as_string())  # 发送给另一个邮箱
        logging.info("邮件发送完成！")

    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()


if __name__ == '__main__':

    report_file ="C:\\Users\\Avidly\\Desktop\\接口测试\\InterfaceTest\\unitest\\Report\\2020-05-23 11_19_08_api_report.html"
    print(report_file)
    send_email(report_file)
