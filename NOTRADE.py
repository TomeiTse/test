import redis
import sys
list2=sys.argv[1:]
r=redis.StrictRedis(host='127.0.0.1',port=6379)
b=r.lrange('NOTRADE',0,-1)
for a in list2:
    a=str(a)

    # print(type(a))

    # b = str(b)
    # print(b)
    if a[0]=='0':
        c=b[0].decode()+','+a+'.SZ'

    if a [0]=='6':
        c =b[0].decode()+','+ a + '.SH'
d = r.lset('NOTRADE', 0, c)

