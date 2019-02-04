# 继承的语法
# 在python中，任何类都有一个共同的父类叫object

class Person():
    name = "NoName"
    age = 18
    __score = 0  # 考试成绩是秘密，只要自己知道
    _petname = "sec"  # 小名，是保护的，子类可以用，但不能公用

    def sleep(self):
        print("Sleeping ... ...")



# 父类写在括号内
class Teacher(Person):

    teacher_id = "9527"

    def make_test(self):
        print("attention")


t = Teacher()
print(t.name)
# 受保护不能外部访问，为啥这里可以
print(t._petname)

# 私有访问问题
# 公开访问私有变量，报错
#print(t.__score)
#print(Teacher.__dict__)
print(t._Person__score)

t.sleep()
print(t.teacher_id)
t.make_test()
print(Person.__dict__)




