from datetime import datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S') #str转换为datetime
print(cday)

ntime=datetime.now()
print(ntime)
print(ntime.strftime("%a,%b %d %H:%M"))