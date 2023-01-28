from Person import Person


class Driver(Person):
    experience: int

    def __init__(self):
        self.super = Person()
        self.experience = int(input('Write an experience of the Driver: '))

    def __repr__(self) -> str:
        if self.experience == 0:
            return f'{super.__repr__()}. {self.super.fullName} has no experience'
        elif self.experience == 1:
            return f'{super.__repr__()}. {self.super.fullName} has a year of experience'
        else:
            return f'{self.super.__repr__()}. {self.super.fullName} has {self.experience} years of experience'