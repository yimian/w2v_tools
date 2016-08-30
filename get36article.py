# -*- coding: utf-8 -*-
from pymongo import MongoClient
from langconv import *
import jieba
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')
testfile=open('36kr.txt','w')
mongo_client = MongoClient('mongodb://127.0.0.1:27017')
db = mongo_client['36kr']
answer_coll = db['articles']
time=0


for doc in answer_coll.find():
    time+=1
    text=doc['content']
    text=re.sub(r'<([^<>]*)>', '', text)
    #繁体字转简体
    text=Converter('zh-hans').convert(text.decode('utf-8'))
    text = text.encode('utf-8')
    str=" ".join(jieba.cut(text))#+''+doc['user']['name']
    testfile.write(str)
    print time
