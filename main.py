import fileinput
import sys
import re
from parking_lot import ParkingLot, Car

parking_lot = ParkingLot()

# Function to process individual command
def process(cmd_params):
  params = cmd_params.strip().split(' ')
  command = params[0]

  if command.lower() == 'create_parking_lot':
     assert len(params) == 2, "Create_parking_lot needs no of slots as well"
     assert params[1].isdigit() is True, "param should be 'integer type'"

     parking_lot.create_parking_lot(int(params[1]))


  elif command.lower() == 'park':
    assert len(params) == 4, "Park needs registration number and driver's age as well"
    assert params[3].isdigit() is True, "Driver's age should be 'integer type'"
    assert re.match("(^[A-Z]{2}\-[0-9]{2}\-[A-Z]{2}\-[0-9]{4}$)",params[1]) != None, "Invalid Registration Number"

    assert parking_lot.check_reg_no_exists(params[1]) == False, "Two cars cannot have same registration number, a car with registration number {} already present".format(params[1])
    
    car = Car(params[1], int(params[3]))
    parking_lot.park(car)

  elif command.lower() == 'leave':
    assert len(params) == 2, "leave needs slot number as well"
    assert params[1].isdigit() is True, "slot number should be 'integer type'"
    parking_lot.free_slot(int(params[1]))

  elif command == 'status':
        parking_lot.status()

  elif command.lower() == 'vehicle_registration_number_for_driver_of_age':
    assert len(params) == 2,"registration_numbers_for_cars_with_driver_of_age needs driver_age as well"

    assert params[1].isdigit() is True, "Driver's age should be 'integer type'"


    parking_lot.reg_numbers_for_cars_with_driver_age(int(params[1]))


  elif command.lower() == 'slot_numbers_for_driver_of_age':
    assert len(params) == 2, "slot_numbers_for_driver_of_age needs driver_age as well"
    assert params[1].isdigit() is True, "Driver's age should be 'integer type'"

    parking_lot.slot_numbers_for_cars_with_driver_age(int(params[1]))

  elif command.lower() == 'slot_number_for_car_with_number':
    assert len(params) == 2, "slot_number_for_registration_number needs registration_number as well"
    parking_lot.slot_number_for_reg_number(params[1])

  elif command.lower() == 'exit':
    exit(0)

  else:
    print("Error: Wrong Command")     

# Handling Input 

if len(sys.argv) == 1:
# To handle individual commands input
    while True:
      try:
        line = input()
        process(line)
      except Exception as e:
        print("Error:", e)
else:
# To read commands from text file
    for line in fileinput.input():
      try:
        process(line)
      except Exception as e:
        print("Error:", e)
 