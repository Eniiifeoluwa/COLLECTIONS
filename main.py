from math import *
number = [1.2, 2, 324, 2]
print(max(number))
matrix = [
    [1, 2, 3,
     4, 5, 6,
     7, 8, 9]]
matrix[0][1] = 20
print(matrix[0])
for row in matrix:
    for column in row:
        print(column)
data = ["Akinola", "17", "20"]
date = ['ayomide', 'Akinola']
for datum in data:
    if datum not in date:
        date.append(datum)
print(date)
phone = input("Phone->  ")
digits_mapping = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four"
}
output = " "
for ph in phone:
    output += digits_mapping.get(int(ph), " ! ") + " "
print(output)
message = input("Enter your mood>>>  ")
words = message.split(" ")
emojis = {
    ":)": "😂",
    "):": "😔"
}
output = ' '
for word in words:
    output += emojis.get(word, word) + " "
print(output)
print(sqrt(81))


try:
    name = int(input("Enter your name>>>  "))
except:
    print("Re enter the value again")
from Afolabi import Afolabi

student = Afolabi("Akinola", 22, "2000")
print(student.name)
print(f"I am {student.age}, years old.  I was born In {student.year}")

# CLASSES
class Person:
    """

    """

    def __init__(self , name):
        self.name = name

    def talk(self):
        """

        """
        print(f"Hi, I am {self.name}.")


john = Person("Akinola Afolabi")
john.talk()


def community(personality):
    print(personality)


community("Akinola ")
community("How do you do?")


class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    pass
class Cat(Mammal):
    pass
dog1 = Dog()
dog1.walk()

Cat1 = Cat()
Cat1.walk()
