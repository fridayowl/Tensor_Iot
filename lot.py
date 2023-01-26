

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

def _generateLicense():
    random_license_number = random.randrange( 0000000, 9999999, max_license_length)
    print(Car(str(random_license_number)))
    return Car(str(random_license_number))
   
ParkingLot(2000)   
import random 
max_license_length = 7
userinput = input("type enter") 
license_dictonary =[]

if userinput == "": 
    temp_licensenumber = _generateLicense()
    license_dictonary.append(temp_licensenumber)
print(license_dictonary) 



     
    