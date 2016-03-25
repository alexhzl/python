# -*- coding: utf-8 -*-
'''
Created on 2016-03-25

@author: HuangZili
'''

import sys
from datetime import *
import pymongo

def main():
    date_begin = datetime.strptime(str(sys.argv[1]), '%Y-%m-%d')
    date_end = datetime.strptime(str(sys.argv[2]), '%Y-%m-%d')
    
    conn = pymongo.MongoClient(host="127.0.0.1", port=27017)
    mydb = conn.logdb
    mycoll = mydb.access_log

    for i in range (0, int ((date_end - date_begin).days) + 1):
        cdate = date_begin + timedelta(days=i)  
        cdatestr = datetime.strftime(cdate, '%Y-%m-%d')
        print cdatestr,
        print mycoll.find({'date': cdatestr, 'urlpath': '/xxxx'}).count(),
        print len(mycoll.distinct('ipaddr', {'date': cdatestr, 'urlpath': '/xxxx'}))

if __name__ == '__main__':
    main()
