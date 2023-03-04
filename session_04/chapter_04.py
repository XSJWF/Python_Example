# 开发人员：DYL
# 开发时间：2022/3/27 12:59

# 列表元素的添加操作

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list1, id(list1))
list1.append("hello")  # 使用append()方法在列表末尾添加一个元素
print(list1, id(list1))  # 添加元素过后并不会创建新的列表对象

list2 = ["王八蛋", "大傻逼", "聪明蛋"]
list1.append(list2)  # 将list2整体作为一个对象添加到list1末尾
print(list1)  # 仔细观察运行结果

list1.extend(list2)  # 用extend方法想列表末尾添加多个元素
print(list1)  # 运行后，仔细观察和上面添加方法的区别

list1.insert(1, 90)  # 在索引为1的位置上插入元素90，insert()方法可以在任意位置插入
print(list1)

# 用切片操作在任意位置添加多个元素
list3 = ["魔鬼", "天使", "凡人"]
list1[1:] = list3  # 把索引为1之后的元素切掉用list3代替
# list1[1:5] = list3 把索引为1到5之间的元素切掉用list3代替
print(list1)


