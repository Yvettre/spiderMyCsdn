# coding=utf-8

from src import *

logger = log.setup_custom_logger('spiderCsdn')

def main():
    spider = spider_main.SpiderMain()
    spider.goYou()


if __name__ == '__main__':
    main()