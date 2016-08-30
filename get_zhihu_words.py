# -*- coding: utf-8 -*-
from pymongo import MongoClient
from langconv import *
import jieba
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')
testfile=open('text.txt','w')
mongo_client = MongoClient('mongodb://127.0.0.1:27017')
db = mongo_client['zhihu_movie']
answer_coll = db['answer_content']
time=0


for doc in answer_coll.find():
    time+=1
    text=re.sub(r'<([^<>]*)>', '', doc['answer_content'])
    #繁体字转简体
    text=Converter('zh-hans').convert(text.decode('utf-8'))
    text = text.encode('utf-8')
    str=" ".join(jieba.cut(text))#+''+doc['user']['name']
    testfile.write(str)
    print time
