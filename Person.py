

class Person:
    age: int
    fullName: str

    def __init__(self):
        self.age = int(input('Write an age of the Person: '))
        name, surname = input('Write a full name of the Person').split(" ")
        self.fullName = f'{name} {surname}'

    def __repr__(self) -> str:
        return f'The persons\'s full name is {self.fullName}. His\\Her age is {self.age}'
