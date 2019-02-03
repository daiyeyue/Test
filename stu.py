def stu(*args):
    '''
    
    niub
    :param args: 
    :return: 
    '''
    print("哈哈哈哈哈")
    # n 用来表示循环次数
    # 主要用来调试
    n = 0
    for i in args:
        print(type(i))
        print(n)
        n += 1
        print(i)

#stu("liuying", "liuxiaoyhing", 19, 200)
#l = ["liuying", 19, 23, "wangxiaojing"];
l = ["liuying", 19, 23, "wangxiaojing"];
#print(*l)
#stu(*l)
print(help(stu))
print(stu.__doc__)

def fun():
    global b1
    b1 = 100
    print(b1)
    print("I am in fun")
    # a2的作用范围是fun
    b2 = 99
    print(b2)
