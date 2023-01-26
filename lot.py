

class ParkingLot :
    # initalizes the parkinglot class 
    
   def  __init__(self,parking_area ,parking_lot=96):
       self.parking_area = parking_area
       self.parking_lot = parking_lot
       self.parking_capacity=parking_area // parking_lot
       self.parking_array=[0] * self.parking_capacity
       print(self.parking_capacity)
       print(self.parking_array)


   
ParkingLot(2000)        
    