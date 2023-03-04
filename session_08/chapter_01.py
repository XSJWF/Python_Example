# 开发人员：DYL
# 开发时间：2022/9/25 8:31

# 获取当前时间的时间戳，会精确到秒
import time

re = time.time()  # 这样得到的结果是从70年1月一日0时0分到现在过的秒数
print(re)

# 时间元组的获取
# import time
re = time.localtime()
print(re)

# 获取格式化时间
# 把时间戳转换成可读时间
# import time
re = time.time()
re = time.ctime(re)
print(re)

# 把时间元组转化成可读时间
# import time
re = time.localtime()
re = time.asctime(re)
print(re)

# 格式化日期字符串
re = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(re)
# %Y表示四位数的年份、%y表示两位数的年份、%m表示月份、%H表示二十四小时制的小时数，%I表示12小时制的小时数
# %M表示分钟数，%S表示秒，%a表示本地简化星期名称，%A表示完整星期名称,%b表示本地简化月份名称，%B表示本地完整月份名称
# %c表示本地相应的日期表示和时间表示

# 将格式化日期转化为字符串
re = time.strptime("2022-9-29 14:10:13", "%Y-%m-%d %H:%M:%S")
print(re)  # 函数前后的格式一定要严格的对应

# 字符串日期转化为时间元组
re = time.mktime(re)
print(re)

# 获取当前CPU时间
# time.process_time(),获取CPU的执行时间（也就是程序运行时间）不包括sleep()的时间
# time.perf_counter(),获取CPU的执行时间，包括sleep()的时间
start = time.perf_counter()
for i in range(101):
    print(i)
time.sleep(1)
end1 = time.process_time()
end2 = time.perf_counter()
print(end2 - start)
print(end1)

# 获取日历的操作
import calendar

print(calendar.month(2022, 9))

# datatime模块处理日期和时间的标准库
# 获取当前的日期
import datetime
print(datetime.datetime.now())
print(datetime.datetime.today())
