# 开发人员：DYL
# 开发时间：2022/3/26 17:49

# 希尔运算符

a, b = 1, 2
print(a == 1 and b == 2)  # “and”和“&&”类似
print(a == 1 and a == b)
print(a == 2 and b == 3)
print(a == 1 or b == 2)  # "or"和“||”类似
print(a == 1 or b == 1)
print(a == 2 or b == 1)
f1 = True
f2 = False
print(not f1)  # 对bool类型的操作数取反
print(not f2)

print("________________in__________________")
s = "Hello World"
print("w" in s)
print("W" in s)
print("o" in s)
# 用于检验某个字符是否在某个字符串中
