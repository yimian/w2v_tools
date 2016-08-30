# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

lines=open('tech_all_low').readlines()
newfile=open('tc','a')

for line in lines:
    newline=line.replace('’s',' ').replace(' s ',' ').replace('“',' ').replace('’',' ').replace('” ',' ')
    newfile.write(newline)

