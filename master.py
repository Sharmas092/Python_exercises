def divide(num, den):
    quot = num // den
    rem  = num % den
    return quot, rem

Total = 10000
Effort = 3 

#Days = Total // Effort
#Rem_Hrs = Total % Effort
Days,  Rem_Hrs = divide(Total, Effort)

#Months = Days // 30
#Days = Days % 30
Months, Days = divide(Days, 30)

#Years = Months // 12
#Months = Months % 12
Years, Months = divide(Months, 12)


print(Years, "Yrs",  Months, "Mnths", Days, "Days" , Rem_Hrs, "Hrs")
