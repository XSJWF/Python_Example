# 开发人员：DYL
# 开发时间：2022/3/26 15:37

# 转义字符

print("Hello\nWorld")

print("Hello\tWorld")

print("Helloooo\tWorld")

print("Hello\rWorld")  # "\r"后面的将前面的覆盖

print("Hello\bWorld")  # "\b"是退一格

print("https://www.baidu.com")

print("老师说：\"大家好！\"")

# 原字符 ，就是不希望转义字符生效，就是在字符串前加一个r或者R
print(R"Hello\nWorld")
# 注意：字符串的最后一个字符不能是反斜杠
# print(r"Helle\nWorld\")
print(r"Helle\nWorld\\")
