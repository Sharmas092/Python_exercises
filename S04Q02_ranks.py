def get_rank (percentage):
    if percentage >= 90 :
        return("First Class")
    elif 75 <= percentage < 90 :
        return ("Second Class")
    elif 35 <= percentage < 75 :
        return ("Average")
    else :
        return ("Failed")

def get_scores():
    english = float(input("Please enter scored marks of english: "))
    science = float(input("Please enter scored marks of science: "))
    maths = float(input("Please enter scored marks of maths: "))
    total_scored = english + science + maths
    total_max = 80+90+100
    percentage = (total_scored/total_max)*100
    
    rank = get_rank(percentage)
    
    print(" Total Marks scored: " , total_scored)
    print(" Percentage: " , percentage)
    print(" Rank : ",rank)
    
get_scores()
