# coding=utf-8

from bs4 import BeautifulSoup
from abc import ABCMeta, abstractmethod

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

        information_Nodes = soup.find('div', class_='inf_number_box clearfix')       
        for item in information_Nodes.find_all('dl'):
            for dd in item.find_all('dd'):
                re_data.append(dd.get_text())
        
        information_Nodes = soup.find('div', class_='interflow clearfix')
        for div in information_Nodes.find_all('div', class_='gradeAndbadge gradewidths'):
            re_data.append(str(div).split(' ')[3].split('\"')[1])

        information_Nodes = soup.find('div', class_='grade gradeAndbadge gradewidths')
        item = str(information_Nodes.find_all('div'))
        re_data.append(item.split(' ')[4][5])

        return dict(zip(re_keys, re_data))