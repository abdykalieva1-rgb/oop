# class Small:
#     def show_size(self):
#         return "Размер Small — компактный и лёгкий."
# class Medium:
#     def show_size(self):
#         return "Размер Medium — стандартный и сбалансированный."
# class Large:
#     def show_size(self):
#         return "Размер Large — просторный и удобный."
# sizes = [Small(), Medium(), Large()]
# for s in sizes:
#     print(s.show_size())
# from numbers import Number


# class Box:
#     def __init__(self,width,heigth,depth):
#         self.width=width
#         self.heigth=heigth
#         self.depth=depth
#     def __str__(self):
#         return f'Box({self.width}x{self.heigth}x{self.depth})'
#     def __eq__(self, other):
#         return (self.width==other.width and self.heigth==other.heigth and self.depth==other.depth)
#
# b1=Box(1,2,3)
# b2=Box(4,5,6)
# b33=Box(7,8,9)
# print(b1)
# print(b1==b2)
# print(b1==b2)


# class Point:
#     def __int__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return f"Point({self.x},{self.y})"
#     def __add__(self,other):
#         return Point(self.x+other.x, self.y+other.y)
#
# p1=Point(2)
# p2=Point(3)
# print(p1+p2)


#
# class Counter:
#     def __init__(self,value):
#         self.value=value
#     def __add__(self,other):
#         return Counter(self.value+other.value)
#     def __eq__(self, other):
#         return self.value==other.value
#     def __str__(self):
#         return f'Counter({self.value})'
#
# c1=Counter(1)
# c2=Counter(2)
#
# print(c1+c2,c1==c2)

# class Name:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return self.name
#     def __eq__(self,other):
#         self.name==other.name
#     def __len__(self):
#         return len (self.name)
#
# n1=Name('Elida')
# n2=Name("Aidan")
# print(n1)
# print(len(n1))
# print(n1==n2)



# class Grade:
#     def __init__(self,grade):
#         self.grade=grade
#     def __eq__(self,other):
#         return self.grade==other.grade
#     def __gt__(self,other):
#         return self.grade>other.grade
#     def __lt__(self,other):
#         return self.grade<other.grade
#
# g1=Grade(4)
# g2=Grade(5)
#
# print(g1==g2)
# print(g1>g2)
# print(g1<g2)
# print(g1)
#




# class MyList:
#     def __init__(self,data):
#         self.data=data
#     def __len__(self):
#         return len(self.data)
#     def __getitem__(self, index):
#         return self.data[index]
#     def __str__(self):
#         return str(self.data)
#
# lst=MyList([1,2,3,4,5])
# print(lst)
# print(len(lst))
# print(lst[2])









#
# class Money:
#     def __init__(self,amount):
#         self.amount=amount
#     def __add__(self, other):
#         return Money(self.amount+other.amount)
#     def __sub__(self,other):
#         return Money(self.amount-other.amount)
#     def __str__(self):
#         return f'{self.amount} com'
#
# m1=Money(100)
# m2=Money(50)
# print(m1+m2)
# print(m1-m2)









# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return f'({self.x},{self.y})'
#     def __add__(self,other):
#         return Point(self.x+other.x,self.y+other.y)
#
# p1=Point(1,2)
# p2=Point(3,4)
# print(p1+p2)








# class Monitor:
#     def __init__(self):
# #         pass
#
#     def on(self):
#         return "Монитор включен"
#
# class Keyboard:
#     def __init__(self):
#         pass
#
#     def type(self):
#          return "клавиатура печатает"
# class Mouse:
#     def __init__(self):
#         pass
#
#     def click(self):
#         return "мышь кликает"
#
# class Computer:
#     def __init__(self,brand):
#         self.brand=brand
#         self.Monitor=Monitor()
#         self.Keyboard=Keyboard()
#         self.Mouse=Mouse()
#
#     def start(self):
#         return f'{self.brand}:компьютер включен'
# #
# # pc=Computer('Lenovo')
# print(pc.start())
# print(pc.Monitor.on())
# print(pc.Keyboard.type())
# print(pc.Mouse.click())







# class Settings:
#     _instance=None
#
#     def __new__(cls,theme='ligth',volume=50):
#         if cls._instance is None:
#             cls._instance = super().__new__ (cls)
#             cls._instance.theme=theme
#             cls._instance.volume=volume
#         return cls._instance
#
# s1=Settings(theme='dark',volume=20)
# s2=Settings()
#
# print(s1 is s2)
# print(s2.theme,s2.volume)
#
# class Settings:
#     _instance = None   # хранит единственный объект
#
#     def __new__(cls, theme="light", volume=50):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.theme = theme
#             cls._instance.volume = volume
#         return cls._instance
#
#
# # Пример
# s1 = Settings(theme="dark", volume=80)
# s2 = Settings()
#
# print(s1 is s2)            # True — один объект
# print(s2.theme,s2.volume)











