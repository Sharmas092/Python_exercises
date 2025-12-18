Total = 10000
#Effort = 5
Effort = int(input("What's your Daily effort? "))

Days = Total // Effort
Rem_Hrs = Total % Effort
Months = Days // 30
Rem_Days = Days % 30
Years = Months // 12
Rem_Months = Months % 12

print(Years, "Yrs",  Rem_Months, "Mnths", Rem_Days, "Days" , Rem_Hrs, "Hrs")
