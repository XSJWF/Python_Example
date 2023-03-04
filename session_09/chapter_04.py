# 开发人员：DYL
# 开发时间：2022/10/7 20:53

# 异常：java差不多
try:
    1 / 0
except ZeroDivisionError as e:
    print(e)
# try:
#     520 + "dad"
# except ZeroDivisionError:
#     print("出错了")

try:
    1 / 0
    530 + "da"
except (ZeroDivisionError, TypeError, ValueError):
    pass
# 用except子句单独处理每一个异常
try:
    1 / 0
    530 + "da"
except ZeroDivisionError:
    print("除数不能为0")
except TypeError:
    print("字符串不能和数字直接相加")

# try-except-else:当try语句中没有检测出异常就会执行else中的内容
try:
    1 / 1
except ZeroDivisionError as e:
    print(e)
else:
    print("没有捕获到异常")

# try-except-finally：无论是否检测到异常都会执行finally
try:
    1 / 0
except ZeroDivisionError as e:
    print(e)
else:
    print("没有捕获到异常")
finally:
    print("我咋样都会执行")

# 综合
try:
    f = open("test.txt", "w")
    f.write("猪猪猪猪猪猪")
except:
    print("出错了")
finally:
    f.close()

# try-finally
# try:
#     while True:
#         pass
# finally:
#     print("死循环")

# 异常嵌套
try:
    try:
        520 + "dad"
    except:
        print("内部异常")
    1 / 0
except:
    print("外部异常")
finally:
    print("收尾结束！")

# raise语句，主动引发异常
# raise ValueError("值不正确")  # 类似java自定义异常，但是异常名必须是已经存在的
# 异常链
# raise ValueError("大傻逼") from ZeroDivisionError

# assert语句也是主动引发异常，只不过它只能引发一个AssertionError的异常，用来调试某些地方很方便
s = "sds"
assert s == "sds"  # 类似于if语句成立的话就不会抛出异常，不成立就会抛出异常
# assert s != "sds"
# assert s == "sss"

