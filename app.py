# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 11:00
# @Author  : Coderfly
# @Email   : coderflying@163.com
# @File    : demo.py
import requests
import random
import time
import sys
import logging
from threading import Thread
from flask import Flask,render_template,request,jsonify
from queue import Queue, Empty
from config import *
from utils import gen
from async_tac import do_get_tac, headers

logging.basicConfig(level=logging.ERROR)

sign_queue = Queue()

app = Flask(__name__)

ws = ''
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
tac_queue = []

@app.errorhandler(Empty)
def error(e):
    return e

@app.before_first_request
def open_service():
    global ws
    if sys.platform.startswith('win'):
        os.system('start /b python chrome.py')
    else:
        os.system('nohup python chrome.py > /dev/null &')
    # 首次启动 等待打开
    time.sleep(5)
    with open('ws', 'r') as f:
        ws = f.read()
    thread = Thread(target=do_get_tac)
    thread.start()
    app.tac_flag = False

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/",methods=['POST'])
def sign():
    tac = request.form.get("tac")
    user_id = request.form.get("user_id")
    if not all([tac,user_id]):
        return 'argements error',401
    sign = gen(ws,tac,user_id)
    return jsonify({
        'signature':sign,
        'user-agent':ua
    })

@app.route('/tac/',methods=['POST'])
def tac():
    # 异步程序一直获取sign
    global tac_queue
    tac = request.form.get("tac")
    if not tac:
        return ""
    tac_queue.append(tac)
    return "success"

@app.route('/sign/<int:user_id>/')
def sign_userid(user_id):
    global ws, tac_queue
    if len(tac_queue) == 0:

        return jsonify({
            'error': '1',
        })
    tac_queue = tac_queue[-5:]
    tac = random.choice(tac_queue)
    # 异步程序一直获取sign
    sign = gen(ws, tac, user_id)
    return jsonify({
        'signature': sign,
        'user-agent': ua
    })


@app.route('/get_sign/',methods=['POST'])
def get_sign():
    global ws,tac_queue
    user_id = request.form.get("user_id")
    if len(tac_queue) == 0:
        return jsonify({
        'error': '1',
    })
    tac_queue = tac_queue[-10:]
    tac = random.choice(tac_queue)
    # 异步程序一直获取sign
    sign = gen(ws, tac, user_id)
    return jsonify({
        'signature': sign,
        'user-agent': ua
    })


if __name__ == '__main__':
    app.run(debug=True, port=port)
