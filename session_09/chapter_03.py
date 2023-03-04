# 开发人员：DYL
# 开发时间：2022/10/7 20:21

# with语句和上下文管理器
with open("test.txt", "w") as f:
    f.write("I always love 肥肥")

# 不需要手动关闭文件更方便

# 将python对象序列化
import pickle

x, y, z = 1, 2, 3
s = "dfs"
a = ["ada", 22, 4.33]
d = {"1": "傻逼", "2": "大傻逼"}
with open("test.pkl", "wb") as f:
    pickle.dump([x, y, z, s, a, d], f)  # 使用dump()，将文件以二进制的形式存到文件中,多个对象可以用元组也可以用列表的方式

with open("test.pkl", "rb") as f:
    x, y, z, s, a, d = pickle.load(f)
print(x, y, z, s, a, d, sep="\n")
