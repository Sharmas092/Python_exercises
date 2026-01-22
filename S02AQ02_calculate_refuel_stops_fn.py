def calculate_refuel_stops(start_odom,end_odom,fuel_used,tank_capacity,trip_distance):
    #Calculates mileage using odometer readings.
    distance_traveled = end_odom - start_odom
    car_mileage = distance_traveled / fuel_used

    #calculate fuel consume
    fuel_need_for_trip = trip_distance/car_mileage

    #calculate stops
    stops = fuel_need_for_trip/tank_capacity

    return car_mileage, stops

#Inputs
start_value = float(input("Please enter the start value of Odometer: "))
end_value = float(input("Please enter the end value of Odometer: "))
fuel_used = float(input("Enter the amount of fuel used: "))
tank_capacity = float(input("Enter your car's fuel tank capacity (liters): "))
trip_distance = float(input("Enter trip distance: "))

                      
#Outputs
car_mileage,stops_required = calculate_refuel_stops(start_value, end_value, fuel_used, tank_capacity, trip_distance)

print("Total fuel used for total trip",  trip_distance/car_mileage)
print("Refuel stops:" , stops_required)
