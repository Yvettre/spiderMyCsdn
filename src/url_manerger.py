# coding=utf-8

from abc import ABCMeta, abstractmethod

class UrlManerger(object):
    __metaclass__ = ABCMeta 

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.fail_urls = set()
    
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls and url not in self.fail_urls:
            self.new_urls.add(url)
    
    def have_new_url(self):
        return len(self.new_urls) != 0
    
    def get_new_url(self):
        new_url = self.new_urls.pop()
        return new_url
    
    # 初始化需要爬取的url列表
    # 不同任务有不同的实现
    @abstractmethod
    def initial_url_list(self):
        pass


# 继承UrlManerger类
class UrlManergerCsdn(UrlManerger):
    
    # 初始化需要爬取的url列表
    # 这里只有一个链接
    def initial_url_list(self):
        new_url = 'http://blog.csdn.net/Yvettre'
        self.add_new_url(new_url)
