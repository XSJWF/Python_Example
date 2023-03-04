# 开发人员：DYL
# 开发时间：2022/3/26 16:31

# 类型转化

name = "张三"
age = 20
print(type(name), type(age))
# print("我叫"+name+",今年"+age+"岁")
print("我叫" + name + ",今年" + str(age) + "岁")  # "+"是连接符,不同类型的数据不能进行连接，str()函数可以将int等其他类型转为str类型
print("________________________使用str()将其他类型转化为str类型_________________________")
a = 10
b = 198.8
c = False
print(type(a), type(b), type(c))
print(type(str(a)), type(str(b)), type(str(c)))
print("________________________使用int()将其他类型转化为int类型__________________________")
s1 = "128"
s2 = "78.99"
s3 = "Hello"
f = 87.99
bo = True
print(type(s1), type(s2), type(s3), type(f), type(bo))
print(int(s1), type(int(s1)))
# print(int(s2), type(int(s2))) 小数型的字符串不能转化
print(int(f), type(int(f)))
print(int(bo), type(int(bo)))
# print(int(s3), type(int(s3))) 将str转化为int类型是str必须为整数数字串，否则报错
print("______________________用float()将其他类型转化为float类型________________________")
s1 = "128.88"
s2 = "78"
s3 = "Hello"
i = 87
bo = True
print(type(s1), type(s2), type(s3), type(i), type(bo))
print(float(s1), type(float(s1)))
print(float(s2), type(float(s2)))
print(float(f), type(float(f)))
print(float(bo), type(float(bo)))
# print(float(s3), type(float(s3))) 非数字类型的字符型不能转化
