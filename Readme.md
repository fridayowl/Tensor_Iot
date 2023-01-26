# TensorIOT Parking lot Assignment 
Create a parking lot class that takes in a square footage size as input
and creates an array of empty values based on the input square footage
size. Assume every parking spot is 8x12 (96 ft2) for this program, but have
the algorithm that calculates the array size be able to account for
different parking spot sizes. For example, a parking lot of size 2000ft2
can fit 20 cars, but if the parking spots were 10x12 (120 ft2), it could
only fit 16 cars. The size of the array will determine how many cars can
fit in the parking lot.*

*Create a car class that takes in a 7 digit license plate and sets it as a
property. The car will have 2 methods:*

*1.        A magic method to output the license plate when converting the
class instance to a string.*

*2.        A "park" method that will take a parking lot and spot # as input
and fill in the selected spot in the parking lot. If another car is parked
in that spot, return a status indicating the car was not parked
successfully. If no car is parked in that spot, return a status indicating
the car was successfully parked.*

*Have a main method take an array of cars with random license plates and
have them park in a random spot in the parking lot array until the input
array is empty or the parking lot is full. If a car tries to park in an
occupied spot, have it try to park in a different spot instead until it
successfully parks. Once the parking lot is full, exit the program.*

*Output when a car does or does not park successfully to the terminal (Ex.
"Car with license plate [LICENSE_PLATE] parked successfully in spot [SPOT
#]").


## Development : 

Creating a Parking lot : 
        
            Parking Area = user input 
            Parking Lot = 96 ft
            Total Capacity =  Parking Area / Parking Lot 
            Parking array = [0] * Total Capacity 

            Example :
            Parking Area = 2000 
            Parking Lot = 96 
            Total Capacity = 2000 / 96  = 20.8 
            <span style="color: red"> Remove the decimal part  </span>
            Parking array = [0] * 20 
            result = [0,0,0,0,0..............] // create 20 empty array.

Creating a Car Class :

            Given :
            Car should return a 7 digit license number using magic method or dunder method 

            Class Car :
                def __init__(self,license_number) :
                    self.license_number = license_number
                
                def __str__(self):
                    return self.license_number


            create a 7 digit random number . 
                max_length =7 
                for i in range(0000000, 1564675 + parking_lot.capacity + 1)
    Create a parkingspot 
            spot = random (0,totalcapacity - 1)
            No need to create the spot if the spot is already full 
            if parking spot is full exit the program 
    
    Create a parking method :

            Takes , Parking lot , parking spot 
            check if the parking spot is empty or nor 
            if not assing the spot 
            else not assign the car to the spot



    Create a main method :

            main method takes an array of cars and the parking lot
            get first car licence number and create a spot 
            transfer the spot the parking function until the car array become none .

    
## IDE USED :

VSCODE  :1.74 
Tested on :
Python version : 3

