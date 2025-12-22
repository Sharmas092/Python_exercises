#inputs

start_value = float(input("Please enter the start value of Odometer: "))
end_value = float(input("Please enter the end value of Odometer: "))
fuel_used = float(input("Enter the amount of fuel used: "))

#calculate mileage

distance = end_value - start_value
mileage = distance / fuel_used

                  
#Results

print("Total distance travlled by car:", distance)
print("Car milaeage;", mileage)                  
