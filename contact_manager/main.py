import json
import re

def ask_user() :
  while True :
    try:
      user_decision = int(input("1. Add Contacts\n2. View Contacts\n3. Search Contacts\n4. Update Contact\n5. Delete Contact\n6. Exit"))
      if user_decision in (1, 2, 3, 4, 5, 6):
        return user_decision
      else:
        print("Invalid Value!!!!")
    except ValueError:
      print("PLEASE ENTER IN BETWEEN 1-6 DEPENDING ON WHAT YOU WANT THIS PROGRAM TO PERFORM!")

def name():
  while True:
    user_name = input('Enter Name')
    try:
      with open("contacts.json", "r") as logbook:
        read_logbook = json.load(logbook)
        duplicare_found = False
        for contact_name in read_logbook:
          if user_name == contact_name["Name"]:
            print("This contact already exist, please try another name")
            duplicare_found = True
            break
        if duplicare_found:
          continue
    except (FileNotFoundError, json.JSONDecodeError):
      read_logbook = []
    return user_name

def phone():
  while True:
    phone_number = input("Enter contact number: ")
    if phone_number.isdigit() and len(phone_number) == 10 :
      return phone_number
    else:
      print("Contact Number must be of 10 digits and contain only integers")
    
def email(): 
  while True:
    ask_email = input("Enter email")
    mail_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(mail_pattern, ask_email):
      return ask_email
    else:
      print("Please Ener Valid Email")

def save_contact(list):
  try:
    with open("contacts.json", "r") as logbook:
      updated_list = json.load(logbook)
  except (FileNotFoundError, json.JSONDecodeError):
    updated_list = [] 

  updated_list.append(list)

  with open("contacts.json", "w") as new_logbook:
    json.dump(updated_list, new_logbook, indent=4)

def add_contacts() :
  new_contact_name = name()
  new_contact_phone = phone()
  new_contact_email = email()
  new_contact = { "Name" : new_contact_name , "Phone" : new_contact_phone, "E-Mail" : new_contact_email,}
  save_contact(new_contact)

def view_contacts() :
  try:
    with open("contacts.json", "r") as logbook:
      read_logbook = json.load(logbook)
      print(read_logbook)
  except (FileNotFoundError, json.JSONDecodeError):
    print("NO CONTACTS IN FOLDER")

def search_contact() :
  try:
    searched_name = input("Enter the name you want to search: ")
    with open("contacts.json", "r") as logbook:
      read_logbook = json.load(logbook)
      for info in read_logbook:
        if searched_name == info["Name"]:
          print(info)
        else:
          print("No such contact exist in your device")
  except (FileNotFoundError, json.JSONDecodeError):
    read_logbook = []
    
def new_data_added(new_logbook, i):
  new_logbook[i]["Name"] = name()
  new_logbook[i]["Phone"] = phone()
  new_logbook[i]["E-Mail"] = email()
  with open("contacts.json", "w") as logbook:
    json.dump(new_logbook, logbook, indent=4)
  print("DATA UPDATED")

def update_contact() :
    try:
      changing_contact = input("Enter the Contact you want to update")
      with open("contacts.json", "r") as logbook:
        new_logbook = json.load(logbook)

      for i, info in enumerate(new_logbook):
        if changing_contact == info["Name"]:
          print("Contact found, Please enter new details")
          new_data_added(new_logbook, i)
          break
    except (FileNotFoundError, json.JSONDecodeError):
      print("No contact found to update")

def delete(new_logbook, i):
  new_logbook.pop(i)
  with open("contacts.json", "w") as contact_list:
    json.dump(new_logbook, contact_list, indent=4)
  print("Contact Successfully deleted")

def delete_contact() :
  try:
    delete_account = input("Enter the account you want to delete:").lower()
    with open("contacts.json", "r") as logbook:
      new_logbook = json.load(logbook)
    for i, info in enumerate(new_logbook):
      if delete_account == info["Name"]:
        delete(new_logbook, i)
        break
  except (FileNotFoundError, json.JSONDecodeError):
    print("No contact found to be deleted")

def _exit():
    user_choice = input("WNAT TO DO SOMETHING MORE?! [y/n]").lower().strip()
    if user_choice in ("y", "n"):
      return user_choice
    else:
      print("INVALID VALUE!!!")


def main():
  while True:
    user_wants = ask_user()
    
    if user_wants == 1 :
      add_contacts()
    if user_wants == 2 :
      view_contacts()
    if user_wants == 3 :
      search_contact()
    if user_wants == 4 :
      update_contact()
    if user_wants == 5 :
      delete_contact()
    if user_wants == 6 :
      print("THANKYOU FOR CONSIDERING OUR SERVICE!!!")
      break 
    
    _continue = _exit()
    if _continue == "n" :
      print("OKAY, HAVE GREAT DAY!")
      break
    else:
      continue

if __name__ == "__main__":
  main()