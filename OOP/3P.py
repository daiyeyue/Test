class Person():
    # name是共有的成员
    name = "liuying"
    # __age就是私有成员
    __age = 18

p = Person()
print(p.name)
print(Person.__dict__)
print(p._Person__age)