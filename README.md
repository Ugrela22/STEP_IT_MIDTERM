# 📚 Book Management System / წიგნების მართვის სისტემა

A console-based book management application written in Python with Georgian language interface.

## Overview

This application allows users to manage a personal book library through a command-line interface. All data is stored in JSON format for persistence between sessions.

## Features

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

```bash
python book_console1.py
```

## Initial Data

The application comes with pre-loaded Georgian literary classics:
- ვეფხისტყაოსანი (The Knight in the Panther's Skin) - შოთა რუსთაველი
- ალუდა ქეთელაური - ვაჟა-ფშაველა  
- მთვარის მოტაცება - კონსტანტინე გამსახურდია

## File Storage

- Data is stored in `books_data.json`
- Automatic backup and recovery
- UTF-8 encoding for Georgian text support

## Technical Features

- Object-oriented design
- Error handling and validation
- Clean separation of concerns
- User-friendly Georgian interface
- Persistent data storage