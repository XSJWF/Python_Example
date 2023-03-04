# 开发人员：DYL
# 开发时间：2022/10/4 9:07
from typing import Dict


# 函数文档、类型注释、内省

# 函数文档
def exchange(dollar, rate=7.11):
    """
    function:汇率转换，美元->人民币
    :param dollar:美元数量
    :param rate:汇率，默认值是7.11（2022-10-04）
    :return:人民币的数量
    """
    return dollar * rate


print(exchange(20))
help(exchange)


# 类型注释，冒号后的就是希望传入的参数值的类型，箭头后面的就是希望返回的类型，当然如果实际传入的参数和它们不一致，也没关系
# 因为这是给人看到的，并不是给机器看的，所以不影响
def times(s: str, n: int) -> str:
    return s * n


print(times("DYL", 5))
print(times(5, 5))


def times(s: str = "kki", n: int = 4) -> str:
    return s * n


print(times())


def times(s: list, n: int = 4) -> list:
    return s * n


print(times([9, 8, 7]))


def times(s: Dict[str, int], n: int = 3) -> list:
    return list(s.keys()) * n


print(times({'A': 1, 'B': 2, 'C': 3}))

# 内省
print(times.__name__)
print(times.__annotations__)
print(exchange.__doc__)
