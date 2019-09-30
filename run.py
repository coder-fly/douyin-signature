# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 11:00
# @Author  : Coderfly
# @Email   : coderflying@163.com
# @File    : demo.py
import time
import subprocess
import logging
from flask import Flask
from threading import Thread
from queue import Queue, Empty
from constants import *
logging.basicConfig(level=logging.ERROR)

sign_queue = Queue()
app = Flask(__name__)

@app.errorhandler(Empty)
def error(e):
    return "暂无sign"

@app.route("/")
def index():
    sign = sign_queue.get(timeout=2)
    sign_queue.task_done()
    return sign[5:].decode().strip()

def open_mitmproxy():
    thread = subprocess.Popen(r"{} -s {} --listen-host {}  --listen-port {} --set termlog_verbosity=error".format(mitmdump_bin,mitmdump_script,mitmproxy_host,mitmproxy_port),stdout=subprocess.PIPE,shell=True,stdin=subprocess.PIPE,)
    while thread.poll() == None:
        message = thread.stdout.readline()
        if message.startswith(b"sign"):
            sign_queue.put(message)
            time.sleep(1)
def open_chrome():
    os.system(f"python chrome.py")

def open_backup():
    app.run(debug=False)

def run():
    threads = []
    threads.append(Thread(target=open_mitmproxy))
    threads.append(Thread(target=open_chrome))
    threads.append(Thread(target=open_backup))
    for thread in threads:
        thread.start()

if __name__ == '__main__':
    run()
