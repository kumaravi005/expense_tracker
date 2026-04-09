"""
Data Analysis module using Pandas.

Why Pandas?
- Built for data analysis and manipulation
- Handles CSV files efficiently
- Easy grouping, sorting, filtering
- Automatic calculations (sum, mean, etc.)
- integrates well with visualization libraries

This module performs calculations and analysis on expense data.
"""

import pandas as pd
from datetime import datetime
from config import DATA_FILE, DATE_FORMAT, MONTHLY_BUDGET_LIMIT, CURRENCY_SYMBOL


def load_data():
    """
    Load expense data from CSV into a Pandas DataFrame.
    
    Why DataFrame?
    - Like Excel spreadsheet in Python
    - Each column has a name
    - Can perform SQL-like operations
    - Easy to calculate statistics
    
    Returns:
        pd.DataFrame: Empty DataFrame if file doesn't exist or is empty
    """
    try:
        df = pd.read_csv(DATA_FILE)
        # Convert 'Date' column to datetime for easier date operations
        df['Date'] = pd.to_datetime(df['Date'])
        # Convert 'Amount' to float for calculations
        df['Amount'] = pd.to_numeric(df['Amount'])
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Note'])
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Note'])


def total_spending():
    """
    Calculate total spending across all expenses.
    
    Returns:
        float: Total amount spent
    """
    df = load_data()
    if df.empty:
        return 0
    return df['Amount'].sum()


def category_wise_spending():
    """
    Calculate total spending for each category.
    
    Returns:
        pd.Series: Category names as index, total amount as values
        
    Example:
        Food                100.50
        Transportation       45.00
        Entertainment        30.00
    """
    df = load_data()
    if df.empty:
        return pd.Series()
    
    # groupby(): Group rows by category, then sum amounts
    category_spending = df.groupby('Category')['Amount'].sum()
    # sort_values(ascending=False): Sort from highest to lowest spending
    return category_spending.sort_values(ascending=False)


def monthly_spending():
    """
    Calculate spending for each month.
    
    How:
    - Extract year-month from Date column
    - Group by month
    - Sum amounts for each month
    
    Returns:
        pd.Series: Month as index, total amount as values
    """
    df = load_data()
    if df.empty:
        return pd.Series()
    
    # dt.to_period('M'): Convert dates to month period (e.g., "2024-01")
    monthly = df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum()
    return monthly


def average_expense():
    """
    Calculate average expense amount.
    
    Returns:
        float: Average amount per transaction
    """
    df = load_data()
    if df.empty or len(df) == 0:
        return 0
    return df['Amount'].mean()


def highest_expense():
    """
    Find the highest single expense.
    
    Returns:
        tuple: (amount, category, date, note)
    """
    df = load_data()
    if df.empty:
        return (0, "N/A", "N/A", "N/A")
    
    # idxmax(): Get index of maximum value
    max_idx = df['Amount'].idxmax()
    max_row = df.loc[max_idx]
    
    return (
        max_row['Amount'],
        max_row['Category'],
        max_row['Date'].strftime(DATE_FORMAT),
        max_row['Note']
    )


def lowest_expense():
    """
    Find the lowest single expense.
    
    Returns:
        tuple: (amount, category, date, note)
    """
    df = load_data()
    if df.empty:
        return (0, "N/A", "N/A", "N/A")
    
    min_idx = df['Amount'].idxmin()
    min_row = df.loc[min_idx]
    
    return (
        min_row['Amount'],
        min_row['Category'],
        min_row['Date'].strftime(DATE_FORMAT),
        min_row['Note']
    )


def filter_by_category(category):
    """
    Get all expenses for a specific category.
    
    Args:
        category (str): Category name to filter
    
    Returns:
        pd.DataFrame: Filtered expenses
    """
    df = load_data()
    if df.empty:
        return df
    
    # df['Category'] == category: Create boolean mask (True/False for each row)
    # df[mask]: Keep only rows where mask is True
    filtered = df[df['Category'] == category]
    return filtered


