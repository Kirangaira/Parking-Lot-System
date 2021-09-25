from parking_lot import ParkingLot, Car

parking_lot = ParkingLot()

cars = [
    Car('KA-01-HM-2937', 21),
    Car('KA-01-HH-1890', 21),
    Car('KA-01-RA-2331', 40),
    Car('KA-01-AA-7020', 30),
    Car('KA-01-MM-2723', 20),
    Car('KA-01-HH-3103', 40),
]

assert parking_lot.create_parking_lot(6) is True

for i in range(0, len(cars)):
    assert parking_lot.park(cars[i]) == i + 1

assert parking_lot.free_slot(4) is True
assert parking_lot.status() is True

assert len(parking_lot.free_parking_lots) == 1
assert parking_lot.park(Car('KA-02-HK-1023', 21)) == 4

assert parking_lot.reg_numbers_for_cars_with_driver_age(21) == ['KA-01-HM-2937', 'KA-01-HH-1890', 'KA-02-HK-1023']
assert parking_lot.slot_numbers_for_cars_with_driver_age(21) == [1, 2, 4]
assert parking_lot.slot_number_for_reg_number('KA-01-HH-3103') == 6
assert parking_lot.slot_number_for_reg_number('MH-04-AY-1111') is None