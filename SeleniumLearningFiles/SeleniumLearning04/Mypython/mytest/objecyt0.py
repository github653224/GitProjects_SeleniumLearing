# 假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：

std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

# print(std1["name"],std1["score"])

def print_score():
    print("%s:%s" %(std1["name"],std1["score"]) )

print_score()