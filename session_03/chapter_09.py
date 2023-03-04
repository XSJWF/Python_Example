# 开发人员：DYL
# 开发时间：2022/3/26 21:05

# 模拟ATM取款,break的使用

password = 8888
for i in range(3):
    if input("请输入密码：") == str(password):
        print("密码正确!")
        break
    else:
        print("密码错误！请再次输入，您还有", 2-i, "次机会")

print("\n____________________第二种方法：__________________\n")
i = 1
while i <= 3:
    if input("请输入密码：") == str(password):
        print("密码正确!")
        break
    else:
        print("密码错误！请再次输入，您还有", 3-i, "次机会")
    i += 1
