# coding=utf-8

import datetime
import pandas as pd
from abc import ABCMeta, abstractmethod
import logging

logger = logging.getLogger('spiderCsdn')

class Outputer(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def output(self, data):
        pass


# 继承Outputer类
class OutputerCsdn(Outputer):
    
    def output(self, data):
        keys = data.keys()
        df = pd.DataFrame(columns=keys)
        data_list = []
        for i, key in enumerate(data):
            data_list.append(data[key])
        df.loc[i] = data_list

        time_format = '%Y-%m-%d-%H-%M-%S'
        time_now = datetime.datetime.now()
        bak_file = './result/output_%s.csv'%time_now.strftime(time_format)
        df.to_csv(bak_file, index=False, sep=' ', mode='wb', encoding='utf-8')  # for bac_up
        df.to_csv('./result/output.csv', index=False, sep=' ', mode='wb', encoding='utf-8')

        logger.info('bak_file: %s' %bak_file)