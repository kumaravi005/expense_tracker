"""
Core module for managing expenses - CRUD operations (Create, Read, Update, Delete).
This module handles all file I/O operations with the CSV data file.

Why separate modules?
- Modular code is easier to test, maintain, and scale
- Each module has one clear responsibility (separation of concerns)
- Easy to reuse functions in different parts of the app
"""

import csv
import os
from datetime import datetime
from config import DATA_FILE, CSV_COLUMNS, DATE_FORMAT, CATEGORIES


def init_csv():
    """
    Initialize the CSV file if it doesn't exist.
    Creates a new CSV with header row containing column names.
    
    Why: Always ensure the data file has proper headers before operations.
    """
    if not os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(CSV_COLUMNS)  # Write header row
            print(f"✓ Created new data file: {DATA_FILE}")
        except IOError as e:
            print(f"✗ Error creating file: {e}")
    else:
        print(f"✓ Data file already exists: {DATA_FILE}")


def add_expense(date, category, amount, note):
    """
    Add a new expense record to the CSV file.
    
    Args:
        date (str): Date in format YYYY-MM-DD
        category (str): One of the predefined categories
        amount (float): Expense amount
        note (str): Optional note/description
    
    Returns:
        bool: True if successful, False otherwise
    
    Error Handling:
        - Validates date format
        - Validates category
        - Validates amount is positive
    """
    # Validate inputs
    if not validate_inputs(date, category, amount):
        return False
    
    try:
        with open(DATA_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            # Round amount to 2 decimal places
            writer.writerow([date, category, f"{float(amount):.2f}", note])
        print(f"✓ Expense added: {category} - {amount} on {date}")
        return True
    except IOError as e:
        print(f"✗ Error adding expense: {e}")
        return False


def get_all_expenses():
    """
    Retrieve all expenses from the CSV file.
    
    Returns:
        list: List of dictionaries, each representing an expense record
        
    Example:
        [{'Date': '2024-01-15', 'Category': 'Food', 'Amount': '50.00', 'Note': 'Lunch'},
         {'Date': '2024-01-16', 'Category': 'Transport', 'Amount': '20.00', 'Note': 'Taxi'}]
    """
    expenses = []
    try:
        with open(DATA_FILE, 'r') as file:
            reader = csv.DictReader(file)
            # DictReader automatically uses first row as column names
            for row in reader:
                expenses.append(row)
        return expenses
    except FileNotFoundError:
        print("✗ Data file not found. Initialize first.")
        return []
    except IOError as e:
        print(f"✗ Error reading file: {e}")
        return []


def edit_expense(row_number, date, category, amount, note):
    """
    Edit an existing expense record.
    
    Args:
        row_number (int): Row number to edit (0-indexed, excluding header)
        date, category, amount, note: New values
    
    Returns:
        bool: True if successful, False otherwise
    
    How it works:
        - Reads all expenses
        - Modifies the specified row
        - Rewrites entire file (because CSV doesn't support in-place edits)
    """
    if not validate_inputs(date, category, amount):
        return False
    
    try:
        expenses = get_all_expenses()
        
        if row_number < 0 or row_number >= len(expenses):
            print(f"✗ Invalid row number: {row_number}")
            return False
        
        # Update the specified expense
        expenses[row_number] = {
            'Date': date,
            'Category': category,
            'Amount': f"{float(amount):.2f}",
            'Note': note
        }
        
        # Rewrite entire file with updated data
        with open(DATA_FILE, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=CSV_COLUMNS)
            writer.writeheader()
            writer.writerows(expenses)
        
        print(f"✓ Expense updated at row {row_number}")
        return True
    except Exception as e:
        print(f"✗ Error editing expense: {e}")
        return False


def delete_expense(row_number):
    """
    Delete an expense record by row number.
    
    Args:
        row_number (int): Row number to delete (0-indexed, excluding header)
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        expenses = get_all_expenses()
        
        if row_number < 0 or row_number >= len(expenses):
            print(f"✗ Invalid row number: {row_number}")
            return False
        
        deleted = expenses.pop(row_number)
        
        # Rewrite file without deleted row
        with open(DATA_FILE, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=CSV_COLUMNS)
            writer.writeheader()
            writer.writerows(expenses)
        
        print(f"✓ Deleted expense: {deleted['Category']} - {deleted['Amount']} on {deleted['Date']}")
        return True
    except Exception as e:
        print(f"✗ Error deleting expense: {e}")
        return False


def validate_inputs(date, category, amount):
    """
    Validate expense inputs before storing.
    
    Args:
        date (str): Date string
        category (str): Category name
        amount (str/float): Expense amount
    
    Returns:
        bool: True if all inputs are valid, False otherwise
    
    Validation Rules:
        - Date must be in YYYY-MM-DD format
        - Category must be in predefined list
        - Amount must be positive number
    """
    # Validate date format
    try:
        datetime.strptime(date, DATE_FORMAT)
    except ValueError:
        print(f"✗ Invalid date format. Use {DATE_FORMAT}")
        return False
    
    # Validate category
    if category not in CATEGORIES:
        print(f"✗ Invalid category. Choose from: {', '.join(CATEGORIES)}")
        return False
    
    # Validate amount
    try:
        amount_float = float(amount)
        if amount_float <= 0:
            print("✗ Amount must be positive")
            return False
    except ValueError:
        print("✗ Amount must be a number")
        return False
    
    return True


def display_expenses(expenses):
    """
    Display expenses in a formatted table.
    
    Args:
        expenses (list): List of expense dictionaries from get_all_expenses()
    """
    if not expenses:
        print("No expenses to display")
        return
    
    # Print table header
    print("\n" + "=" * 80)
    print(f"{'#':<3} {'Date':<12} {'Category':<18} {'Amount':<12} {'Note':<35}")
    print("=" * 80)
    
    # Print each expense
    for idx, expense in enumerate(expenses):
        note = expense['Note'][:32] + "..." if len(expense['Note']) > 32 else expense['Note']
        print(f"{idx:<3} {expense['Date']:<12} {expense['Category']:<18} ${expense['Amount']:<11} {note:<35}")
    
    print("=" * 80 + "\n")
