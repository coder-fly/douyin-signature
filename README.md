# 分享页抖音


## 说明
稍微修改了一下代码，并找到了代码中检测node与浏览器差异的部分，现已可以直接使用node运行
需要网页版抖音的，请移步[网页版某音signature获取,支持搜索、点赞、关注](https://github.com/coder-fly/douyin_web_signature)

## usage
```
npm install jsdom@16.5.1 canvas@2.7.0

node douyin.js

# then
curl http://127.0.0.1:7878
```

## Docker
```
docker run -d -p 7878:7878 --name douyin --rm  makkapakka/douyin-web:latest

# then
curl http://127.0.0.1:7878
```

## 版权说明
仅供交流学习使用，严禁商业用途
