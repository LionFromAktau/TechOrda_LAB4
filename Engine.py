import dataclasses


class Engine:
    power: int
    company: str

    def __init__(self, power:int, company: str):
        self.power = power
        self.company = company

    def __repr__(self) -> str:
        return f'The Engine\'s company name: {self.company}. The Engine\'s power {self.power} h.p'
