# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 18:02
# @Author  : Coderfly
# @Email   : coderflying@163.com
# @File    : utils.py
import asyncio
from pyppeteer import connect

async def sign_(wsid,tac,user_id):
    browser = await connect(browserWSEndpoint=wsid)
    pages = await browser.pages()
    page = pages[0]
    await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
    sign = await page.evaluate('generateSignature',tac,user_id)
    return sign


def gen(wsid,tac,user_id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    sign = loop.run_until_complete(sign_(wsid,tac,user_id))
    return sign

if __name__ == '__main__':
    pass