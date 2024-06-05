x = 5
print("Are you ready? This is it! You have five chances!")
userGuess = int(input("Guess a number between 1 & 10 "))
numofGuesses = 1

while userGuess != x and numofGuesses < 5:
    if userGuess == x - 1 or userGuess == x + 1:
        print("HOT")
    else:
        print("COLD")
    numofGuesses = numofGuesses + 1
    userGuess = int(input("lol, guess again "))

if userGuess == x:
    print("CORRECT")
else:
    print("INCORRECT")
    print("GAME OVER")

