# 开发人员：DYL
# 开发时间：2022/3/27 11:19

# index()方法获取列表索引的使用

list1 = ["Hello", "World", "Hello", "87"]

print(list1.index("Hello"))  # 如果列表中有多个重复元素，那么在查询它的时候只会返回第一个出现的该元素的索引

# print(list1.index("Python"))查询不存在的元素就会触发异常，可以试试。

print(list1.index("Hello", 1, 3))  # 在索引为1-3(不包括3)之间查找“Hello”的索引，注意使用格式


