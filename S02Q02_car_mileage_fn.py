def get_trip_mileage(start_odom, end_odom, fuel_used):
    """Calculates mileage using odometer readings."""
    distance_traveled = end_odom - start_odom
    mileage = distance_traveled / fuel_used
    return mileage
    
#inputs
start_value = float(input("Please enter the start value of Odometer: "))
end_value = float(input("Please enter the end value of Odometer: "))
fuel_used = float(input("Enter the amount of fuel used: "))
      
#Result
print("Car mileage;", get_trip_mileage(start_value, end_value, fuel_used))
