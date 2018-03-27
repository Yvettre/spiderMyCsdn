# coding=utf-8

from src import *
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config/config.ini')
logger_name = config.get('logger', 'logger_name')

logger = log.setup_custom_logger(logger_name)

def main():
    spider = spider_main.SpiderMain()
    spider.goYou()


if __name__ == '__main__':
    main()