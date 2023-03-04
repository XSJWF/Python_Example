# 开发人员：DYL
# 开发时间：2022/6/16 16:55

# 字符串中的查找方法

# index()查找字符串中某个子字符串第一次出现的位置，如果不存在则会抛出ValueError
# rindex()查找子字符串最后一次出现的位置，不存在则会抛出ValueError
# find()查找子字符串第一次出现的位置，不存在则返回-1
# rfind()查找子字符串最后一次出现的位置，不存在则返回-1
s = "hello,hello"
print(s.index("lo"))
print(s.find("lo"))
print(s.rindex("lo"))
print(s.rfind("lo"))

# print(s.index("k"))
# print(s.rindex("k"))  # 因为k不存在，所以会抛出异常
print(s.find("k"))  # k不存在所以返回-1，但是不会抛出异常，所以建议在查找时建议使用find()方法
print(s.rfind("k"))

# 字符串中的常用操作

# 大小写转换
# upper()方法可以把字符串中所有的字符都转换成大写字母
# lower()方法可以把字符串中所有的字符都转换成小写字母
# capitalize()方法可以把第一个字符转换为大写的，其余字符转换成小写
# title()把每一个单词的第一个字符转换成大写，把每一个单词的剩余字符转换成小写
