# spiderMyCsdn

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/Yvettre/spiderMyCsdn/blob/master/LICENSE)

## Introduction
- 实现简单的爬虫，定时任务爬取[自己的csdn博客](http://blog.csdn.net/Yvettre)页面
- 解析阅读量(views)、粉丝数(fans)、喜欢数(likey)、评论数(comment)、积分(score)、排名(rank)、等级(level)等信息，结果存放在/result/output.csv
- 定时任务给自己发邮件报告当天的博客信息
- 增加``mysql``模块，将博客信息导入本地的mysql数据库中
- 增加``config.ini``，方便统一配置待爬取页面的根链接、mysql的配置信息以及logger的标识名
- 关于代码的详细介绍可戳[我的博文](https://blog.csdn.net/yvettre/article/details/79887024)

## Environments
- python-2.7.14
- mysql-5.5.35

## Required Python Packages
simply one line as follow:
```
pip install -r requirements.txt
```

## Usages
- create mysql database
```
create database yvettre;
```
- create table csdn
```
use yvettre;
create table if not exists csdn (datetime DATETIME, origin int, fans int, likey int, comment int, views int, score int, rank int, level int);
```
- get Blog information:
```
python main.py
```