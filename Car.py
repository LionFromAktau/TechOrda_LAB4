

from Driver import Driver
from Engine import Engine


class Car:
    carClasses: str
    engine: Engine
    driver: Driver
    marka: str

    def __init__(self):
        self.marka = input('Write a mark of a car')
        self.carClasses = input('Write a class of a car')
        power = int(input('Write a power of the engine: '))
        company = input('Write a company of the engine')
        self.engine = Engine(power=power, company=company)
        self.driver = Driver()

    def star(self):
        print('Forward')

    def stop(self):
        print('Stop')

    def turnRight(self):
        print("Turn Right")

    def TurnLeft(self):
        print("='Turn Left")

    def __repr__(self):
        return f'The mark of the auto: {self.marka}. The class of the auto: {self.carClasses}.\n{self.driver.__repr__()}.\n{self.engine.__repr__()}'
