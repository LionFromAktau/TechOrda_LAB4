from Car import Car


class SportCar(Car):
    speed: float

    def __init__(self):
        self.super = Car()
        self.speed = int(input('Write speed of the car'))

    def __repr__(self) -> str:
        return f'{self.super.__repr__()}.\nSpeed of the car: {self.speed}'