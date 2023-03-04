# 开发人员：DYL
# 开发时间：2022/4/18 20:13

# 获取字典中的元素

scores = {'张三': 100, '李四': 98, '王五': 97}

# 第一种方式，使用[]里面写键，用键取值

print(scores['张三'])

# 第二种方式，使用get()方法

print(scores.get('李四'))

# 使用第一种方式，如果输入的键不存在则会报出键错误(KeyError)，而使用第二种方式则不会报错，会返回一个NONE

# print(scores['黄三'])
print(scores.get('黄三'))
# 用get()方法可以传入一个默认值，意思就是，如果查找的键不存在，就返回这个默认值，如果存在就返回其本来的值
print(scores.get('黄三', 67))
print(scores.get('张三', 77))