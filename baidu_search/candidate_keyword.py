# -*- coding: utf-8 -*-
from config import mysql_db,headers
import pandas as pd
from baiduSearch import generate_related_word
import time
import signal

__author__ = 'Haoran'


# Register an handler for the timeout
def handler(signum, frame):
    print("timeout!")
    raise Exception("end of time")

# 从candidate table里读取keyword
resultQuery = pd.read_sql("select utm_term from sem.candidate_table order by recommend DESC limit 1000", mysql_db)
df = pd.DataFrame()
term = resultQuery['utm_term']

# Register the signal function handler
signal.signal(signal.SIGALRM, handler)



# 在百度里搜索 然后生成相关词(dataframe)
i = 0
while i < len(term):
    try:
        print(i)
        baiduQuery = term[i]
        # Define a timeout for your function
        signal.alarm(10)
        wdList = generate_related_word(baiduQuery)
        # Cancel the timer
        signal.alarm(0)
        tmp = pd.DataFrame({'utm_term': baiduQuery, 'related_word': wdList})
        # 导入mysql
        tmp.to_sql('Baidu_Related_words', mysql_db, flavor='mysql', if_exists='append', index=False)
        #time.sleep(1)
        i += 1

    except Exception as exc:
        continue



