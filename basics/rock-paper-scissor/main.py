import random

def ask_user():
  while True:
    choice = input("ROCK, PAPER or SCISSORS ?! (r/p/s)").lower().strip()
    if choice in("r", "p", "s") :
      return choice
    else:
      print("Invalid Choice, please choose again")

def again():
  while True:
    play_again = input("Wanna Play Again?!🥰 [y/n]").lower().strip()
    if play_again in ("y", "n"):
      return play_again
    else:
      print("Invalid Choice, please choose again")

def main():
  while True:
    choices = ("r", "p", "s")
    computers_choice = random.choice(choices)
    user_choice = ask_user()
    
    emojis = {
      "r" : "🪨",
      "p" : "📃",
      "s" : "✂️" 
      }
    
    print(f"you chose:{emojis[user_choice]}\ncomputer chose:{emojis[computers_choice]}")

    if user_choice == computers_choice :
      print("its a tie😱")
    elif (user_choice == "r" and computers_choice == "p") or (user_choice == "p" and computers_choice == "s") or(user_choice == "s" and computers_choice == "r"): 
       print("YOU LOST!😔😔")
    else:
      print("YOU WON !! 🎉🎉")

    stop_game = again()
    if stop_game == "n":
      print("okay see ya next time")
      break

if __name__ == "__main__":
  main()