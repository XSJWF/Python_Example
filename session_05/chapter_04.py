# 开发人员：DYL
# 开发时间：2022/4/18 20:35

# 字典的常用操作

# 获取所有的key
scores = {'张三': 100, '李四': 98, '王五': 97}
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有的键组成的视图转成列表

# 获取所有的value
values = scores.values()
print(values)
print(type(values))
print(list(values))  # 转成列表

# 获取所有的键值对(key-value)
items = scores.items()
print(items)  # 结果中的每一个小括号是一个元组（数据类型）
print(type(items))
