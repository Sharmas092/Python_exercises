num =1 
while num<=100:
    num = int(input("Please enter number: "))
    if num < 0 :
        print("No negative numbers please")
        break
    elif num < 100: #redundant to check if enter num>0 
        print(num**0.5)   
else:
    print("Bye")   

print("Done")
