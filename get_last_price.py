import tushare as ts
import redis
import datetime
import time
import sys


list1=sys.argv[1:]

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
# print(list1)

# pre_c=ts.get_realtime_quotes(c)['pre_close']
# def get_lastprice():

for i in list1:
    i=str(i)
    if i[0]=='0' or i[0]=='3':

        pre_c=ts.get_realtime_quotes(i)['pre_close'][0]



        nt = datetime.datetime.now()
        strnt=nt.strftime('%Y%m%dT%H%M%S.%f')
        v=strnt[:-3]+','+pre_c+','+'0'
        i=i+'.SZ'
        r.hset("HXMS.tomo",i,v)
print('ok')

# get_lastprice()


