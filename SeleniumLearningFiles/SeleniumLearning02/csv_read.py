import csv
date = csv.reader(open(r"D:\Users\Administrator\PycharmProjects\web\user_info.csv","r"))

# 取用户的邮箱地址
for user in date:
   print(user[1])
   print(user[3])