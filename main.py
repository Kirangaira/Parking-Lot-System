import fileinput
import sys
import re

# Function to process individual command
def process(cmd_params):
  params = cmd_params.strip().split(' ')
  command = params[0]

  if command == 'Create_parking_lot':
     assert len(params) == 2, "Create_parking_lot needs no of slots as well"
     assert params[1].isdigit() is True, "param should be 'integer type'"
  elif command == 'Park':
    assert len(params) == 4, "Park needs registration number and driver's age as well"
    assert params[3].isdigit() is True, "param should be 'integer type'"
    assert re.match("(^[A-Z]{2}\-[0-9]{2}\-[A-Z]{2}\-[0-9]{4}$)",params[1]) != None, "Invalid Registration Number"
  elif command == 'Leave':
    assert len(params) == 2, "leave needs slot number as well"
    assert params[1].isdigit() is True, "slot number should be 'integer type'"

  elif command == 'Vehicle_registration_number_for_driver_of_age':
    assert len(params) == 2,"registration_numbers_for_cars_with_driver_of_age needs driver_age as well"

  elif command == 'Slot_numbers_for_driver_of_age':
    assert len(params) == 2, "slot_numbers_for_driver_of_age needs driver_age as well"

  elif command == 'Slot_number_for_car_with_number':
    assert len(params) == 2, "slot_number_for_registration_number needs registration_number as well"

  elif command == 'exit':
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
 