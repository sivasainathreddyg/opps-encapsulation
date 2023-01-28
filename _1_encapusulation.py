#encapsulation
#it is use to bind attributes(variable) and behaviour(methods) together into single unit
#it is used to acess private menbers through public environment
#private member--- cannot be accessed outside the class

class Car:
    def __init__(self,__engine,brand,mileage):
        self.__engine=__engine  #private member 
        self.brand=brand
        self.mileage=mileage
    def display(self):
        return f"car details:\nEngine:{self.__engine}\nbrand:{self.brand} \nmileage{self.mileage}"
    # getter and setter

    # setter for engine
    def set_engine(self,__engine):
        self.__engine = __engine 

    # getter for engine
    def get_engine(self):
        return self.__engine

    # setter for brand
    def set_brand(self,brand):
        self.brand = brand 

    # getter for engine
    def get_brand(self):
        return self.brand

    # setter for mileage
    def set_mileage(self,mileage):
        self.mileage = mileage

    # getter for mileage
    def get_mileage(self):
        return self.mileage

car = Car("Diesel Engine","BMW","35km/l")
# data = car.display()
# print(data)
# print(car.brand)
# print(car.__engine)

car.set_engine("petrol engine")
data=car.get_engine()
print(data)



# print("Before modification : \n",data,"\n")

# car.set_mileage("45km/l")
# car.set_engine("Petrol Engine")

# data=car.display()
# print("After modification : \n",data,"\n")

# mileage = car.get_mileage()
# print("\n Mileage : ",mileage)


