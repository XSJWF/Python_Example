# 开发人员：DYL
# 开发时间：2022/3/26 21:42

# 仔细体会最后的那个else，体会为什么输入正确后不会运行该语句，而三次输入错误后会运行该语句

a = 0
password = 8888
while a < 3:
    if input("请输入密码：") == str(password):
        print("密码正确！")
        break
    else:
        print("密码错误！您还有", 2 - a, "次机会")
    a += 1
else:
    print("你的三次机会已经用完！")
