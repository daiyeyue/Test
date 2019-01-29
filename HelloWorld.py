#!/usr/bin/python
print("Hello, World!");
print("diaoni");
print("1")
print("2")
print("3")

age = 19
if age < 18:
    print("小于18岁");
else:
    print("大于19岁");

gender = input("请输入性别：")
print("你输入的性别是：{0}".format(gender))

if gender == "nan":
    print("来，我们纪念一下今天吧，代码敲十遍");
    print('come on');
else:
    print("发糖喽发糖喽")
    print("你是女生，特殊照顾喽")


print("开始上课喽")

# score  存放学生成绩
# 注意input的返回值类型
score = input("请输入学生成绩：")
# 需要把str转换成int
score = int(score)

if score>=90:
    print("A")
if score>= 80  and score<90:
    print("B")
if score >= 70 and score<80:
    print("C")
if score >=60 and score<70:
    print("D")
if score < 60:
    print("起开，我没你这撒学僧")


for name in  ['zhangsan', 'lisi', 'wangwu','jingjing']:
    print(name)

for name in  ['zhangsan', 'lisi', 'wangwu','jingjing']:
    print(name)
    if name == "jingjing":
        print("我的最爱{0}出现了".format(name))
    else:
        print("同学我们不约，不约，同学请自重")
else:
    print("别的都不是我的学生，不会在爱了")
    print("别的都不是我的学生，不会在爱了")
    print("别的都不是我的学生，不会在爱了")
    print("别的都不是我的学生，不会在爱了")


for i in range(1,11):
    pass
    print("我爱芳芳")


Money = 100000;
Year = 1;
while Money < 100000 * 2:
    Money = Money * 1.067;
    print("第{0}年拿了{1}块钱".format(Year,Money))
    Year = Year + 1;
else:
    print("祝贺拿到{0}钱".format(Money))
