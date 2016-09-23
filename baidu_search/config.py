# -*- coding: utf-8 -*-
from sqlalchemy import create_engine

__author__ = 'Haoran'


mysql_db = create_engine('mysql+pymysql://root:growth@192.168.20.96:3306/sem?charset=utf8', echo=False)
user_agent = """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)
                AppleWebKit/537.36 (KHTML, like Gecko)
                Chrome/53.0.2785.116 Safari/537.36"""
headers = {'User-Agent': user_agent}
