# 开发人员：DYL
# 开发时间：2022/10/7 10:52

# 由于Windows操作系统的特殊性，它的文件路径中使用反斜杠("\")来分割路径，而其他操作系统都是用斜杠("/")来分割的
# 所以在Windows下使用路径的时候，因为Python里面反斜杠是转义符，所以在写路径的时候需要再写一个反斜杠来转义路径中的反斜杠

# pathlib -- 面向对象的文件系统路径，可以让文件和路径操作变得更快更方便
from pathlib import Path
print(Path.cwd())  # cwd()方法可以获取当前工作目录的路径
p = Path(Path.cwd())
print(p)
q = p / "test.txt"  # 可以直接利用'/'来对路径进行拼接
print(q)
print(p.is_dir())  # isdir()，判断是否是一个文件夹
print(q.is_dir())
print(q.is_file())  # is_file()，判断是否是一个文件
print(p.is_file())
print(p.exists())  # exists()，判断路径是否存在
print(q.exists())
print(Path("saa").exists())
print(p.name)  # 使用name属性获取路径尾部最后一项的名字
print(q.name)
print(p.stem)  # 用stem属性来获取文件的文件名
print(q.stem)
print(p.suffix)  # 用suffix属性获取文件的后缀名
print(q.suffix)
print(p.parent)  # 用parent属性来获取父级目录
print(q.parent)
print(p.parents)  # 用parents属性来获取逻辑祖先路径构成的不可变序列(可迭代对象)
for i in p.parents:
    print(i)
print(p.parents[0], "\n", p.parents[1])
print(p.parts)  # parts属性，将路径拆分成元组储存起来
print(p.stat())  # stat()方法，查询文件或文件夹的信息
print(p.stat().st_size)  # 大小
print(q.stat().st_size)
print(Path("./test.txt").resolve())  # resolve()，将相对路径转化成绝对路径
print(p.iterdir())  # iterdir()，获取当前路径下的所有子文件和子文件夹，是一个生成器
for each in p.iterdir():
    print(each)
print([x for x in p.iterdir() if x.is_file()])  # 利用列表推导式，将p路径下面的所有文件夹添加到列表

n = p / "t2"  # mkdir(),创建一个文件夹
# n.mkdir()  # 如果创建的目录已经存在，机会报错，所以，我们就尽量用exit_ok来忽略
n.mkdir(exist_ok=True)
n = p / "t2/a/b/c"
n.mkdir(exist_ok=True, parents=True)  # 如果创建的目录的父级目录不存在，那就可以用parents来忽略
n = p / "test.txt"
f = n.open("w")  # 和open()函数的用法差不多
f.write("I love 肥肥")
f.close()
n = p / "t2/a/b/c"

n.rmdir()  # rmdir()，删除文件夹，删除的时候目录必须为空
n = q
# n.unlink  # unlink()，删除文件
p = Path(".")
print(p.glob("*.txt"))  # glob()，查找文件，*是通配符，是所有的意思，这里就是所有.txt后缀的文件
print(list(p.glob("*.txt")))
print(list(p.glob("**/*.py")))  # 查找当前目录以及其子目录下面所有的.py文件

