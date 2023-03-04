# 开发人员：DYL
# 开发时间：2022/3/26 21:53

# 输出一个三行四列的矩阵

for i in range(1, 4):
    for j in range(1, 5):
        print("*", end="\t")  # 不换行输出,也可以写为 end="" ，不写 end= 的话 默认是 end="\n"
    print()  # 换行

# 打印九九乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, "*", i, "=", i * j, end="\t")
    print()
# break和continue在多重循环中只控制本层循环
