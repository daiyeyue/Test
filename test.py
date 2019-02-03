# 集合的定义
s = set()
print(type(s))
print(s)

# 此时，大括号内一定要有值，否则定义出的是一个dict
s = {2,1,3,4,8,6,7}
print(s)

# 如果只是用大括号定义，则定义的是一个dict类型
d = {}
print(type(d))
print(d)

s = {[1,2,3], ["i", "love", "wangxiaojing"], [4,5,6]}
print(s)
for k, m, n in s:
    print(k, "--", m, "--", n)

for k in s:
    print(k)

# copy:拷贝
# remove:移除制定的值，直接改变原有值，如果要删除的值不存在，报错
# discard:移除集合中指定的值，跟ｒｅｍｖｏｅ一样，但是入股要删除的话，不报错
s = {23,3,4,5,1,2,3}
s.remove(4)
print(s)
s.discard(1)
print(s)

print("*" * 20)
s.discard(1100)
print(s)

s.remove(1100)
print(s)

# 集合函数
# intersection: 交集
# difference:差集
# union: 并集
# issubset: 检查一个集合是否为另一个子集
# issuperset: 检查一个集合是否为另一个超集
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}

s_1 = s1.intersection(s2)
print(s_1)

s_2 = s1.difference(s2)
print(s_2)

s_3 = s1.issubset(s2)
print(s_3)

# 字典的创建
# 创建空字典1
d = {}
print(type(d))
print(d)

# 创建空字典2
d = dict()
print(d)


# 创建有值的字典， 每一组数据用冒号隔开， 每一对键值对用逗号隔开
d = {"one":1, "two":2, "three":3}
print(d)

# 用dict创建有内容字典1
d = dict({"one":1, "two":2, "three":3})
print(d)

# 用dict创建有内容字典2
# 利用关键字参数
d = dict(one=1, two=2, three=3)
print(d)

dict()


# 通用函数： len, max, min, dict
# str(字典): 返回字典的字符串格式
d = {"one":1, "two":2, "three":3}
print(d)
print(str(d))

#
d = dict( [("one",1), ("two",2), ("three",3)])
print(d)

d = {"one":1, "two":2, "three":3}
i = d
print(type(i))
i = d.items()
print(type(i))
print(i)

from collections import Iterable
print(isinstance({'dede':123},Iterable))
print(isinstance((1,2,3),Iterable) )

d = {"one":1, "two":2, "three":3}
print(d.get("on333"))

# get默认值是None，可以设置
print(d.get("one", 100))
print(d.get("one333", 100))

#体会以下代码跟上面代码的区别
print(d['on333'])