# # Question 1

# class CreditCard:

#     def __init__(self, card_number, expiration_date, security_code):
#         self.card_number = card_number
#         self.expiration_date = expiration_date
#         self.security_code = security_code

#     def __str__(self) -> str:
#         return f"\nCard Number: {self.card_number}\n\nExpiration Date: {self.expiration_date}\n\nSecurity Code: {self.security_code}\n"

# d = CreditCard(123654789098, '02/30', 367)
# print(d)


# # Question 2

# class Animal:
#     kingdom = 'I am a mamal'

#     def __init__(self, name, age, weight) -> None:
#         self.name = name
#         self.age = age
#         self.weight = weight
    
#     def __repr__(self) -> str:
#         return f"Hey! I am {self.name}. I am {self.age}, and I weigh {self.weight} kgs.\n"


# class Dog(Animal):
#     def __init__(self, name, age, weight) -> None:
#         super().__init__(name, age, weight)
        
#     def bark(self):
#         return "WOO WOO" 


# d = Dog('Chris', 15, 22)
# print(d)
        
# # Question 3

# class Queue:
#     identity = 'This is my Queue'
#     def __init__(self) -> None:
#         self.my_queue = []
    
#     def push(self, item):
#         self.my_queue.append(item)
#         return self.my_queue

#     def pop(self):
#         if len(self.my_queue) > 0:
#             self.my_queue.pop(0)
#         return self.my_queue

#     def size(self):
#         return len(self.my_queue)

# s = Queue()

# print(s.push(1))
# print(s.push('one'))
# print(s.push(2))
# print(s.push('two'))
# print(s.push(3))
# print(s.push('three'))
# print()
# print(s.pop())
# print()
# print(s.size())
        
# Question 4

from turtle import color


class Stack:
    identity = 'This is my Stack'
    def __init__(self) -> None:
        self.my_stack = list()

    def push(self, element):
        self.my_stack.append(element)
        return self.my_stack

    def pop(self):
        if len(self.my_stack) > 0:
            self.my_stack.pop()
        return self.my_stack

    def size(self):
        return len(self.my_stack)

s = Stack()
print(s.push(1))
print(s.push('one'))
print(s.push(2))
print(s.push('two'))
print(s.push(3))
print(s.push('three'))
print()
print(s.pop())
print()
print(s.size())

# Question 5

class Person:
    info = 'About me.'
    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address
    
    def __str__(self) -> str:
        return f"My name is {self.name}. I have {self.age} years. I stay in {self.address}."

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def work(self):
        return f"{self.name} is working."

d = Person('Tom', 23, 'Kampala')
print()
print(d)
print()
print(d.eat())
print()
print(d.sleep())
print()
print(d.work())
print()

# Question 6

class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def work(self):
        return f"{self.name} is working."

class Programmer(Employee):
    def __init__(self, name, age, salary, programming_language) -> None:
        super().__init__(name, age, salary)
        self.programming_language = programming_language

    def code(self):
        return f"{self.name} is coding in {self.programming_language}."


d = Programmer('Charles', 23, 600000, 'Python')
print()
print(d.eat())
print()
print(d.sleep())
print()
print(d.work())
print()
print(d.code())

# Question 7

class Vehicle:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"{self.make} {self.model} {self.year} is starting."

    def stop(self):
        return f"{self.make} {self.model} {self.year} is stopping."

    def drive(self):
        return f"{self.make} {self.model} {self.year} is driving."


class Car(Vehicle):
    def __init__(self, make, model, year, color) -> None:
        super().__init__(make, model, year)
        self.color = color

    def park(self):
        return f"The {self.color} {self.make} {self.model} {self.year} is parking."

d = Car('Toyota', 'RAV4', 2022, 'Red')
print()
print(d.start())
print()
print(d.stop())
print()
print(d.drive())
print()
print(d.park())

# Question 8

class Animal:
    kingdom = 'I am a mamal'

    def __init__(self, name, color, age) -> None:
        self.name = name
        self.color = color
        self.age = age
    
    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def make_sound(self):
        return f"{self.name} is making sound."



class Dog(Animal):
    def __init__(self, name, color, age, breed) -> None:
        super().__init__(name, color, age)
        self.breed = breed
    def bark(self):
        return f"{self.name} is barking." 


d = Dog('Jimmy', 'Brown', 5, 'Hybrid')
print()
print(d.eat())
print()
print(d.sleep())
print()
print(d.make_sound())
print()
print(d.bark())