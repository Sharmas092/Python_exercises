lucky = 12 
guess = 20

if guess < lucky - 2 :
    print("Too Low")
if guess > lucky + 2 :
    print("Too High")
if guess == lucky:
    print("Correct")
elif (guess >= lucky - 2) and (guess <= lucky + 2) :
    print("Almost There")
    
