# -*- coding: utf-8 -*-
import requests
import re
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q=0.9"
}

response = requests.get('https://www.iesdouyin.com/share/user/58958068057',headers=headers,verify=False)

tac = re.search(r"tac='([\s\S]*?)'</script>",response.text).group(1)
data = {
    "tac":tac.split("|")[0],
    'user_id':'58958068057'
}

response = requests.post('http://49.233.200.77:5001',data=data)

sign = response.json().get('signature')

url = "https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id={}&sec_uid=&count=21&max_cursor=0&aid=1128&_signature={}"
uids = '''100000212300
100000236218
100000483090'''
proxies = {
    # 'https':'https://' + '180.105.100.172:30111'
}
for uid in uids.splitlines():
    url = url.format(uid.strip(),sign)
    response = requests.get(url,headers=headers,verify=False,proxies=proxies)
    print(response.json())