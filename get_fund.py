# -*- coding: utf-8 -*-
import urllib2
from setting import Setting
import re
import threadpool
import sys
print sys.getdefaultencoding()


class Get_fund:
    def __init__(self, url, regex):
        self.url = url
        self.regex = regex

    def download(self, user_agent='wswp'):
        print('Downloading:', self.url)
        headers = {'User-agnet': user_agent}
        request = urllib2.Request(self.url, headers=headers)
        html = ''
        try:
            html = urllib2.urlopen(self.url).read().decode("UTF-8")
        except Exception as e:
            print('Download error:', e)
        return html

    def get_data(self, html):
        return re.findall(self.regex, html)


def get_fund_data(url, regex, result_data):
    fund = Get_fund(list(url.values())[0], regex)
    data = fund.download()
    result = re.findall('[-+]\d+\.\d+%', fund.get_data(data)[0])
    result_data[list(url.keys())[0]] = result[0].encode('utf-8')
    return result


if __name__ == '__main__':
    settings = Setting()
    url_queue = settings.get_url()
    regex = settings.regex
    result_data = {}
    threadpool.threadpool(get_fund_data, url_queue, regex, result_data)
    keys = list(result_data.keys())
    fp = open(settings.result_path, 'w')
    for key in keys:
        line = key + ',' + result_data[key] + '\n'
        fp.write(line)
    fp.close()
# print(data)
