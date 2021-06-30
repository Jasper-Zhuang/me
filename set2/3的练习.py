def advancedGuessingGame():
    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    lowerBound = input("Enter an lower bound: ")
    try:
        lowerBound = int(lowerBound)
    except:
       lowerBound= input("Enter an right lower bound: ")
    lowerBound = int(lowerBound)
    print("OK then, a number between {} and _ ?".format(lowerBound))
    upperBound = input("Enter an right upper bound: ")
    try:
        upperBound = int(upperBound)
    except:
       upperBound = input("Enter an upper bound: ")
    print("OK then, a number between {} and {} ?".format(lowerBound , upperBound))
    
    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = int(input("Guess a number: "))
        print("You guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"