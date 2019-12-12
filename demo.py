# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 15:28
# @Author  : Coderfly
# @Email   : coderflying@163.com
# @File    : demo.py

import requests

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    # "referer": "https://www.iesdouyin.com/share/user/58958068057",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    # "cookie": "_ga=GA1.2.1933718197.1569723451; _gid=GA1.2.574325593.1569723451",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9"
}

url = "https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id=93537979910&sec_uid=&count=21&max_cursor=0&aid=1128&_signature={}"

response = requests.get(url.format('MIUt2hAabXuB2UcML9KZxzCFLc'),headers=headers,verify=False)
print(response.text)
