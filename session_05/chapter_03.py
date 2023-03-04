# 开发人员：DYL
# 开发时间：2022/4/18 20:24

# 字典中的基本操作，增删改等

# 字典中是否存在某个元素的判断，对该元素的键使用in或者not in来判断判断该元素是否存在字典中，语句为真返回TRUE，为假返回False

scores = {'张三': 100, '李四': 98, '王五': 97}
print('张三' in scores)
print('张三' not in scores)
print('黄七' in scores)
print('黄七' not in scores)

# 删除元素操作

del scores['张三']
print(scores)
# 清空字典元素
scores.clear()
print(scores)

# 新增字典元素

scores['陈明'] = 89
print(scores)

# 膝盖字典元素

scores['陈明'] = 69
print(scores)
