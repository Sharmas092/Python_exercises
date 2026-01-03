#inputs

start_odo_value = float(input("Please enter the start value of Odometer: "))
end_odo_value = float(input("Please enter the end value of Odometer: "))
fuel_used = float(input("Enter the amount of fuel used: "))
tank_capacity = float(input("Enter the fuel capacity of car: "))

#calculate mileage

distance = end_odo_value - start_odo_value
mileage = distance/fuel_used

#calculate car range

car_range = mileage * tank_capacity

#total trip distance from problem

trip_distance = 560
stops = 0
current_fuel_range = car_range

print("car's mileage " , mileage, "km/l")
print("Total range on a full tank", car_range, "km")
                      
for km in range(1, trip_distance + 1):
    current_fuel_range -= 1
                      
    if current_fuel_range <= 0 and km < trip_distance :
        stops = +1
        current_fuel_range = car_range
        print("Stop", stops, "Refueling at" , km, "km")
print("Total number of stops requires for refilling", stops)                      
                      
                      
                      
