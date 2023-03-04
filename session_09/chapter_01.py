# 开发人员：DYL
# 开发时间：2022/10/5 15:52

# 永久存储，参数基本和C语言创建或者打开文件差不多

# open(file,mode)打开文件,没有的话就自动创建,file就是文件的路径，mode就是文件的打开方式，和C语言都差不多；
file = open("test.txt", 'w')
file.write("大傻逼")  # 将字符串写入到文件对象中，并且返回写入的字符数量（也就是字符串的长度）
file.writelines(["大聪明\n", "二百五"])  # 将一系列的字符串写入到文件对象中（不会自动添加换行符，所以通常是人为地在每个字符串的末尾加换行符）
file.close()  # 关闭文件对象
file = open("test.txt", "r+")
print(file.readable())  # 查看文件是否可读
print(file.writable())  # 查看文件是否可写
for each in file:
    print(each)  # 遍历文件内容输出，文件对象也是一个可迭代的对象
print(file.read())  # 输出为空，因为上一步已经把文件读到最后，文件指针指向了最后面
print(file.tell())  # 查看文件指针的位置
file.seek(0)  # 将文件指针放在文件的开头
print(file.readline())  # 读取一行的内容
print(file.tell())
print(file.read())  # 就是读取到EOF的位置
file.write("I love 肥肥")
file.flush()  # 可以在不关闭文件的情况下就把内容写入到文件中（即刷新缓存区），因为如果不关闭文件的话，写入的内容一般都在缓存流中，关闭了文件才会真正写入
# 但是用pycharm就不用管这个，因为好像会自动调用这个方法，反正不需要关闭也不需要调用这个方法内容还是会直接存到文件中。
# truncate(pos=None,/)，将文件对象截取到pos的位置，不指定pos的话默认截取到文件指针当前指定的位置
print(file.truncate(10))  # 使用单独的写入模式"w"也会出现截断的情况
file = open("test.txt", "w")  # 会发现文件内容清空了,用“w”来写的这种情况就是覆盖写

