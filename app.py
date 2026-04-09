"""
Main CLI Application for Expense Tracker.

This is the entry point that brings all modules together.
Provides an interactive menu for users to add, view, analyze expenses.

Why CLI first?
- Easy to test and debug
- Works without external dependencies
- Foundation for Streamlit app
"""

import os
from datetime import datetime
from expense_manager import (
    init_csv, add_expense, get_all_expenses, 
    edit_expense, delete_expense, display_expenses
)
from analysis import (
    total_spending, category_wise_spending, monthly_spending,
    average_expense, highest_expense, lowest_expense,
    filter_by_category, filter_by_date_range, filter_by_month,
    monthly_budget_status, generate_summary_report,
    get_statistics_dict
)
from visualization import (
    plot_category_bar_chart, plot_category_pie_chart,
    plot_monthly_trend, plot_budget_gauge, show_all_charts_interactive,
    create_dashboard_image
)
from config import CATEGORIES, DATE_FORMAT, CURRENCY_SYMBOL


class ExpenseTrackerApp:
    """
    Main application class that manages the CLI interface.
    
    Design Pattern: Class-based approach allows:
    - Organize related methods together
    - Maintain state (if needed)
    - Easy to test individual functions
    """
    
    def __init__(self):
        """Initialize the application."""
        self.running = True
    
    def clear_screen(self):
        """Clear console screen for better readability."""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_header(self, title):
        """Print a formatted header."""
        print("\n" + "=" * 70)
        print(f"  {title}")
        print("=" * 70 + "\n")
    
    def print_menu(self):
        """Display main menu options."""
        self.print_header("PERSONAL EXPENSE TRACKER")
        print("""
    1.  Add Expense
    2.  View All Expenses
    3.  Edit Expense
    4.  Delete Expense
    
    5.  View Summary Report
    6.  Category-wise Spending
    7.  Monthly Spending Trends
    8.  Budget Status
    
    9.  Filter by Category
    10. Filter by Date Range
    11. Filter by Month
    
    12. View Visualizations
    13. Create Dashboard
    
    0.  Exit
        """)
    
    def menu_add_expense(self):
        """Handle adding a new expense."""
        self.print_header("ADD NEW EXPENSE")
        
        try:
            print(f"Available categories: {', '.join(CATEGORIES)}\n")
            
            # Get inputs from user
            date = input(f"Enter date ({DATE_FORMAT}): ").strip()
            category = input("Enter category: ").strip()
            amount = input("Enter amount: ").strip()
            note = input("Enter note (optional): ").strip()
            
            # Add expense
            add_expense(date, category, amount, note)
            
            input("\nPress Enter to continue...")
            
        except Exception as e:
            print(f"Error: {e}")
            input("Press Enter to continue...")
    
    def menu_view_all(self):
        """Display all expenses."""
        self.print_header("ALL EXPENSES")
        expenses = get_all_expenses()
        display_expenses(expenses)
        input("Press Enter to continue...")
    
    def menu_edit_expense(self):
        """Handle editing an expense."""
        self.print_header("EDIT EXPENSE")
        
        try:
            expenses = get_all_expenses()
            if not expenses:
                print("No expenses to edit")
                input("Press Enter to continue...")
                return
            
            # Show all expenses with row numbers
            for idx, expense in enumerate(expenses):
                print(f"{idx}: {expense['Date']} - {expense['Category']} - {CURRENCY_SYMBOL}{expense['Amount']}")
            
            row_num = int(input("\nEnter row number to edit: "))
            
            print(f"\nCurrent: {expenses[row_num]}")
            print(f"Available categories: {', '.join(CATEGORIES)}\n")
            
            date = input(f"New date ({DATE_FORMAT}): ").strip()
            category = input("New category: ").strip()
            amount = input("New amount: ").strip()
            note = input("New note: ").strip()
            
            edit_expense(row_num, date, category, amount, note)
            input("\nPress Enter to continue...")
            
        except (ValueError, IndexError) as e:
            print(f"Error: Invalid input - {e}")
            input("Press Enter to continue...")
    
    def menu_delete_expense(self):
        """Handle deleting an expense."""
        self.print_header("DELETE EXPENSE")
        
        try:
            expenses = get_all_expenses()
            if not expenses:
                print("No expenses to delete")
                input("Press Enter to continue...")
                return
            
            # Show all expenses
            for idx, expense in enumerate(expenses):
                print(f"{idx}: {expense['Date']} - {expense['Category']} - {CURRENCY_SYMBOL}{expense['Amount']}")
            
            row_num = int(input("\nEnter row number to delete: "))
            
            delete_expense(row_num)
            input("\nPress Enter to continue...")
            
        except (ValueError, IndexError) as e:
            print(f"Error: Invalid input - {e}")
            input("Press Enter to continue...")
    
    def menu_summary_report(self):
        """Display comprehensive summary report."""
        self.print_header("SUMMARY REPORT")
        report = generate_summary_report()
        print(report)
        input("Press Enter to continue...")
    
    def menu_category_spending(self):
        """Show category-wise spending breakdown."""
        self.print_header("CATEGORY-WISE SPENDING")
        
        cat_spending = category_wise_spending()
        
        if cat_spending.empty:
            print("No expenses recorded yet")
        else:
            total = cat_spending.sum()
            print(f"{'Category':<20} {'Amount':>15} {'Percentage':>15}")
            print("-" * 50)
            
            for category, amount in cat_spending.items():
                percentage = (amount / total * 100) if total > 0 else 0
                print(f"{category:<20} {CURRENCY_SYMBOL}{amount:>14,.2f} {percentage:>14.1f}%")
            
            print("-" * 50)
            print(f"{'TOTAL':<20} {CURRENCY_SYMBOL}{total:>14,.2f}")
        
        input("\nPress Enter to continue...")
    
    def menu_monthly_trends(self):
        """Show monthly spending trends."""
        self.print_header("MONTHLY SPENDING TRENDS")
        
        monthly = monthly_spending()
        
        if monthly.empty:
            print("No expenses recorded yet")
        else:
            print(f"{'Month':<15} {'Amount':>15}")
            print("-" * 30)
            
            for month, amount in monthly.items():
                print(f"{str(month):<15} {CURRENCY_SYMBOL}{amount:>14,.2f}")
        
        input("\nPress Enter to continue...")
    
    def menu_budget_status(self):
        """Show current month budget status."""
        self.print_header("BUDGET STATUS")
        
        today = datetime.now()
        status = monthly_budget_status(today.year, today.month)
        
        print(f"Current Month: {today.strftime('%B %Y')}\n")
        print(f"Budget Limit:         {CURRENCY_SYMBOL}{status['budget']:,.2f}")
        print(f"Amount Spent:         {CURRENCY_SYMBOL}{status['spent']:,.2f}")
        print(f"Remaining:            {CURRENCY_SYMBOL}{status['remaining']:,.2f}")
        print(f"Percentage Used:      {status['percentage']:.1f}%")
        print(f"\nStatus: {status['status']}")
        
        # Progress bar
        bar_length = 40
        filled = int(bar_length * status['percentage'] / 100)
        bar = '█' * filled + '░' * (bar_length - filled)
        print(f"\nProgress: [{bar}]")
        
        input("\nPress Enter to continue...")
    
    def menu_filter_category(self):
        """Filter expenses by category."""
        self.print_header("FILTER BY CATEGORY")
        
        print(f"Available categories: {', '.join(CATEGORIES)}\n")
        category = input("Enter category: ").strip()
        
        filtered = filter_by_category(category)
        
        if filtered.empty:
            print(f"No expenses found for category: {category}")
        else:
            print(f"\nExpenses in {category}:\n")
            print(f"{'Date':<12} {'Category':<18} {'Amount':>12} {'Note'}")
            print("-" * 70)
            
            for _, row in filtered.iterrows():
                date_str = row['Date'].strftime(DATE_FORMAT)
                print(f"{date_str:<12} {row['Category']:<18} {CURRENCY_SYMBOL}{float(row['Amount']):>11,.2f} {row['Note']}")
            
            total = filtered['Amount'].sum()
            print("-" * 70)
            print(f"Total for {category}: {CURRENCY_SYMBOL}{total:,.2f}")
        
        input("\nPress Enter to continue...")
    
    def menu_filter_date_range(self):
        """Filter expenses by date range."""
        self.print_header("FILTER BY DATE RANGE")
        
        start = input(f"Enter start date ({DATE_FORMAT}): ").strip()
        end = input(f"Enter end date ({DATE_FORMAT}): ").strip()
        
        try:
            filtered = filter_by_date_range(start, end)
            
            if filtered.empty:
                print(f"No expenses found between {start} and {end}")
            else:
                print(f"\nExpenses from {start} to {end}:\n")
                print(f"{'Date':<12} {'Category':<18} {'Amount':>12} {'Note'}")
                print("-" * 70)
                
                for _, row in filtered.iterrows():
                    date_str = row['Date'].strftime(DATE_FORMAT)
                    print(f"{date_str:<12} {row['Category']:<18} {CURRENCY_SYMBOL}{float(row['Amount']):>11,.2f} {row['Note']}")
                
                total = filtered['Amount'].sum()
                print("-" * 70)
                print(f"Total: {CURRENCY_SYMBOL}{total:,.2f}")
        
        except Exception as e:
            print(f"Error: {e}")
        
        input("\nPress Enter to continue...")
    
    def menu_filter_month(self):
        """Filter expenses by specific month."""
        self.print_header("FILTER BY MONTH")
        
        try:
            year = int(input("Enter year (e.g., 2024): "))
            month = int(input("Enter month (1-12): "))
            
            if month < 1 or month > 12:
                print("Invalid month. Please enter 1-12")
                input("Press Enter to continue...")
                return
            
            filtered = filter_by_month(year, month)
            
            if filtered.empty:
                print(f"No expenses found for {month}/{year}")
            else:
                print(f"\nExpenses for {month}/{year}:\n")
                print(f"{'Date':<12} {'Category':<18} {'Amount':>12} {'Note'}")
                print("-" * 70)
                
                for _, row in filtered.iterrows():
                    date_str = row['Date'].strftime(DATE_FORMAT)
                    print(f"{date_str:<12} {row['Category']:<18} {CURRENCY_SYMBOL}{float(row['Amount']):>11,.2f} {row['Note']}")
                
                total = filtered['Amount'].sum()
                print("-" * 70)
                print(f"Total: {CURRENCY_SYMBOL}{total:,.2f}")
        
        except ValueError:
            print("Error: Invalid input")
        
        input("\nPress Enter to continue...")
    
    def menu_visualizations(self):
        """Display visualization options."""
        while True:
            self.clear_screen()
            self.print_header("DATA VISUALIZATIONS")
            
            print("""
    1. Category-wise Bar Chart
    2. Expense Distribution Pie Chart
    3. Monthly Spending Trend
    4. Budget Gauge Chart
    5. All Charts (Interactive)
    0. Back to Main Menu
            """)
            
            choice = input("Select option: ").strip()
            
            try:
                if choice == '1':
                    plot_category_bar_chart()
                elif choice == '2':
                    plot_category_pie_chart()
                elif choice == '3':
                    plot_monthly_trend()
                elif choice == '4':
                    today = datetime.now()
                    plot_budget_gauge(today.year, today.month)
                elif choice == '5':
                    show_all_charts_interactive()
                elif choice == '0':
                    break
                else:
                    print("Invalid option")
                    input("Press Enter to continue...")
            
            except Exception as e:
                print(f"Error displaying chart: {e}")
                input("Press Enter to continue...")
    
    def menu_dashboard(self):
        """Create and display comprehensive dashboard."""
        self.print_header("CREATING DASHBOARD...")
        
        try:
            create_dashboard_image('expense_dashboard.png')
            print("\n✓ Dashboard created successfully!")
            print("Saved as: expense_dashboard.png")
        except Exception as e:
            print(f"Error creating dashboard: {e}")
        
        input("\nPress Enter to continue...")
    
    def run(self):
        """Main application loop."""
        # Initialize CSV on startup
        init_csv()
        
        while self.running:
            self.clear_screen()
            self.print_menu()
            
            choice = input("Select option: ").strip()
            
            if choice == '1':
                self.menu_add_expense()
            elif choice == '2':
                self.menu_view_all()
            elif choice == '3':
                self.menu_edit_expense()
            elif choice == '4':
                self.menu_delete_expense()
            elif choice == '5':
                self.menu_summary_report()
            elif choice == '6':
                self.menu_category_spending()
            elif choice == '7':
                self.menu_monthly_trends()
            elif choice == '8':
                self.menu_budget_status()
            elif choice == '9':
                self.menu_filter_category()
            elif choice == '10':
                self.menu_filter_date_range()
            elif choice == '11':
                self.menu_filter_month()
            elif choice == '12':
                self.menu_visualizations()
            elif choice == '13':
                self.menu_dashboard()
            elif choice == '0':
                print("\nThank you for using Expense Tracker!")
                print("Your data has been saved.\n")
                self.running = False
            else:
                print("Invalid option. Please try again.")
                input("Press Enter to continue...")


def main():
    """Entry point of the application."""
    app = ExpenseTrackerApp()
    app.run()


if __name__ == "__main__":
    main()
