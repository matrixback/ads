#!/usr/bin/env python
# encoding: utf-8

import urllib2 
import json 
import datetime 
import time 
import os 

def gen_file_name():
    dt = datetime.datetime.now()
    return 'ads-b-{}'.format(dt.strftime('%Y-%M'))

def mkdir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

if __name__ == '__main__':
    dir_name = '~/ads-b-data'
    mkdir(dir_name)
    while True:
        try:
            req = urllib2.urlopen('http://localhost:80')
            data = json.loads(req.read())
            file_name = gen_file_name()
            with open(os.paht.join(dir_name, file_name), 'a') as f:
                f.write(data)
                f.write('\n')
        except Exception as e:
            pass 
        
        time.sleep(1)



