"""
Sample Data Generator for Testing.

This script generates sample expense data for testing and demonstration.
Useful for quickly populating the app with data to see visualizations.

Run this once to populate sample data, then use the app normally.
"""

from datetime import datetime, timedelta
import random
from expense_manager import init_csv, add_expense
from config import CATEGORIES


def generate_sample_data(num_months=3):
    """
    Generate sample expense data.
    
    Args:
        num_months (int): Number of months of data to generate
    """
    print(f"Generating {num_months} months of sample expense data...\n")
    
    # Initialize CSV
    init_csv()
    
    # Sample notes for different categories
    notes_by_category = {
        'Food': ['Breakfast', 'Lunch', 'Dinner', 'Snacks', 'Groceries', 'Coffee'],
        'Transportation': ['Uber', 'Taxi', 'Gas', 'Train', 'Bus', 'Parking'],
        'Entertainment': ['Movie', 'Concert', 'Gaming', 'Streaming', 'Books', 'Dining out'],
        'Utilities': ['Electricity', 'Water', 'Internet', 'Phone', 'Rent'],
        'Healthcare': ['Doctor', 'Pharmacy', 'Gym', 'Checkup', 'Dentist'],
        'Shopping': ['Clothes', 'Electronics', 'Shoes', 'Accessories', 'Gifts'],
        'Education': ['Course', 'Books', 'Tuition', 'Workshop', 'Training'],
        'Other': ['Donation', 'Subscription', 'Misc', 'Pet', 'Repair']
    }
    
    # Generate data
    start_date = datetime.now() - timedelta(days=30 * num_months)
    current_date = start_date
    expenses_added = 0
    
    while current_date <= datetime.now():
        # Add 0-3 expenses per day
        num_expenses = random.randint(0, 3)
        
        for _ in range(num_expenses):
            # Random category
            category = random.choice(CATEGORIES)
            
            # Random amount based on category
            if category == 'Food':
                amount = round(random.uniform(5, 50), 2)
            elif category == 'Transportation':
                amount = round(random.uniform(10, 30), 2)
            elif category == 'Entertainment':
                amount = round(random.uniform(20, 100), 2)
            elif category == 'Utilities':
                amount = round(random.uniform(50, 200), 2)
            elif category == 'Healthcare':
                amount = round(random.uniform(30, 150), 2)
            elif category == 'Shopping':
                amount = round(random.uniform(20, 100), 2)
            elif category == 'Education':
                amount = round(random.uniform(50, 200), 2)
            else:  # Other
                amount = round(random.uniform(10, 80), 2)
            
            # Random note
            note = random.choice(notes_by_category.get(category, ['Misc']))
            
            # Add expense
            date_str = current_date.strftime('%Y-%m-%d')
            add_expense(date_str, category, amount, note)
            
            expenses_added += 1
        
        current_date += timedelta(days=1)
    
    print(f"✓ Successfully generated {expenses_added} sample expenses!")
    print("\nSample expense data added. You can now:")
    print("  1. Run 'python app.py' for CLI")
    print("  2. Run 'streamlit run streamlit_app.py' for web app")
    print("  3. View visualizations and reports")


if __name__ == "__main__":
    print("=" * 60)
    print("SAMPLE DATA GENERATOR")
    print("=" * 60)
    print()
    print("This will generate 3 months of sample expense data.")
    print("WARNING: This will ADD to existing data.")
    print()
    
    proceed = input("Continue? (yes/no): ").strip().lower()
    
    if proceed == 'yes':
        try:
            generate_sample_data()
            print("\n" + "=" * 60)
            print("✓ Done! Your app is ready to explore.")
            print("=" * 60)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Cancelled.")
