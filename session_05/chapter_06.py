# 开发人员：DYL
# 开发时间：2022/4/18 20:45

# 字典中键不能重复，值可以重复

dic = {'name': '张三', 'name': '李四'}
print(dic)  # 如果键重复了name就会出现值的覆盖

dic1 = {'name': '张三', 'nikeName': '张三'}
print(dic1)

# 字典时无序的，其实也是有序的（根据hash()函数计算出来的hash值来排序的）
# 字典的内存随便元素的增加减少来增加减少

# 字典生成式

# 使用内置函数zip()将对应的元素打包成一个元组，然后返回由这些元组生成的列表，生成字典
# zip()括号中的对象必须是一个可迭代对象，即可以循环遍历的对象

items = ['Fruits', 'Books', 'Others']
prices = [98, 89, 77, 98]

dic2 = {items: prices for items, prices in zip(items, prices)}
print(dic2)  # 最终生成三个字典元素，在压缩生成的过程中会以元素少的那个列表为基准生成字典
