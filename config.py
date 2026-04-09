"""
Configuration file for the Expense Tracker application.
This file contains all constant values and default settings.
"""

# Data file path
DATA_FILE = 'expenses.csv'

# Budget limit (in currency units)
MONTHLY_BUDGET_LIMIT = 5000

# Expense categories
CATEGORIES = [
    'Food',
    'Transportation',
    'Entertainment',
    'Utilities',
    'Healthcare',
    'Shopping',
    'Education',
    'Other'
]

# CSV column names
CSV_COLUMNS = ['Date', 'Category', 'Amount', 'Note']

# Budget warning threshold (percentage of budget)
# Alert when spending exceeds this percentage
BUDGET_WARNING_THRESHOLD = 0.80  # 80% of budget

# Date format for user input
DATE_FORMAT = '%Y-%m-%d'  # Example: 2024-01-15

# Currency symbol for display
CURRENCY_SYMBOL = '$'
