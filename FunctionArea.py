'''
def fun():
    global b1
    b1 = 100
    print(b1)
    print("I am in fun")
    # a2的作用范围是fun
    b2 = 99
    print(b2)

#print(b1)
fun()
print(b1)
'''


a = 1
b = 2
def fun(c, d):
    e = 111
    print("Locals={0}".format(locals()))
    print("Globals={0}".format(globals()))


fun(100, 200)

# exec示例
x = 100
y = 200
# 执行x+y
# z = x + y
z1 = x + y
# 1, 注意字符串中引号的写法
# 2. 比对exec执行结果和代码执行结果
#z3 = exec("print('x+y:', x+y)")

print(z1)
print(z2)
print(z3)