#
# class Player:
#     def __init__(self, name):
#         self.name = name
# class Team:
#     def __init__(self, name):
#         self.name = name
#         self.players = []
#     def __add__(self, player):
#         self.players.append(player)
#     def __remove__(self, player):
#         self.players.remove(player)
#     def __show__(self):
#         print(f"Команда {self.name}:")
#         for p in self.players:
#             print("-", p.name)
# p1 = Player("Elida")
# p2 = Player("Медер")
#
# team = Team("Орлиные")
# team.__add__(p1)
# team.__add__(p2)
# team.__show__()






#
# class Dog:
#     def speak(self):
#         return "Гав!"
# class Cat:
#     def speak(self):
#         return "Мяу!"
# class Bird:
#     def speak(self):
#         return "Чирик!"
# class AnimalFactory:
#     @staticmethod
#     def create(animal_type):
#         if animal_type == "dog":
#             return Dog()
#         elif animal_type == "cat":
#             return Cat()
#         elif animal_type == "bird":
#             return Bird()
#         else:
#             return None
# animal = AnimalFactory.create("cat",)
# animal1=AnimalFactory.create('dog')
# animal2=AnimalFactory.create('bird')
# print(animal.speak())
# print(animal1.speak())
# print(animal2.speak())

#
#
# class Room:
#     def __init__(self, name):
#         self.name = name
#
#
# class House:
#     def __init__(self):
#         self.rooms =[Room('зал'),[Room('кухня'),[Room('спальня')]]]
#
#     def show(self):
#         for r in self.rooms:
#          print(r.name)
#
#
# home = House()
# home.show()



# class Room:
#     def __init__(self, name):
#         self.name = name
#
# class House:
#     def __init__(self):
# #         self.rooms = [Room("Зал"), Room("Кухня"), Room("Спальня")]
# #
# #     def show(self):
# #         for r in self.rooms:
# #             print(r.name)
# #
# # h = House()
# # h.show()
#
#
# class Subscriber:
#     def __init__(self, name):
#         self.name = name
#
#     def update(self, news):
#         print(f"{self.name} получил новость: {news}")
#
#
# class News:
#     def __init__(self):
#         self.subscribers = []
#
#     def subscribe(self, sub):
#         self.subscribers.append(sub)
#
#     def unsubscribe(self, sub):
#         self.subscribers.remove(sub)
#
#     def publish(self, message):
#         for sub in self.subscribers:
#             sub.update(message)
#
#
# s1 = Subscriber("Алиса")
# s2 = Subscriber("Бек")
#
# news = News()
# news.subscribe(s1)
# news.subscribe(s2)
#
# news.publish("Новое обновление в системе!")



# class Subscriber:
#     def __init__(self, name):
#         self.name = name
#     def update(self,news):
#         print(f'{self.name} получиль новост: {news}')
# class News:
#     def __init__(self):
#         self.subscribers = []
#     def subscribe(self,sub):
#         self.subscribers.append(sub)
#     def unsubscribe(self,sub):
#         self.subscribers.remove(sub)
#     def publish(self, message):
#         for sub in self.subscribers:
#             sub.update(message)
#
# s1=Subscriber('Elida')
# s2=Subscriber('Aidana')
# news=News()
# news.subscribe(s1)
# news.subscribe(s2)
#
# news.publish('Новое обновление в системе!')





















# class Animal:
#     def sound(self):
#         return "Some sound"
# class Dog(Animal):
#     def sound(self):
#         return "Гав!"
# class Cat(Animal):
#     def sound(self):
#         return "Мау!"
# dog = Dog()
# cat = Cat()
#
# print(dog.sound())
# print(cat.sound())





# class Transport:
#     def move(self):
#         return "Moving..."
# class Car(Transport):
#     def move(self):
#         return "Car is driving"
# class Bike(Transport):
#     def move(self):
#         return "Bike is riding"
# car = Car()
# bike = Bike()
#
# print(car.move())
# print(bike.move())






#
#
#
#
# class Shape:
#     def draw(self):
#         return "Drawing shape"
# class Circle(Shape):
#     def draw(self):
#         return "Drawing circle"
# class Square(Shape):
#     def draw(self):
#         return "Drawing square"
# circle = Circle()
# square = Square()
#
# print(circle.draw())
# print(square.draw())








# class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# # class Student(Person):
# #     def study(self):
# #         return f"{self.name} is studying"
# # class Teacher(Person):
# #     def teach(self):
# #         return f"{self.name} is teaching"
# #
# #
# # student = Student("Elida", 18)
# # teacher = Teacher("Maria", 35)
# #
# # print(student.study())
# print(teacher.teach())











