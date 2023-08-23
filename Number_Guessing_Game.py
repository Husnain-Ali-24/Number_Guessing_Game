import random
from Number_Guessin_art import logo
print(logo)
print("Wellcome to the Number Guessing Game!")
print("I am Thinking of a number between 1 and 100")
Input=input("Choose a difficulty. Type 'easy' or 'high': ")
computer_number=random.randint(1,100)
Easy=0
def check(Input):
 if Input=="easy":
  return Easy+10
 elif Input=="high":
  return Easy+5
Easy=check(Input)
condition=True
while condition==True:
 while Easy>0:
  print(f"You Have {Easy} Attempts to guess the number.")
  Input1=int(input("Make a Guess: "))
  if Input1>computer_number:
   print("Too High")
  elif Input1<computer_number:
   print("Too low")
  elif Input1==computer_number:
   print(f"You Got it! The answer was{computer_number}")
   break
  Easy-=1
  if Easy==0:
   print("You Loss!")
 Input2=input("run again? type 'y' or type 'n'")
 if Input2=="y":
  print("Wellcome to the Number Guessing Game!")
  print("I am Thinking of a number between 1 and 100")
  Input=input("Choose a difficulty. Type 'easy' or 'high': ")
  Easy=0
  Easy=check(Input)
  condition=True
 elif Input2=='n':
  condition=False