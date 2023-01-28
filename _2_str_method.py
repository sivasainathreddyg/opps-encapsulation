class Car:
    def __init__(self,__engine,brand,mileage):
        self.__engine=__engine  #private member 
        self.brand=brand
        self.mileage=mileage
    def __str__(self):
        return f"car details:\nEngine:{self.__engine}\nbrand:{self.brand} \nmileage{self.mileage}"
car=Car("Disel","BMW",30)
print(car)