def filter_by_date_range(start_date, end_date):
    """
    Get expenses within a date range.
    
    Args:
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
    
    Returns:
        pd.DataFrame: Filtered expenses
    """
    df = load_data()
    if df.empty:
        return df
    
    # Convert string dates to datetime for comparison
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)
    
    # Filter rows where Date >= start_date AND Date <= end_date
    filtered = df[(df['Date'] >= start) & (df['Date'] <= end)]
    return filtered


def filter_by_month(year, month):
    """
    Get expenses for a specific month.
    
    Args:
        year (int): Year (e.g., 2024)
        month (int): Month (1-12)
    
    Returns:
        pd.DataFrame: Filtered expenses
    """
    df = load_data()
    if df.empty:
        return df
    
    # Extract year and month from Date column
    # dt.year: Year of each date
    # dt.month: Month of each date
    filtered = df[(df['Date'].dt.year == year) & (df['Date'].dt.month == month)]
    return filtered


def monthly_budget_status(year, month):
    """
    Check spending against budget for a specific month.
    
    Returns:
        dict: Contains 'spent', 'budget', 'remaining', 'percentage', 'status'
    """
    month_data = filter_by_month(year, month)
    spent = month_data['Amount'].sum() if not month_data.empty else 0
    
    remaining = MONTHLY_BUDGET_LIMIT - spent
    percentage = (spent / MONTHLY_BUDGET_LIMIT * 100) if MONTHLY_BUDGET_LIMIT > 0 else 0
    
    # Determine status based on spending percentage
    if percentage >= 100:
        status = "🔴 OVER BUDGET"
    elif percentage >= 80:
        status = "🟠 WARNING - Near budget limit"
    else:
        status = "🟢 Within budget"
    
    return {
        'spent': round(spent, 2),
        'budget': MONTHLY_BUDGET_LIMIT,
        'remaining': round(remaining, 2),
        'percentage': round(percentage, 1),
        'status': status
    }


def generate_summary_report():
    """
    Generate a comprehensive summary report of all expenses.
    
    Returns:
        str: Formatted report text
    """
    df = load_data()
    
    report = "\n" + "=" * 60 + "\n"
    report += "EXPENSE SUMMARY REPORT\n"
    report += "=" * 60 + "\n\n"
    
    if df.empty:
        report += "No expenses recorded yet.\n"
        report += "=" * 60 + "\n"
        return report
    
    # Overall Statistics
    report += "📊 OVERALL STATISTICS\n"
    report += "-" * 60 + "\n"
    report += f"Total Expenses:        {len(df)}\n"
    report += f"Total Amount Spent:    {CURRENCY_SYMBOL}{total_spending():,.2f}\n"
    report += f"Average per Expense:   {CURRENCY_SYMBOL}{average_expense():,.2f}\n"
    report += f"Highest Expense:       {CURRENCY_SYMBOL}{highest_expense()[0]:,.2f} ({highest_expense()[1]})\n"
    report += f"Lowest Expense:        {CURRENCY_SYMBOL}{lowest_expense()[0]:,.2f} ({lowest_expense()[1]})\n"
    report += f"Date Range:            {df['Date'].min().strftime(DATE_FORMAT)} to {df['Date'].max().strftime(DATE_FORMAT)}\n\n"
    
    # Category Breakdown
    report += "💰 CATEGORY BREAKDOWN\n"
    report += "-" * 60 + "\n"
    for category, amount in category_wise_spending().items():
        percentage = (amount / total_spending() * 100) if total_spending() > 0 else 0
        report += f"{category:<20} {CURRENCY_SYMBOL}{amount:>10,.2f}  ({percentage:>5.1f}%)\n"
    
    report += "\n" + "=" * 60 + "\n"
    return report


def get_statistics_dict():
    """
    Return all statistics as a dictionary.
    Useful for Streamlit dashboard.
    
    Returns:
        dict: All calculated statistics
    """
    df = load_data()
    
    return {
        'total_expenses': len(df),
        'total_spending': round(total_spending(), 2),
        'average_expense': round(average_expense(), 2),
        'highest_expense': highest_expense(),
        'lowest_expense': lowest_expense(),
        'category_spending': category_wise_spending().to_dict(),
        'monthly_spending': monthly_spending().to_dict(),
        'is_empty': df.empty
    }
