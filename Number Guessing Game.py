import random

print("Number Guessing Game")

number = random.randint(1,9)
chances = 0
print("Enter Your Guess between 1 and 9 : ")

while chances < 5:
    guess = int(input("Enter Your Guess : "))

    if guess == number:
      print("You Won")
      break

    elif guess < number:
     print("Guess A Number Higher Than ",guess )
    
    else:
     print("Guess A Number Lower Than ",guess )

    chances += 1

if not chances < 5:
    print("You Loose The Number Is",number)

    


