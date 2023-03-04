# 开发人员：DYL
# 开发时间：2022/3/26 20:36

# for循环的使用

for i in "Python":  # for的遍历循环对象必须为可迭代对象，比如：列表、字符串...
    print(i)
for i in range(10):
    print(i)
# 如果在循环体中不需要使用自定义变量可将其写成下划线
for _ in range(5):
    print("王八蛋")
# 使用for循环运算1-100的偶数和
i = 0
sum1 = 0
for _ in range(50):
    i += 2
    sum1 += i
print(sum1)
