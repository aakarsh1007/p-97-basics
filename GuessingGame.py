guessingGame = int(input("Guess Any Number From 0-9:"))
print(guessingGame)
if (guessingGame == 4):
    print("You got the Number Right")
elif (guessingGame > 4):
    print("Guess A Lesser Number ")
else :
    print(" Guess A larger Number")