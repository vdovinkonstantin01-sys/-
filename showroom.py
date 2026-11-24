from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    @abstractmethod
    def range_km(self):
        pass

    def discounted_price(self, percent):
        return self.price * (1 - percent / 100)

    def describe(self):
        return f"{self.make} {self.model} ({self.year})"


class Serviceable(ABC):
    @abstractmethod
    def service(self):
        pass


class ElectricCar(Car, Serviceable):
    def __init__(self, make, model, year, price, battery_kwh, kwh_per_100km):
        super().__init__(make, model, year, price)
        self.battery_kwh = battery_kwh
        self.kwh_per_100km = kwh_per_100km

    def range_km(self):
        return (self.battery_kwh / self.kwh_per_100km) * 100

    def service(self):
        return f"{self.make} {self.model}: зарядка батареи"

    def describe(self):
        return f"Электромобиль {super().describe()}"


class GasCar(Car, Serviceable):
    def __init__(self, make, model, year, price, tank_l, l_per_100km):
        super().__init__(make, model, year, price)
        self.tank_l = tank_l
        self.l_per_100km = l_per_100km

    def range_km(self):
        return (self.tank_l / self.l_per_100km) * 100

    def service(self):
        return f"{self.make} {self.model}: замена масла"

    def describe(self):
        return f"Бензиновый {super().describe()}"


class Showroom:
    def __init__(self):
        self._cars = []

    def add(self, car):
        if not isinstance(car, Car):
            raise TypeError("Можно добавлять только объекты Car")
        self._cars.append(car)

    def total_price(self, percent=0):
        return sum(car.discounted_price(percent) for car in self._cars)

    def longest_range(self):
        if not self._cars:
            return None
        return max(self._cars, key=lambda car: car.range_km())

    def service_all(self):
        return [car.service() for car in self._cars if isinstance(car, Serviceable)]

    def __len__(self):
        return len(self._cars)


if __name__ == "__main__":
    pass
