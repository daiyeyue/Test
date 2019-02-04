# 继承中的构造函数 - 3

class Animel():
    def __init__(self):
        print("Animel")


class PaxingAni(Animel):
    def __init__(self, name):
        print(" Paxing Dongwu {0}".format(name))


class Dog(PaxingAni):
    # __init__就是构造函数
    # 每次实例化的时候，第一个被自动的调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print("I am init in dog")


# 实例化Dog时，查找到Dog的构造函数，参数匹配，不报错
d = Dog()


class Cat(PaxingAni):
    pass


# 此时，由于Cat没有构造函数，则向上查找
#  因为PaxingAni的构造函数需要两个参数，实例化的时候给了一个，报错
#c = Cat()
c = Cat("d")