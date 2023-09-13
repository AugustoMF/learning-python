import random

secretNumber = random.randint(1,6)
guessCount = 0
guessLimit = 3
while guessCount < guessLimit:
   guess = int (input  ('Guess the secret number '))
   guessCount += 1
   if guess == secretNumber:
      print ("Corect!")
      break
else: 
    print(secretNumber)
    print ("You failed")
