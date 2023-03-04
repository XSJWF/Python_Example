# 开发人员：DYL
# 开发时间：2022/3/27 14:17

# 列表元素的删除

list1 = [1, 2, 3, 4, 5, 6, 3]
list1.remove(2)  # remove(i)，移除值为i的元素
print(list1)
list1.remove(3)  # 有重复元素，只会移除第一个出现的
print(list1)

list2 = [1, 2, 3, 4, 5, 6, 7]
list2.pop(1)
print(list2)
list2.pop(5)
print(list2)
# pop(i)移除指定索引i位置上的元素，如果不指定参数索引即pop()，将会默认删除列表中的最后一个元素

list3 = [1, 2, 3, 4, 5, 6, 7]
new_list = list3[1:3]  # 切片操作会产生一个新的对象
print(new_list)

# 不产生新对象的切片操作
print(list3)
list3[1:3] = []
print(list3)

# 清除列表中的所有元素

list3.clear()
print(list3)  # 只清除元素不删除列表

# 删除列表
del list3  # 将列表删除
print(list3)  # 报错，列表不存在
