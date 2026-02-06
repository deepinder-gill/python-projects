import random

def too_high():
  print("too high!")
  
def too_low():
  print("too low!")

def congo():
   print("YOU GOT IT !!!!!")

def user_guess():
  while True:
    try:
      a = int(input("enter a number between 1 and 100:"))
      if 1 <= a <= 100:
        return a
      else:
        print("number must be between 1 and 100")
    except ValueError:
      print("Invalid Input !!!!! Please enter a whole number")

   
def main():

  random_number = random.randint(1,100)
  while True:
    guess = user_guess()
    if random_number == guess:
      congo()
      break
    elif random_number > guess:
      too_low()
    elif random_number < guess:
      too_high()
          
if __name__ == "__main__" :
  main() 
   