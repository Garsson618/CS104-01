import random

numberOfGuesses=20
gameOver=False
theComputerNumber=random.randint(1, 1000000)
lowGuessRange=1
highGuessRange=1000000
playerGuess=0

print("I am thinking of a number between 1 and 1,000,000. Make a guess and I will tell you if you are too high, too low or you have guessed correctly and won the game. You will have 20 guesses. After 20 guesses, you lose the game. I will help you by keeping track of the range in which your guess will be valid. For example, if the number I am thinking of is 480,000 and your first guess is 650,000, I will tell you the number I am thinking of is lower than 650,000. In that case, I will limit your next guess to numbers between 1 and 650,000. If your next guess is 750,000, I will tell you that number is out of range and ask you again for your guess. But, if your next guess is say 249,300, I will say the number I am thinking of is higher than that. In that case, I will limit your next guess to numbers between 249,300 and 650,000. Get the idea? I will count each guess and stop you after 20 guesses if you still have not guessed the number. Based on what I told you, can you think of a way to improve your chances? Good Luck!")

while not gameOver:
    playerGuess=int(input('\n'"You have "+str(numberOfGuesses)+" guesses left. Your range is between "+str(lowGuessRange)+" and "+str(highGuessRange)+"\nEnter your Guess: "))
    if  playerGuess<lowGuessRange or playerGuess>highGuessRange:
        print("That number is outside the range")
        numberOfGuesses=numberOfGuesses+1

    if playerGuess<theComputerNumber:
        print("Your Guess is too Low")
        lowGuessRange=playerGuess
        numberOfGuesses=numberOfGuesses-1

    if playerGuess>theComputerNumber:
        print("Your Guess is too High")
        highGuessRange=playerGuess
        numberOfGuesses=numberOfGuesses-1

    if playerGuess==theComputerNumber:
        gameOver=True
        print("You guessed correctly! The number was " + str(theComputerNumber))
        

    if numberOfGuesses==0:
        gameOver=True
        print("\nYou have used all of your guesses. The Correct Number was " + str(theComputerNumber))
        
