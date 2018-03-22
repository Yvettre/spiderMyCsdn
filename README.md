# spiderMyCsdn

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/Yvettre/spiderMyCsdn/blob/master/LICENSE)

## Introduction
- 实现简单的爬虫，定时任务爬取[自己的csdn博客](http://blog.csdn.net/Yvettre)页面
- 解析阅读量、粉丝数、喜欢数、评论数、积分、排名等信息，结果存放在/result/output.csv
- 定时任务给自己发邮件报告当天的博客信息

## Environments
python-2.7.14

## Required Python Packages
simply one line as follow:
```
pip install -r requirements.txt
```

## Usages
get Blog information:
```
python main.py
```