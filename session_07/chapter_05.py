# 开发人员：DYL
# 开发时间：2022/9/18 21:00

"""
字符串函数操作，由内嵌函数也有对象方法的;内嵌函数就是可以直接拿来用的，就像求一个字符串或者某个对象的长度的函数len()一样，
例：text = "abcdefg" len(text) = 7;可以直接拿来用，而对象方法通俗来说就是点(.)出来的，例：字符串大写函数方法：
text = "abcdefg"，text.upper() = "ABCDEFG"
"""

# len(),作用计算字符串或者一些存储对象（列表等）的长度，返回值是长度（整型）
text = "abcde"
print(len(text))
text = [1, 2, 3, 4, 5, 6]
print(len(text))
# find(self,sub,start,end),self通常可省略，查找子串的索引下标，sub就是需要检索的子串，start检索的起始位置（可省略，默认为0），
# end就是检索的结束位置（可省略，默认为字符串的末尾也即是len(str)）,返回值是检索到的子串下标，找不到的话就返回-1；
text = "abcdefghijkefg"
print(text.find("efg"))  # 从左往右找，找到一个立即停止，如果后面有重复的，也只会返回第一个找到的位置
print(text.find("ok"))
# rfind(self,sub,start,end)唯一和find()不同的就是它是从右往左查找的；
print(text.rfind("efg"))
# index(self,sub,start,end),也是用来查子串的索引，和上面基本相同的用法，不同的是，如果找不到子串会直接抛出一个异常
print(text.index("efg"))
# print(text.index("ok"))
# rindex(self,sub,start,end),和index差不多，不过是从右往左找，自行验证，我就不写了
# count(self,sub,start,end),用法和上面差不多，查找子串出现的次数；
print(text.count("f"))

# 字符串的转换操作
# replace(self,old,new,count)，old表示旧字符串，new表示替换后的新字符串，count表示替换的个数（不写的话默认替换全部）
# replace()不会修改字符串本身，如需保存，需用一个变量来保存替换后的字符串
text = "jshdoanncaoh"
print(text.replace('a', 'o'))  # 这里就把字符串中的a全部变成o了
print(text)
print(text.replace('h', 'i', 1))  # 这里就把字符串中的第一个h换成了i
# capitalize(),就是将自己的本身字符串的首字母变大写，也不会改变字符串本身，如需保存，需用变量接收
print(text.capitalize())
print(text)
# title(),将字符串中每个单词(只要不是字母统统都算分隔符，而分隔符隔开的就算是两个单词)的首字母大写，也同样不会改变字符串本身
text = "dad dfw few peo%tre"
print(text.title())
print(text)
# lower()，将字符串中的每个字符都变成小写，也不会改变字符串本身
text = "HDKSINDSKS"
print(text.lower())
print(text)
# upper(),将字符串中的每个字符都变成大写，也不改变字符串本身
text = "secondhand"
print(text.upper())
print(text)

# ljust(width,fillchar),原字符串在左边，填充的字符串(只能是一个字符)在右边,width就是填充后的字符串总长度，如果你设置为和现在的字符串一样长，则不会填充；填充操作不会修改字符串本身
text = "data"
print(text.ljust(4, "w"))
print(text.ljust(8, "o"))
print(text)
# rjust(width，fillchar)，原字符串在右边，填充的字符串(只能是一个字符)在左边,用法和ljust()一样
print(text.rjust(6, "u"))
print(text)
# center(width,fillchar),原字符串在中间，填充的在两边(如果填充位置不够左右平分，则优先填充在原字符串的左边)，其余和左右填充差不多
print(text.center(9, "w"))
print(text.center(8, "K"))
print(text)

# lstrip(chars),移除字符串左边(从左边开始移除)的chars字符集,遇到不属于chars字符集中的字符停止，可以自行测试多种情况来理解，chars可以不写（不写的话默认移除字符串左侧的空格），不会修改原字符串
text = "  dsj fhs ifm  "
print(text.lstrip())
text = "dad dad wd ds"
print(text.lstrip('da'))
# rstrip(chars),从左边移除，其他用法和lstrip()差不多，这里就不演示了；

# spilt(sep,maxsplit),sep是分隔符，maxsplit是最大分割次数（省略不写的话就有多少分割多少），返回值是分割后的子串所组成的列表,同样不会修改原字符串
text = "nin-ing-guh-idj"
print(text.split("-"))
print(text)
text = "安都会，大的打底我，对我的，单位我，大幅度发个"
print(text.split("，", 3))
print(text)
# partition(sep),把字符串分成三部分（分隔符左边的，分隔符，分隔符邮编的），以搜索（默认从左开始搜索）到的第一个分隔符为标准，返回值是元组类型的，同样不会修改原字符串
print(text.partition("，"))
print(text)
# rpartition(sep),就是从右边开始搜索分隔符，其他的和上面一样；
print(text.rpartition("，"))
print(text)

# splitlines(keepends),keepends（TRUE or False）表示是否保留换行符(默认False)，返回值是被换行符分割的多个字符串所组成的列表，也不会修改原字符串
text = "da \n dwd \n faj"
print(text.splitlines(True))
# join(iterable),根据指定字符串来拼接可迭代对象，得到拼接后的字符，也不会修改原来的字符串
text = ["dabjda", "dahife", "iwusj"]
print("，".join(text))
print(text)

# isalpha()，用来判定字符串中是否所有的字符都是字母，返回结果True或者False
text = "zhi"
print(text.isalpha())
text = "zhi4"
print(text.isalpha())
# isdigit(),用来判定字符串中是否所有的字符都是数字，结果同样返回True或者False
text = "827382"
print(text.isdigit())
text = "19739qw"
print(text.isdigit())
# isalnum()，用来判断字符串中是否所有的字符都是数字或字母，结果返回True或者False
text = "131ads"
print(text.isalnum())
text = "13qwe,？"
print(text.isalnum())
# isspace()，用来判断是都所有的字符都是空白符(包括空格、缩进、换行等不可见转义符)，返回时也是True或者False
text = " \n"
print(text.isspace())
text = " \n ds"
print(text.isspace())
# startwith(prefix,start-0,end-len(str)),判定字符串是否以某个字符开头，prefix表示需要判定的前缀字符串，start表示起始位置，end表示截止位置
# 起始位置不写默认就是0，结束位置不写默认就是字符串的长度，返回值也是True或者False
text = "dad ioi js lsj"
print(text.startswith("d"))
print(text.startswith(" ", 3))
# endwith(prefix,start-0,end-len(str))，判断是否以某个字符串结尾
print(text.endswith("i", 2, 5))

# in、not in，判断一个字符串是否被另一个字符串包含，返回值True或者False
print("1238" in "1234545")
print("1234" in "1234567")
print("12" not in "7879")
print("12" not in "1233445")
