# 开发人员：DYL
# 开发时间：2022/3/26 19:45

# if语句的使用

money = 1000
s = int(input("请输入取款金额："))
'''if s <= money:
    money -= s
    print("取款成功！余额为：", money)
else:
    print("取款失败，余额不足！")
'''
money -= s
print("取款成功!" if s <= money else "取款失败，余额不足！")  # 重点掌握这种方式：满足if条件就执行if语句前一句的代码，若不满足则执行else语句后面的代码
