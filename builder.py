class Car:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.color = None

    def __str__(self):
        return f"Car(engine={self.engine}, wheels={self.wheels}, color={self.color})"

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_engine(self, engine: str):
        self.car.engine = engine
        return self

    def set_wheels(self, wheels: int):
        self.car.wheels = wheels
        return self

    def set_color(self, color: str):
        self.car.color = color
        return self

    def build(self):
        return self.car

if __name__ == "__main__":
    builder = CarBuilder()
    car = (
        builder
        .set_engine("V8")
        .set_wheels(4)
        .set_color("red")
        .build()
    )
    print(car)
