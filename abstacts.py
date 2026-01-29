from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @classmethod
    def stop_engine(self):
        print('engine stopped.')
class Car(Vehicle):
    def start_engine(self):
        print('car engine started.')
class Bike(Vehicle):
    def start_engine(self):
        print('bike engine started')
my_car=Car()
my_bike=Bike()
my_car.start_engine()
my_bike.start_engine()
my_car.stop_engine()
my_bike.stop_engine()


