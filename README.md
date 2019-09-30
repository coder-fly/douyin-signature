## 使用chromedriver + mitmproxy持续获取抖音网页版signature
需要注意的是使用signature请求数据时，user-agent必须与获取sign时的user-agent保持一致，sign具有有效期，在有效期内可无限使用

## 使用方法
- 安装依赖,chrome,
- python run.py
- 访问localhost:5000端口夺取队列中的sign