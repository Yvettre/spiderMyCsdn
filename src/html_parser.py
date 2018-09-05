# coding=utf-8

from bs4 import BeautifulSoup
from abc import ABCMeta, abstractmethod
import logging
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('./config/config.ini')
logger_name = config.get('logger', 'logger_name')

logger = logging.getLogger(logger_name)

class HtmlParser(object):
    __metaclass__ = ABCMeta 

    @abstractmethod
    def _get_new_data(self, soup):
        return
    
    def parse(self, html_cont):
        if html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_data = self._get_new_data(soup)

        return new_data


# 继承HtmlParser类
class HtmlParserCsdn(HtmlParser):
    
    def _get_new_data(self, soup):
        re_data = []
        re_keys = ['origin','fans','likey','comment','views','score','rank','level']

        information_Nodes = soup.find('div', class_='data-info d-flex item-tiling')       
        for item in information_Nodes.find_all('dl'):
            re_data.append(item['title'].encode('utf-8'))
        
        information_Nodes = soup.find('div', class_='grade-box clearfix').find_all('dl') 

        # 由于get_text()获得的结果中所需数据的前后有空白字符，使用strip()去掉前后的空白字符
        # 另外：lstrip()是去掉左边的空格，rstrip()是去掉右边的空格
        re_data.append(information_Nodes[1].find('dd')['title'].encode('utf-8'))  # 具体views量    
        # re_data.append(information_Nodes[1].find('dd').get_text().encode('utf-8').strip())  # 显示的views量
        re_data.append(information_Nodes[2].find('dd')['title'].encode('utf-8'))  # 具体score数
        # re_data.append(information_Nodes[2].find('dd').get_text().encode('utf-8').strip())  # 显示的score数
        re_data.append(information_Nodes[3]['title'].encode('utf-8'))  # rank

        # 由于获得的title内容是中文，使用unicode编码，无法直接使用str转为字符串
        # 因此加.encode('utf-8')转编码
        re_data.append(str(information_Nodes[0].find('a')['title'].encode('utf-8'))[0])  # level

        return dict(zip(re_keys, re_data))