import heapq
from collections import defaultdict, OrderedDict

class Car:
  '''
  Car Class for creating a Car Object having registration number and driver age
  '''
  def __init__(self, reg_no, age):
      '''
      Constructor to intialize the data members
      '''
      self.reg_no = reg_no
      self.driver_age = age

  def __str__(self):
      '''
      Overriding the print command to print an object.
      '''
      return "Car [registration_number=" + self.reg_no + ", driver_age=" + self.driver_age + "]"
    
class ParkingLot:
    '''
    ParkingLot class to create a Parking lot object having all the methods to park a class, free a slot and so on.
    '''
    def __init__(self):
      '''
      Constructor with data members

      reg_slot_mapping: A dictionary containing registration number as the key and corresponding slot number as the value
      
      driver_age_reg_mapping: A dictionary having driver's age as the key and list of corresponding registration numbers of car as value
      
      slot_car_mapping: An ordered dictionary having slot number as the key and car registration number as value

      free_parking_lots: A heap containing available parking slots

      '''
      self.reg_slot_mapping = dict()
      self.driver_age_reg_mapping = defaultdict(list)
      # we need to maintain the orders of cars while showing 'status'
      self.slot_car_mapping = OrderedDict()
      # initialize all slots as free
      self.free_parking_lots = []
      
    def create_parking_lot(self, total_slots):
        '''
        To create a parking lot 
        '''
        # Using min heap as this will always give minimum slot number in O(1) time which will be nearest to entry
        print("Created parking of {} slots".format(total_slots))
        for i in range(1, total_slots + 1):
            heapq.heappush(self.free_parking_lots, i)
        return True

    def get_nearest_slot(self):
        '''
        To get the nearest slot available
        '''
        return heapq.heappop(self.free_parking_lots) if self.free_parking_lots else None

    def park(self, car):
        '''
        To park a car
        '''
        slot_no = self.get_nearest_slot()
        if slot_no is None:
            print("Sorry, parking lot is full")
            return
        print('Car with vehicle registration number "{}" has been parked at slot number {}'.format(car.reg_no, slot_no))
        self.slot_car_mapping[slot_no] = car
        self.reg_slot_mapping[car.reg_no] = slot_no
        self.driver_age_reg_mapping[car.driver_age].append(car.reg_no)
        return slot_no

    def free_slot(self, slot_to_be_freed):
        '''
        To free up a slot
        '''
        found = None
        for reg_no, slot in self.reg_slot_mapping.items():
            if slot == slot_to_be_freed:
                found = reg_no

        # Cleanup from all cache
        if found:
            heapq.heappush(self.free_parking_lots, slot_to_be_freed)
            del self.reg_slot_mapping[found]
            car_to_leave = self.slot_car_mapping[slot_to_be_freed]
            self.driver_age_reg_mapping[car_to_leave.driver_age].remove(found)
            del self.slot_car_mapping[slot_to_be_freed]
            print('Slot number {} vacated, the car with vehicle registration number "{}" left the space, the driver of the car was of age {}'.format(slot_to_be_freed, car_to_leave.reg_no, car_to_leave.driver_age))
            return True

        else:
            print("slot is not in use")
            return False

    def status(self):
        '''
        To get the status of parking lot
        '''
        print("Slot No.  Registration No  Driver Age")
        for slot, car in self.slot_car_mapping.items():
            print("{}         {}    {}".format(slot, car.reg_no, car.driver_age))
        return True


    def reg_numbers_for_cars_with_driver_age(self, driver_age):
        '''
        To get Vehicle registration numbers for all cars which are parked by the driver of a certain age
        '''
        registration_numbers = self.driver_age_reg_mapping[driver_age]
        print(", ".join(registration_numbers))
        return self.driver_age_reg_mapping[driver_age]

  
    def slot_numbers_for_cars_with_driver_age(self, driver_age):
        '''
        To get Slot numbers of all slots where cars of drivers of a particular age are parked.
        '''
        registration_numbers = self.driver_age_reg_mapping[driver_age]
        slots = [self.reg_slot_mapping[reg_no] for reg_no in registration_numbers]
        print(", ".join(map(str, slots)))
        return slots

    def slot_number_for_reg_number(self, reg_no):
        '''
        To get Slot number in which a car with a given vehicle registration plate is parked. 
        '''
        slot_number = None
        if reg_no in self.reg_slot_mapping:
            slot_number = self.reg_slot_mapping[reg_no]
            print(slot_number)
            return slot_number
        else:
            print("Not found")
            return slot_number

    def check_reg_no_exists(self, reg_no):
      '''
      To check uniqueness of Registration Number
      '''
      found = False
      for key in self.reg_slot_mapping:
        if key == reg_no:
          found = True
      return found