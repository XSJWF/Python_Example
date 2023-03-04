# 开发人员：DYL
# 开发时间：2022/4/28 11:33

# 集合的相关操作
s = {10, 2, 45, 567, 63}

# 元素判断操作
print(10 in s)
print(2 not in s)
print(33 not in s)

# 元素的新增操作
s.add(43)  # 一次添加一个元素用add
print(s)

s.update({20, 30, 40})  # 一次至少添加一个元素update
print(s)

s.update([39, 89, 67, 88])  # 添加列表
print(s)
s.update((11, 22, 33, 44))  # 添加元组
print(s)

# 元素的删除
s.remove(63)
# s.remove(9)  # 删除指定元素，如果指定元素不存在会抛出异常
print(s)
s.discard(44)
s.discard(4000)  # 删除指定元素，但是如果不存在不会抛出异常
print(s)

s.pop()  # pop()方法没有参数，随机删除一个元素
print(s)
s.pop()
print(s)

s.clear()  # 清空所有元素
print(s)
