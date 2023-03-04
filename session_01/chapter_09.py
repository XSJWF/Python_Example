# 开发人员：DYL
# 开发时间：2022/3/26 16:14
from decimal import Decimal

a = 3.14159
print(type(a))
n1 = 1.1
n2 = 2.2
print(Decimal("1.1") + Decimal("2.2"))  # 计算机是采用二进制存储的，所以计算浮点型会有误差
# 通过导入 Decimal模块可以解决
