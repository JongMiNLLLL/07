class Dog:
    def __init__(self, name, breed):
        self.dog_name = name
        self.dog_breed = breed
        self.dog_sex = "남"

    def bark(self):
        print(self.dog_name,"가 짖습니다.")

my_dog = Dog("통통이", "시바")
my_dog.bark()
