import urllib.request
from setting import Setting
import os
import re
import threadpool


class Get_fund:
    def __init__(self, url, regex):
        self.url = url
        self.regex = regex

    def download(self, user_agent='wswp'):
        global html
        print('Downloading:', self.url)
        headers = {'User-agnet': user_agent}
        request = urllib.request.Request(self.url, headers=headers)
        try:
            html = urllib.request.urlopen(self.url).read().decode("UTF-8")
        except urllib.request.URLError as e:
            print('Download error:', e.reason)
        return html

    def get_data(self, html):
        return re.findall(self.regex, html)


def get_fund_data(url, regex, result_data):
    fund = Get_fund(list(url.values())[0], regex)
    data = fund.download()
    result = re.findall('[-+]\d+\.\d+%', fund.get_data(data)[0])
    result_data[list(url.keys())[0]] = result[0]
    return result


if __name__ == '__main__':
    settings = Setting()
    url_queue = settings.get_url()
    regex = settings.regex
    result_data = {}
    threadpool.threadpool(get_fund_data, url_queue, regex, result_data)
    print(result_data)
    keys = list(result_data.keys())
    fp = open(settings.result_path, 'w')
    for key in keys:
        line = key + ',' + result_data[key] + '\n'
        fp.write(line)
    fp.close()
# print(data)
