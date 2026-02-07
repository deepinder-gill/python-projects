#  Password Manager (Python)

A simple command-line password manager built using Python and `cryptography.fernet`.

This project allows you to securely **store and view passwords** by encrypting them using a secret key.  
Passwords are never saved in plain text.

---

##  Features
- Encrypts passwords using **Fernet symmetric encryption**
- Store passwords for websites / usernames
- View decrypted passwords securely
- Uses a secret key stored locally (never pushed to GitHub)
- Beginner-friendly but introduces real-world security concepts

---

##  Tech Stack
- Python
- cryptography (Fernet)

---

##  Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt