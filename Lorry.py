from Car import Car


class Lorry(Car):
    carrying: int

    def __init__(self):
        self.super = Car()
        self.carrying = int(input('Write carrying of the car'))

    def __repr__(self) -> str:
        return f'{self.super.__repr__()}.\nCarrying of the car: {self.carrying}'
