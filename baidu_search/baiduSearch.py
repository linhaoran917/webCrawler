# -*- coding: utf-8 -*-
import sys
import urllib.request
import re
from bs4 import BeautifulSoup
import urllib

__author__ = 'Haoran'
if __name__ == '__main__':
    
    user_agent = """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)
        AppleWebKit/537.36 (KHTML, like Gecko)
        Chrome/53.0.2785.116 Safari/537.36"""
    headers = {'User-Agent': user_agent}
    
    query = sys.argv[1]
    d = {'w': query}
    geturl = "http://www.baidu.com/s?%s"%urllib.parse.urlencode(d)
    request = urllib.request.Request(geturl, headers=headers)
    response = urllib.request.urlopen(request)
    page = response.read()
    soup = BeautifulSoup(page, 'html.parser')
    text = soup.select('#rs')
    pattern = re.compile(r'>\S*</a>')
    word = re.findall(pattern, str(text))
    for item in word:
        a = item[1:-4]
        print(a)
