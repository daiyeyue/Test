class Student():
    name = "dana"
    age = 18
    # 注意say的写法，参数有一个self
    def say(self):
        #self.name = "aaaa"
        #self.age = 200
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))

yueyue = Student()
yueyue.say()

class Teacher():
    name = "dana"
    age = 19
    def say(self):
        self.name = "yaona"
        self.age = 17
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))
        print(__class__.name)
    def sayAgain():
        print(__class__.name)
        print("nice to see you again")

t =  Teacher()
t.say()
Teacher.sayAgain()