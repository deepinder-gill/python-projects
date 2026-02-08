# Contact Manager (Python CLI)

This is a simple command-line Contact Manager built using Python.  
The project was created to practice working with files, JSON data, input validation, and basic CRUD operations.

## Features
- Add new contacts
- View all saved contacts
- Search contacts by name
- Update existing contacts
- Delete contacts
- Data stored persistently using a JSON file

## Concepts Used
- Functions and loops
- File handling
- JSON read/write
- Input validation
- Regular expressions (for email validation)
- Error handling using try/except

## How It Works
- Contacts are stored in a `contacts.json` file
- Each contact contains:
  - Name
  - Phone number
  - Email address
- Duplicate names are not allowed
- Menu-driven CLI interface

## Testing
The project was manually tested by running all menu options and validating edge cases such as duplicate entries and invalid inputs.

## Note
This project is intentionally kept simple and focused on logic rather than advanced UI or frameworks.  
Some edge cases and output formatting can be improved in future versions.

## Purpose
This project was built as a learning exercise to strengthen Python fundamentals and understand how real applications manage and store data.

