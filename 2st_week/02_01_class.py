class Person:
    def __init__(self, name, age):
        self.name = name
        self.age =  age

    def talk(self):
        print("Hi I am ", self.name)

person_1 = Person("유재석", 50)
print(person_1) # Person 이라는 Class 의 객체 이다. 0x000001BB9F8C12B0 라는 ID 를 가지고 있다.
print(person_1.name)
print(person_1.age)
person_1.talk()

person_2 = Person("강호동", 45)
print(person_2) # Person 이라는 Class 의 객체 이다. 0x000001BBA11E9090 라는 ID 를 가지고 있다.
print(person_2.name)
print(person_2.age)
person_2.talk()