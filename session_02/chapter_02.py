# 开发人员：DYL
# 开发时间：2022/3/26 16:52

# 输入函数 input()

present = input("大圣想要什么礼物呢？")
print(present, type(present))

a = input("请输入第一个加数：")
b = input("请输入第二个加数：")
print(a + b)
# input默认是str类型，所以结果是两个字符串连接起来

a = int(input("请输入第一个加数："))
b = int(input("请输入第二个加数："))
print(a+b)
