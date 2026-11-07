#1. Answer the following questions:
#a. What is duck typing, as explained in the video?
# Ducktyping is another way to achieve polymorphism without using inheriatnce and also has a concept saying
#"If it looks liek a duck and quacks like a duck, then it msut be a duck."
#b. What did the Car class need to have so it could work inside the same loop as Dog and
#Cat, even if it does not inherit from the Animal class?
#The car class or its objects needed to have the minimum necessary methods/attribites to work inside the 
#same loop as Dog and Cat, even if it does not inherit from the Animal class, which is the move() method. 


class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on the water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")  


def start_trip(vehicle):
        vehicle.move()

car = Car()
boat = Boat()   
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)   


#3. How does the code in 2.2 demonstrate polymorphism?
#The code shows polymorphism because the same function,start_trip(vehicle),
# can accept different objects (Car, Boat, and Drone) and call their move() methods.