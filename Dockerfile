FROM node:14.15.1-buster-slim

WORKDIR /apps/douyin
ADD douyin.js /apps/douyin/
EXPOSE 7878

RUN set -ex \
    && npm config set registry https://registry.npmmirror.com/ \
    && npm -g config set user root \
    && npm install jsdom@16.5.1 canvas@2.7.0 --canvas_binary_host_mirror=https://npm.taobao.org/mirrors/node-canvas-prebuilt/

CMD ["node", "douyin.js"]