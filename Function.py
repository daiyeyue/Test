def daiye():
    print('我定义的函数')

def fangfang():
    pass;

daiye()

def hello(person):
    print("{0}, 你肿么咧".format(person))
    print("Sir, 你不理额额就走咧")
    #return "daiye"

get  = hello("person");
print(get)

for row in range(1,10):
    # 打印一行
    for col in range(1, row+1):
        # print函数默认任务打印完毕后换行
        #print( row * col, end=" ")
        print(row * col,end="/")
    print("-------------------")

    print(3*4,end="////////////");
    print(3*4);
    print(end=)


for row in range(1,10):
    for col in range(1, row+1):
        print( row * col, end=" ")
    print("")