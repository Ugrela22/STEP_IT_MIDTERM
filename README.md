# 🏦 STEP IT Midterm Project Collection / პროექტების კოლექცია

A collection of three Python console applications with Georgian language interfaces, developed as part of the STEP IT midterm project.

## Projects Overview 

This repository contains three main applications:

### 1. 🏧 ATM System (ATM.py)
A fully functional ATM simulation with user authentication and banking operations.

### 2. 🧮 Calculator (calculator.py) 
An advanced calculator with comprehensive error handling and mathematical operations.

### 3. 📚 Book Management System (book_console1.py)
A console-based library management application for organizing personal book collections.

## 🏧 ATM System Features

- **User Authentication**: Secure PIN-based login with card number validation
- **Account Management**: Balance inquiry, withdrawal, and deposit operations
- **Transaction Limits**: Withdrawal limits and deposit maximum amounts
- **Data Persistence**: User data stored in text file format
- **Security Features**: Account lockout after failed login attempts
- **Georgian Interface**: Full Georgian language support for banking operations
- **Error Handling**: Comprehensive input validation and error messages

### Test Credentials:
- Card: 1234, PIN: 1111 (გიორგი - 5000₾)
- Card: 5678, PIN: 2222 (ნინო - 3500₾)  
- Card: 9999, PIN: 3333 (ლევან - 10000₾)

## 🧮 Calculator Features

- **Basic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Advanced Operations**: Power (x^y), Square Root (√)
- **Error Handling**: Division by zero, invalid input, overflow protection
- **Input Validation**: Comprehensive number validation and format checking
- **Georgian Interface**: Mathematical operations with Georgian language interface
- **Safety Limits**: Protection against memory overflow and extreme calculations

## 📚 Book Management Features

- **Add Books**: Add new books with title, author, and publication year
- **Remove Books**: Delete books from the library by title
- **Search Functionality**: 
  - Search by title
  - Search by author
  - Search by publication year
- **View All Books**: Display complete library collection
- **Data Persistence**: Automatic save/load using JSON file storage
- **Input Validation**: Comprehensive validation for all user inputs
- **Georgian Language Interface**: Full Georgian language support

## Code Structure

### Classes

- **`Book`**: Represents a single book with title, author, and publication year
  - Methods: `to_dict()`, `from_dict()`, `__str__()`

- **`BookManager`**: Handles all book operations and file management
  - File operations: `save_to_file()`, `load_from_file()`
  - Book operations: `add_book()`, `remove_book()`, `search_*()`, `display_all_books()`
  - Creates initial sample data with Georgian literature classics

### Functions

- **Validation Functions**: `validate_title()`, `validate_author()`, `validate_year()`
- **Interface Functions**: Separate functions for each menu option
- **Display Functions**: `print_menu()`, `display_search_results()`

## How to Run

### ATM System
```bash
python ATM.py
```

### Calculator
```bash
python calculator.py
```

### Book Management System
```bash
python book_console1.py
```

## Initial Data

The application comes with pre-loaded Georgian literary classics:
- ვეფხისტყაოსანი (The Knight in the Panther's Skin) - შოთა რუსთაველი
- ალუდა ქეთელაური - ვაჟა-ფშაველა  
- მთვარის მოტაცება - კონსტანტინე გამსახურდია

## File Structure

```
STEP_IT_MIDTERM/
├── ATM.py                 # ATM system implementation
├── calculator.py          # Advanced calculator
├── book_console1.py       # Book management system
└── README.md             # Project documentation
```

## Data Storage

- **ATM System**: User data stored in `users.txt` with UTF-8 encoding
- **Book System**: Library data stored in `books_data.json` with automatic backup
- **Calculator**: No persistent storage (session-based calculations)

## Technical Features

- **Object-oriented Programming**: Clean class-based architecture
- **Error Handling**: Comprehensive exception handling and input validation
- **Georgian Language Support**: Full Unicode support for Georgian text
- **Data Persistence**: Automatic save/load functionality where applicable
- **User Experience**: Intuitive console interfaces with clear navigation
- **Security**: Input validation and secure authentication mechanisms

## Development Environment

- **Language**: Python 3.x
- **Encoding**: UTF-8 for Georgian language support
- **File I/O**: Text and JSON file handling
- **Math Operations**: Built-in math library for advanced calculations
