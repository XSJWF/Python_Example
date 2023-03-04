# 开发人员：DYL
# 开发时间：2022/4/28 11:46


# 集合之间的关系
s1 = {10, 20, 30, 40}
s2 = {20, 10, 40, 30}
# 用==或者！=判断
print(s1 == s2)
print(s1 != s2)
# 因为集合的元素的无序的所以，这两个集合不管内部元素是怎样排列的是要是相同的那么两个集合就是相等的

# 判断一个集合是否是另一个集合的子集合
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40, 50}
s3 = {10, 20, 30}
print(s2.issubset(s1))
print(s3.issubset(s2))
print(s1.issubset(s2))

# 判断一个集合是否是另一个集合的超集
print(s1.issuperset(s2))
s3 = {10, 20, 90}
print(s2.issuperset(s3))

# 判断两个结合是否有交集
print(s2.isdisjoint(s1))  # 有交集为False
s3 = {11, 22, 33}
print(s2.isdisjoint(s3))  # 没有交集为True
