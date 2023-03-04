# 开发人员：DYL
# 开发时间：2022/3/27 14:45

# 列表的排序

list1 = [23, 53, 64, 76, 86, 796, 54343, 244]
print("排序前的列表：", list1, id(list1))
list1.sort()  # 用sort()方法进行排序，默认升序，并且排序后不会产生新的列表对象
print("排序后的列表", list1, id(list1))

list1.sort(reverse=True)  # reverse=True为降序，reverse=False为升序，不写的话默认reverse=False
print("降序：", list1)
list1.sort(reverse=False)
print("升序", list1)

print("____________________使用内置函数sorted()进行排序，将会产生一个新的对象__________________")

list2 = [11, 2, 44, 66, 43, 86, 46]
print("原列表：", list2)
new_list = sorted(list2)  # 和sort()一样默认为升序
print("排序后：", new_list)

new_list = sorted(list2, reverse=True)  # 关键字使用的方法和sort()方法一样
print("降序：", new_list)
