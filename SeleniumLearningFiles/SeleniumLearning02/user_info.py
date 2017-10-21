user_file=open(r"D:\Users\Administrator\PycharmProjects\web\user_info.txt","r")
# print(user_file.read())
lines=user_file.readlines()
print(lines)
user_file.close()

for line in lines:
    username=line.split(",")[0]
    password=line.split(",")[1]

print(username,password)
