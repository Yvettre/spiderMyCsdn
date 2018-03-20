# coding=utf-8

import urllib2

class HtmlDownloader(object):
    
    def download(self, url):
        if url is None:
            return None
        request = urllib2.Request(url)
        request.add_header("user-agent","Mozilla/5.0")
        response = urllib2.urlopen(request)
        if response.getcode() != 200:
            return None
        return response.read()