import random

def roll_dice():
  dice_1 = random.randint(1,6)
  dice_2 = random.randint(1,6)
  print(f"you got: ({dice_1}, {dice_2})")

def exit_game():
  print("okay, exiting!")

def main():
  while True :
    user_decision = input("do you want to roll the dice ?! [y/n]").lower().strip()

    if user_decision == "y":
      roll_dice()

    elif user_decision == "n":
      exit_game()
      break

    else:
      print("invalid choice")

if __name__ == "__main__":
  main()