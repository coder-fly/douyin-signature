# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 16:12
# @Author  : Coderfly
# @Email   : coderflying@163.com
# @File    : mitm.py
import logging
import mitmproxy.http

logging.basicConfig(level=logging.ERROR)

class Counter:

    def __init__(self):
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        # 修改js,将临时加密对象_bytedAcrawler保存为全局变量window.singer
        if "/page/reflow_user/index_" in flow.request.url:
            flow.response.text = flow.response.text.replace("signature=_bytedAcrawler.sign(nonce)","window.singer=_bytedAcrawler,signature = _bytedAcrawler.sign(nonce)")
        if "_signature=" in flow.request.url:
            print(f'sign:{flow.request.url.split("_signature=")[-1].split("&")[0]}')





addons = [
    Counter()
]