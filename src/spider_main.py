# coding=utf-8

import logging
import url_manerger, html_downloader, html_parser, outputer
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('./config/config.ini')
logger_name = config.get('logger', 'logger_name')

logger = logging.getLogger(logger_name)

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manerger.UrlManergerCsdn()
        self.downloader = html_downloader.HtmlDownloader()
        self.htmlparser = html_parser.HtmlParserCsdn()
        self.outputer = outputer.OutputerCsdn()       
        self.cnt = 0
    
    def goYou(self):       # 爬取
        # 初始化需要爬取的url列表
        self.urls.initial_url_list()
        while self.urls.have_new_url():            
            new_url = self.urls.get_new_url()
            self.cnt += 1
            try:
                html_cont = self.downloader.download(new_url)
                new_data = self.htmlparser.parse(html_cont)
                self.outputer.output(new_data)
                self.urls.old_urls.add(new_url)
            except Exception, e:
                self.urls.fail_urls.add(new_url)
                logger.error(e)
                logger.error('crawling is failed: %s' %new_url)
        logger.info('Crawling: %d ; Seccessed: %d ; Failed: %d' % (self.cnt, len(self.urls.old_urls), len(self.urls.fail_urls)))
        logger.info('crawling is done!')