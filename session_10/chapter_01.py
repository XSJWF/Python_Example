# 开发人员：DYL
# 开发时间：2022/10/7 21:35

# 类和对象，基本理念和java的面向对象差不多

# 封装
class Tsy:
    head = 1
    eyes = 2
    legs = 4
    shell = True

    def crawl(self):
        print("啥打开大家")

    def run(self):
        print("二百五")

    def eat(self):
        print("吃粑粑")

    def sleep(self):
        print("睡觉觉")

    def get_self(self):
        print(self)


t1 = Tsy()
print(t1.head)
print(t1.legs)
print(t1.shell)
t1.crawl()
t1.sleep()
t1.eat()
t2 = Tsy()
print(t1.get_self())
print(t1)
print(t2.get_self())
print(t2)
