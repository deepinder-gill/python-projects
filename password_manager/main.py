from cryptography.fernet import Fernet 
#key = Fernet.generate_key()
#with open ("mykey.key", "wb") as secret_key:
#  secret_key.write(key)
def load_key():
  with open("mykey.key", "rb") as unlock:
    unlock_key = unlock.read()
  unlocker = Fernet(unlock_key)
  return unlocker

def ask():
  while True:
    user_decision = input("do you wish to ADD new password or VIEW old passwords?? [A/V]").upper()
    if user_decision in ("A", "V"):
      return user_decision
    else:
      print("INVALID VALUE!!")

def add():
  unlocking_key = load_key()
  username = input("enter username or website: ")
  password = input(f"enter password for {username}:")
  encrypted_password = unlocking_key.encrypt(password.encode())
  with open("PASSWORDS.txt", "a") as add_data:
    add_data.write(f"{username} | {encrypted_password.decode()}\n")

  return "data save successfully"

def wanna_continue():
  while True:
    continue_decision = input("do you wish to add more data?!!? [Y/N]").upper()
    if continue_decision in("Y", "N"):
      return continue_decision
    else:
      print("INVALID VALUE!!")

def view_data():
  try:
    unlocking_key = load_key()
    with open("PASSWORDS.txt", "r") as view:
      for line in view:
        username, encrypted_password = line.strip().split("|")
        decrypted_password = unlocking_key.decrypt(encrypted_password.encode()).decode()
        print(f"USERNAME: {username}\nPASSWORD: {decrypted_password}")

  except FileNotFoundError :
      print("NO DATA SAVED YET!!")

def main():
  while True:
    User_wish = ask()
    if User_wish == "A":
      to_add = add()
      print(to_add)
      to_continue = wanna_continue()
      if to_continue == "N" :
        print("THANKYOU!!!")
        break

    elif User_wish == "V":
      view_data()
      to_continue = wanna_continue()
      if to_continue == "N" :
        print("THANKYOU FOR USING OUR SERVICE!!!")
        break

if __name__ == "__main__":
  main()

