

class ParkingLot :
    # initalizes the parkinglot class 
    
   def  __init__(self,parking_area ,parking_lot=96):
       self.parking_area = parking_area
       self.parking_lot = parking_lot
       self.parking_capacity=parking_area // parking_lot
       self.parking_array=[0] * self.parking_capacity
       print(self.parking_capacity)
       print(self.parking_array)

#Car class the defines the property of the car 

class Car :
    def __init__(self,license_number):
        self.license_number = license_number
    
    def __str__(self):
        return self.license_number

def _generate_license_number():
    random_license_number = random.randrange( 0000000, 9999999, max_license_length)
    # print(Car(str(random_license_number)))
    return random_license_number
   
ParkingLot(2000)   
import random 


max_license_length = 7  #max length of license.

userinput = input("type enter")   #userinput when car enters.

license_dictonary =[] #to map all the license numbers.

checkduplication=True

#check and creates new license for each car .
if userinput == "": 
    while  checkduplication :
        temp = _generate_license_number() 
        if temp not in license_dictonary :
            license_dictonary.append(temp)
            cars = Car(str(temp))
            cont= False

print(license_dictonary)

     
    