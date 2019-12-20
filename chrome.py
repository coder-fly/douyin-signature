import asyncio

from pyppeteer.launcher import connect, launch

"""可以打开一个chrome，获取ws信息，然后后续的操作都在这一个浏览器上进行"""
webdriver_js = '''() =>
           Object.defineProperties(navigator,{
             webdriver:{
               get: () => false
             }
           })

'''

async def connect_chrome():
    browser = await launch(headless=True,args=["--no-sandbox"])
    with open("ws","w") as f:
        f.write(browser.wsEndpoint)
    page = await browser.pages()
    page = page[0]
    await page.setUserAgent(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
    await page.evaluate(webdriver_js)
    await page.goto("http://127.0.0.1:5000")
    await asyncio.sleep(20000000)
    await page.close()
    await browser.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(connect_chrome())