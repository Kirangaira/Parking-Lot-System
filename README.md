## Problem Statement
We own a parking lot that can hold up to ‘n’ cars at any given point in time. Each slot is given a number starting at one increasing with increasing distance from the entry point in steps of one. We want to create an automated ticketing system that allows our customers to use our parking lot without human intervention.

When a car enters the parking lot, we want to have a ticket issued to the driver. The ticket issuing process includes:- 

1. We are taking note of the number written on the vehicle registration plate and the age of the driver of the car.
2. And we are allocating an available parking slot to the car before actually handing over a ticket to the driver (we assume that our customers are kind enough to always park in the slots allocated to them).

The customer should be allocated a parking slot that is nearest to the entry. At the exit, the customer returns the ticket, marking the slot they were using as being available.

Due to government regulation, the system should provide us with the ability to find out:-

- Vehicle Registration numbers for all cars which are parked by the driver of a certain age.
- Slot number in which a car with a given vehicle registration plate is parked. 
- Slot numbers of all slots where cars of drivers of a particular age are parked.

We get the input by reading input.txt directly (you’ll have to create it in your environment) .The file will contain a set of commands separated by a newline, we need to execute the commands in order and produce output.

### Input (input.txt)
```
Create_parking_lot 6
Park KA-01-HH-1234 driver_age 21
Park PB-01-HH-1234 driver_age 21
Slot_numbers_for_driver_of_age 21
Park PB-01-TG-2341 driver_age 40
Slot_number_for_car_with_number PB-01-HH-1234
Leave 2
Park HR-29-TG-3098 driver_age 39
Vehicle_registration_number_for_driver_of_age 18
```
### Output (In stdout)

```
Created parking of 6 slots
Car with vehicle registration number "KA-01-HH-1234" has been parked at slot number 1
Car with vehicle registration number "PB-01-HH-1234" has been parked at slot number 2
1,2
Car with vehicle registration number "PB-01-TG-2341" has been parked at slot number 3
2
Slot number 2 vacated, the car with vehicle registration number "PB-01-HH-1234" left the space, the driver of the car was of age 21
Car with vehicle registration number "HR-29-TG-3098" has been parked at slot number 2
```

### Description of each command from the above input file:
Command      | Description of command
------------ | -------------
Create_parking_lot 6 | Create a parking lot of 6 slots
Park KA-01-HH-1234 driver_age 21 | Park car with vehicle registration number “ KA-01-HH-1234”, and the vehicle is driven by the driver of age 21
Park PB-01-HH-1234 driver_age 21 | Park car with vehicle registration number “ PB-01-HH-1234”, and the car is driven by the driver of age 21
Slot_numbers_for_driver_of_age 21 | Return all Slot Number(Comma-separated) of all cars which have drivers with age==21
Park PB-01-TG-2341 driver_age 40  | Park car with vehicle registration number “ PB-01-TG-2341”, and the car is driven by the driver of age 40
Slot_number_for_car_with_number PB-01-HH-1234 | Return slot number for the car with registration number “PB-01-HH-1234”
Leave 2 | Vacate the slot number 2 from the parking lot, i.e. car which was parked at slot number 2 has left the space if there exists no car at slot number 2, print “Slot already vacant” 
Park HR-29-TG-3098 driver_age 39 | Park car with vehicle registration number “ HR-29-TG-3098”, and the car is driven by the driver of age 39
Vehicle_registration_number_for_driver_of_age 18 | Get all parked vehicle registration number of cars parked by the driver of age 18

### Project Requirements:

- Python 3.8

### Commands to run the Program:

From project directory, run the following commands:

To execute the commands in input.txt, type the following in ***shell***: 
 ```
 python3.8 main.py
 ```

To execute individual command, refer to the above table and type the command in ***console*** when program is running:

For example:
```
Park KA-01-HM-2134 driver_age 21
```

To terminate the program:
```
exit
```
To run test cases, type the following in ***shell***:
 ```
 python3.8 test.py
 ```
