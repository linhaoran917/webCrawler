# -*- coding: utf-8 -*-
import sys
from urllib import request
import re
from bs4 import BeautifulSoup
import urllib

__author__ = 'Haoran'


def generate_related_word(query, html_headers):
    # generate list of related_words from baidu search
    d = {'w': query}
    geturl = "http://www.baidu.com/s?%s" % urllib.parse.urlencode(d)
    req = urllib.request.Request(geturl, headers=html_headers)
    response = urllib.request.urlopen(req)
    page = response.read()
    soup = BeautifulSoup(page, 'html.parser')
    text = soup.select('#rs')
    pattern = re.compile(r'>\S*</a>')
    word = re.findall(pattern, str(text))
    # list 百度相关搜索词
    related_words = []
    for item in word:
        a = item[1:-4]
        related_words.append(a)
    return related_words


def _check_args():
    args = sys.argv
    if len(args) == 1:
        print('need a arguments!')
        return 0
    elif len(args) == 2:
        return 1
    else:
        print('Too many arguments!')
        return 0


if __name__ == '__main__':
    user_agent = """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)
        AppleWebKit/537.36 (KHTML, like Gecko)
        Chrome/53.0.2785.116 Safari/537.36"""
    headers = {'User-Agent': user_agent}
    if _check_args() == 1:
        relatedwords = generate_related_word(sys.argv[1], headers)
        for item in relatedwords:
            print(item)


