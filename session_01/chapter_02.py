# 开发人员：DYL
# 开发时间：2022/3/26 11:18

# print()语句的使用

print(520)

print(98.99)

print("Hello World!")

print("3 + 1 =", 3 + 1)

fp = open("D:/text.txt", "a+")  # “a+”如果文件不存在就创建
print("Hello World!", file=fp)
fp.close()
