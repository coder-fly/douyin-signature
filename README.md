## 使用chromedriver + mitmproxy持续获取抖音网页版signature
需要注意的是使用signature请求数据时，user-agent必须与获取sign时的user-agent保持一致，sign具有有效期，在有效期内可无限使用

## get
无需获取tac参数，直接get请求访问以下地址(user_id可更换)
- url:http://49.233.200.77:5001/sign/100000483090/
- response:

    `{
        "signature": "c0D5KBASLrTCHJP-GCbOh3NA-T",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }`
## post
自己获取tac并通过Post请求获取signature,详见demo.py

## other
- 代码中已经将ua写死，固定为
`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36`
- 获取无水印链接
`http://49.233.200.77:5001/watermark/6769364429223021837/`