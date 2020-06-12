import requests
import json
import os,time


now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 工程目录
pc_path = root_path + "\\testFile\\pcdata\\" + now + "_picture.jpg"  # report输出目录

cookies ={"PHPSESSID":"0d5fefbae58a4da06e282bca5d894d25"}  #图片链接的 cookies
headers ={"token":"c4b9f2d4-f2f8-46f4-b10e-a8817924a661"}  #图片链接的 token
"""
因为开启了电脑的代理，请求的时候会出现错误，取消代理再次可以获取到图片。其中cookies,token是登录页面的
"""
html = requests.get('https://demo.fastadmin.net/index.php?s=/captcha',cookies =cookies,headers=headers)
with open(pc_path, 'wb') as file:
    file.write(html.content)
    file.close()

import pytesseract
from PIL import Image

image = Image.open("C:\\Users\\\Avidly\\Desktop\\接口测试\\InterfaceTest\\unitest\\testFile\\pcdata\\2222_picture.png")
# In[*]
code = pytesseract.image_to_string(image)
print(code)

