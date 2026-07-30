# Python Expense Tracker

A command-line Expense Tracker built with Python.

This project focuses on the backend logic of an expense tracking application. The goal is to develop and test the application's core functionality before building a graphical user interface.

The current version does not focus on UI or UX because desktop interface is planned for a future release.

## Features

- Add expenses
- View all expenses
- Edit expenses
- Remove expenses
- Automatically record the expense date
- View expense statistics:
  - Total expenses
  - Number of expenses
  - Average expense
  - Lowest expense
  - Highest expense
- Save expenses to a JSON file
- Load expenses from a JSON file

## Technologies Used

- Python
- JSON
- datetime

## Data Structure

Each expense is stored as a dictionary:

```python
{
    "amount": 5000,
    "category": "Food",
    "description": "Lunch",
    "date": "2026-07-27"
}
```

## Concepts Reviewed

- Functions
- Lists
- Dictionaries
- Loops
- Input validation
- Exception handling (`try` / `except`)
- File handling
- JSON serialization and deserialization
- Python's `datetime` module
- CRUD operations (Create, Read, Update, Delete)

## Concepts Practiced

- Expense data modeling
- Statistical calculations
- Aggregating data using `sum()`
- Finding minimum and maximum values
- Organizing application logic into reusable functions
- Backend-first application development

## Future Improvements

### Backend

- Search expenses
- Filter expenses by category
- Category-based statistics
- Monthly reports
- Budget tracking
- Export expenses to CSV

### GUI

- Build a desktop application
- Display expenses in a table
- Forms for adding and editing expenses
- Buttons and menus for navigation
- Improved user experience and visual design

## Project Status

The backend is functional and provides all core expense-tracking features. The next step is to build a graphical user interface  while reusing the existing backend logic.

## Author

Henoc "Enk" AMUZU
