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
        re_data = {}

        cnt = 0
        information_Nodes = soup.find('div', class_='inf_number_box clearfix')       
        for item in information_Nodes.find_all('dl'):
            cnt += 1
            for dd in item.find_all('dd'):
                if cnt==1:
                    re_data['origin'] = dd.get_text()
                elif cnt == 2:
                    re_data['fans'] = dd.get_text()
                elif cnt == 3:
                    re_data['like'] = dd.get_text()
                elif cnt == 4:
                    re_data['comment'] = dd.get_text()
        
        information_Nodes = soup.find('div', class_='interflow clearfix')
        span = information_Nodes.find_all('span')
        re_data['views'] = span[2].get_text()
        re_data['score'] = span[4].get_text()
        re_data['rank'] = span[6].get_text()

        information_Nodes = soup.find('div', class_='grade gradeAndbadge gradewidths')
        item = str(information_Nodes.find_all('div'))
        re_data['level'] = item.split(' ')[4][5]

        return re_data