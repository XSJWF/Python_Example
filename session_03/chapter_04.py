# 开发人员：DYL
# 开发时间：2022/3/26 20:06

# range的三种创建方式

r = range(10)  # 默认从零开始，且相邻的元素相差1
print(r)
print(list(r))  # list列表类似于数组

r = range(1, 10)  # 从1开始到10结束（不包括10），range(start, stop)
print(list(r))

r = range(1, 10, 2)  # 从1开始到10结束（不包括10），步长为2，range(start, stop, step)
print(list(r))

if 10 in r:
    print(10, "在r列表中")
else:
    print(10, "不在r列表中")
if 9 in r:
    print(9, "在r列表中")
else:
    print(9, "不在r列表中")

print(range(1, 20, 1))
'''此时虽然一个range表示的是1-20的数，另一个range表示的是1-101的数，但是他们所占的内存大小是一样的，
因为此时还没有真正使用到他们，现在占内存的只有其中的start、stop、step三个位置占用内存'''
print(range(1, 101, 1))
