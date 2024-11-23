import inspect
class Person:
    name: str
    surname: str
    age: int
    pensione: bool
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.set_pensione(self.age)
    def set_pensione(self, value: int):
        if value >= 60:
            self.pensione = True
        else:
            self.pensione = False
    def info_person(self):
        print(f'person:\t{self.name} | {self.surname} | {self.age}')
class Group:
    nameGroup: str
    Quantity: int
    age: int
    Students: list
    def __init__(self, nameGroup: str, Quantity: int, age: int, Students: list ):
        self.nameGroup = nameGroup
        self.Quantity = Quantity
        self.age = age
        self.Students = Students
    def info_all(self):
        print("----------------------Повна інформація по групі:")
        print(f'Group: {self.nameGroup} | {self.Quantity} | {self.age}')
class Student(Person):
    progress: str
    group: str
    def __init__(self, progress: str, group: str, name: str, surname: str, age: int):
         self.progress = progress
         self.group = group
         Person.__init__(self, name=name, surname=surname, age=age)
         super().set_pensione(self.age)
class Worker(Person):
    position: str
    duties: str
    def __init__(self, position: str, duties: str, name: str, surname: str, age: int):
        self.position = position
        self.duties = duties
        Person.__init__(self, name=name, surname=surname, age=age)
        super().set_pensione(self.age)
# personX = Person(name='unknown_name', surname='unknown_surname', age=30)
# personX.info_person()
class Teacher(Person):
    position: str
    duties: str
    def __init__(self, subject: str, hours: int, name: str, surname: str, age: int):
        self.subject = subject
        self.hours = hours
        Person.__init__(self, name=name, surname=surname, age=age)
    def info_teacher(self):
        print(f'teacher:\t{self.subject} | {self.hours}')
    def info_all(self):
        self.info_person()
        self.info_teacher()
# teacher = Teacher(subject='Pycharm', hours=24, name='unknown_name', surname='unknown_surname', age=30)
# teacher.info_all()
# nameGroup = input("Введіть назву групи:")
# age = int(input("Введіть вікову категорію:"))
# mStudents = []
# for x in range(1, 4):
#     nameSt = input("Введіть ім'я студента №"+str(x)+":")
#     surname = input("Введіть призвище студента №"+str(x)+":")
#     progress = input("Введіть успішність (добре, погано, інше) "+str(x)+":")
#     student = Student(progress=progress, group=nameGroup, name=nameSt, surname=surname, age=age)
#     mStudents.append(student)
# Quantity = len(mStudents)
# group = Group(nameGroup=nameGroup, Quantity=Quantity, age=age, Students=mStudents)
# group.info_all()

# for method in dir(Student):
#     print(method)
mClass = [Student, Worker]
for vClass in mClass:
    print(f'######### \t{vClass} parameters')
    sig = inspect.signature(vClass)
    for parameter in sig.parameters.values():
        print(parameter.name)
    print(f'######### {vClass} | methods')
    for method in dir(vClass):
        print(method)

# print("######### Student | parameters")
# sig = inspect.signature(Student)
# for parameter in sig.parameters.values():
#     print(parameter.name)
# print("######### Student | methods")
# for method in dir(Student):
#     print(method)
# print("######### Worker | parameters")
# sig = inspect.signature(Worker)
# for parameter in sig.parameters.values():
#     print(parameter.name)
# print("######### Worker | methods")
# for method in dir(Worker):
#     print(method)