#
# class Device:
#     def turn_on(self):
#         return "Device is turning on"
# class Phone(Device):
#     def turn_on(self):
#         return "Phone is turning on"
# class Computer(Device):
#     def turn_on(self):
#         return "Computer is turning on"
# phone = Phone()
# computer = Computer()
#
# print(phone.turn_on())
# print(computer.turn_on())
#
#
#
#
#
#
#
# class Food:
#     def __init__(self, name):
#         self.name = name
# class Fruit(Food):
#     pass
# class Vegetable(Food):
#     pass
#
# apple = Fruit("Apple")
# carrot = Vegetable("Carrot")
#
# print(apple.name)
# print(carrot.name)






#
#
# class Toy:
#     def play(self):
#         return "Playing with toy"
# class Ball(Toy):
#     def play(self):
#         return "Playing with ball"
# class Doll(Toy):
#     def play(self):
#         return "Playing with doll"
#
# ball = Ball()
# doll = Doll()
# print(ball.play())
# print(doll.play())


#

#
#
# class Furniture:
#     def __init__(self, material):
#         self.material = material
# class Chair(Furniture):
#     pass
# class Table(Furniture):
#     pass
# chair = Chair("Wood")
# table = Table("Metal")
#
# print(chair.material)
# print(table.material)
#
# 
#
# class Monitor:
#     def display(self,text):
#         return (f'монитор отображает:',{text})
# class Keyboard:
#     def type(self):
#         return 'клавиатура печатает:'
# class Mouse:
#     def click (self):
#         return 'мышь кликает'
#
# class Computer:
#     def __init__(self,brand):
#         self.brand=brand
#         self.monitor=Monitor()
#         self.keyboard=Keyboard()
#         self.mouse=Mouse()
#
#     def start (self):
#         return f'{self.brand}: компьютер включен'
#
# A=Computer('apple')
# print(A.start())
    


        
        
#
#
#
# students = [
#     {"name": "Алина", "age": 18, "grades": [85, 90, 88]},
#     {"name": "Элида", "age": 19, "grades": [70, 75, 72]},
#     {"name": "Данияр", "age": 18, "grades": [95, 92, 94]}
# ]
#
#
# def calculate_average(students_list):
#     result = []
#     for student in students_list:
#         grades = student["grades"]
#         avg = sum(grades) / len(grades)
#
#         new_student = {
#             "name": student["name"],
#             "age": student["age"],
#             "average": avg
#         }
#         result.append(new_student)
#
#     return result
#
#
# def print_best_students(students_with_avg):
#     for student in students_with_avg:
#         if student["average"] > 80:
#             print(student["name"], "-", student["average"])
#
# students_with_avg = calculate_average(students)
# print_best_students(students_with_avg)












#
#
# # Базовый класс Payment
#
# class Payment:
#     def __init__(self, owner, balance):
#         self.__owner = owner
#         self.__balance = balance
#

#     @property
#     def owner(self):
#         return self.__owner
#
#     @property
#     def balance(self):
#         return self.__balance
#

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"{self.owner}: пополнение на {amount}. Баланс = {self.balance}")
#         else:
#             print("Сумма должна быть положительной.")
#

#     def pay(self, amount):
#         if amount <= 0:
#             print("Ошибка: сумма должна быть положительной.")
#             return False
#
#         if self.__balance >= amount:
#             self.__balance -= amount
#             print(f"{self.owner}: успешно оплачено {amount}. Остаток: {self.balance}")
#             return True
#         else:
#             print(f"{self.owner}: недостаточно средств.")
#             return False
#

#     def info(self):
#         print(f"Владелец: {self.owner}, баланс: {self.balance}")
#
#

# class CardPayment(Payment):
#     def pay(self, amount):
#         commission = amount * 0.02
#         total = amount + commission
#
#         print(f"{self.owner}: комиссия 2% = {commission}")
#
#         return super().pay(total)
#
#

# class MobilePayment(Payment):
#     def pay(self, amount):
#         if amount > 5000:
#             print(f"{self.owner}: отказ — мобильный платёж не может быть > 5000")
#             return False
#
#         commission = amount * 0.01
#         total = amount + commission
#
#         print(f"{self.owner}: комиссия 1% = {commission}")
#
#         return super().pay(total)
#




# class CryptoPayment(Payment):
#     def pay(self, amount):
#         print(f"{self.owner}: анонимная оплата, комиссия = 0")
#         return super().pay(amount)
#
#



# class PaymentManager:
#     def __init__(self):
#         self.payments = []
#
#     def add(self, payment):
#         self.payments.append(payment)
#
#     def process_all(self, amount):
#         print("\n=== Обработка всех платежей ===")
#         for p in self.payments:
#             p.pay(amount)
#



# card = CardPayment("Elida (Карта)", 0)
# mobile = MobilePayment("Aidana (Моб. Платёж)", 0)
# crypto = CryptoPayment("Аlina (Крипто)", 0)
#
# card.deposit(5000)
# mobile.deposit(10000)
# crypto.deposit(10000)
#

# manager = PaymentManager()
# manager.add(card)
# manager.add(mobile)
# manager.add(crypto)
#

# manager.process_all(3000)
#
#












