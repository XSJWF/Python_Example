# 开发人员：DYL
# 开发时间：2022/3/26 20:30
# 计算1-100之间的偶数和
i = 1
sum1 = 0
while i <= 100:
    if i % 2 == 0:  # 也可以写成 if not i % 2:   因为0的bool值为零
        sum1 += i
    else:
        pass
    i += 1
print("1-100之间的偶数和为：", sum1)
