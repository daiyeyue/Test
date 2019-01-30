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