# 开发人员：DYL
# 开发时间：2022/6/16 14:58

# 集合的数学操作

# 求交集
s1 = {10, 20, 30, 40, 50}
s2 = {20, 30, 50, 60, 70}
print(s1.intersection(s2))
print(s1 & s2)  # "&"符号和intersection()方法等价

# 求并集
print(s1.union(s2))
print(s1 | s2)  # "|"符号和union()方法等价

# 求差集
print(s1.difference(s2))  # 求s1集合排除与s2的交集后剩下的元素所组成的集合
print(s1 - s2)

# 对称差集
print(s1.symmetric_difference(s2))  # 把s1和s2所有元素排除两个集合的交集所剩下的所有元素所组成的集合
print(s1 ^ s2)

