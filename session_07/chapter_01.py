# 开发人员：DYL
# 开发时间：2022/6/16 15:15

# 字符串是一个不可变序列
# 字符串的驻留机制

a = 'Python'
b = "Python"
c = '''Python'''
print(id(a))
print(id(b))
print(id(c))
# 三个变量的id是一样的因为字符串的驻留机制，仅保存一份相同且不可变的字符串的方法，不同的值被存放在字符串的驻留池中，
# Python的驻留机制对相同的字符串只保留一份拷贝，后续创建相同字符串时，不会开辟新空间，而是把该字符串的地址赋给新创建的变量
# 可以用对象的思维来理解他，即一开始创建一个对象赋值给一个变量，后面所有变量创建后赋的相同的值都是这个对象，即对象只有一个，但可以多个变量指向它

# 当字符串的长度为0或者1的时候,或者符合标识符的字符串(字符串只在编译时进行驻留，而不是运行时),或者[-5,256]之间的数字有驻留
# 驻留机制的这几种情况都只出现在原生的PythonIDE，因为pycharm对字符串做了优化所以驻留体现不出来，可以把下面的代码拿到Python的原生IDE下去运行
# 也可以直接在最下方的Python控制台运行效果一样
# s1 = ""
# s2 = ''
# s1 is s2  # True
# s1 = '%'
# s2 = '%'
# s1 is s2  # True
#
# s1 = "abc%"
# s2 = "abc%"  # "abc%"不符合标识符的字符串(只有字母、数字、下划线)长度又超过1了，所以不会出现驻留
# s1 == s2  # True
# s1 is s2  # False
# id(s1)
# id(s2)
#
# s1 = 'abcx'
# s2 = 'abcx'  # 此时"abcx"是符合标识符的，所有有驻留
# s1 == s2  # True
# s1 is s2  # True
# id(s1)
# id(s2)
#
# a = "abc"
# b = "ab" + "c"
# c = "".join(["ab","c"])
# a is b  # True  a、b在程序运行前就是一样的了，即b在程序运行前就连接完成了，所以a、b有驻留
# a is c  # False  c的方法是需要程序在运行时才调用，所以说驻留只在编译时有，而非程序运行时

# 强制驻留
# import sys
# a = "abc%"
# a = "abc%"
# a = sys.intern(b)
# a is b  #True

# 字符串驻留机制的优缺点：当需要值相同的字符串时，可以直接从字符串池里拿出来用，避免频繁地创建和销毁，提升效率节约内存，
# 因此拼接字符串和修改字符串是比较影响性能的
# 在需要进行字符串拼接时建议使用str类型的join方法，而非'+'，因为join()方法是先计算出所有字符中的长度，然后拷贝，
# 只会new一次对象，效率要比'+'效率高