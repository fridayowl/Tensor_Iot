import random

class ParkingLot :
    
    # initalizes the parkinglot class
    def  __init__(self,parking_area ,parking_lot=96):
       self.parking_area = parking_area
       self.parking_lot = parking_lot
       self.parking_capacity=parking_area // parking_lot
       self.parking_array=[None] * self.parking_capacity
       print(self.parking_capacity)
       print(self.parking_array)
       
       
    def car_park(self,car , spot): 
        if self.parking_array[spot] is  None: 
            self.parking_array[spot]=car
            print(self.parking_array[spot]) 
            return f" A car with License Number #  {car.license_number} parked in this Spot # {spot} Successfully"
        else :
            return f" A car with License Number #  { self.parking_array[spot] } already parked in this Spot # {spot}"
        
#Car class the defines the property of the car 
class Car :
    def __init__(self,license_number):
        self.license_number = license_number
    
    def __str__(self):
        return self.license_number
 
def main(cars , parking_lot):
    while cars and None in parking_lot.parking_array:
        carlicense_plate = cars.pop(0)
        spot = random.randint(0, parking_lot.parking_capacity- 1)
        while parking_lot.parking_array[spot] is not None :
            spot = spot = random.randint(0, parking_lot.parking_capacity - 1)     
        print(parking_lot.car_park(carlicense_plate,spot))
        
           
__init__="__main__"

parking_lot = ParkingLot(2000)   
max_license_length = 7  #max length of license.
random_license_number = random.randrange(0000000, 9999999-parking_lot.parking_capacity, max_license_length)
userinput = input("type enter")    
if userinput == "":  
    cars = [Car(str(i)) for i in range(
        random_license_number,random_license_number + parking_lot.parking_capacity + 1)]
    main(cars,parking_lot)