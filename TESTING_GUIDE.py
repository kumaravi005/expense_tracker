"""
TESTING & VALIDATION GUIDE

This document explains how to test each component of the Expense Tracker
to ensure everything works correctly.
"""

# ==============================================================================
# UNIT TESTING: Testing Individual Modules
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ UNIT TESTING - Test Each Module Separately                      │
└─────────────────────────────────────────────────────────────────┘

Test 1: config.py
────────────────────────────────────────────────────────────────

Purpose: Verify all configuration values are set correctly

Steps:
1. Open Python interpreter:
   python

2. Run these commands:
   from config import *
   print(CATEGORIES)
   print(MONTHLY_BUDGET_LIMIT)
   print(DATE_FORMAT)

Expected: All constants should display properly
✓ Test passes if values are displayed without errors
""")


print("""
Test 2: expense_manager.py (CSV Operations)
────────────────────────────────────────────────────────────────

Purpose: Verify CSV file creation and data operations

Steps:
1. Open Python interpreter:
   python

2. Run:
   from expense_manager import init_csv, add_expense, get_all_expenses
   init_csv()
   
3. Expected: You should see:
   ✓ Created new data file: expenses.csv
   
4. Check if file exists:
   import os
   os.path.exists('expenses.csv')
   
Expected: Returns True

5. Add test expense:
   add_expense('2024-01-15', 'Food', '50.00', 'Test expense')
   
Expected: You should see:
   ✓ Expense added: Food - 50.0 on 2024-01-15

6. Retrieve expenses:
   expenses = get_all_expenses()
   print(expenses)
   
Expected: List with your added expense

✓ Test passes if all operations work without errors
""")


print("""
Test 3: analysis.py (Pandas Analysis)
────────────────────────────────────────────────────────────────

Purpose: Verify data analysis functions work correctly

Prerequisites: You should have data in CSV from Test 2

Steps:
1. Open Python interpreter:
   python

2. Run:
   from analysis import load_data, total_spending, category_wise_spending
   
3. Load data:
   df = load_data()
   print(df)
   
Expected: DataFrame printed with expense data

4. Calculate total:
   total = total_spending()
   print(f'Total: ${total:.2f}')
   
Expected: Shows total amount

5. Category breakdown:
   cat_spend = category_wise_spending()
   print(cat_spend)
   
Expected: Categories with amounts

6. Test filtering:
   from analysis import filter_by_category
   food_expenses = filter_by_category('Food')
   print(food_expenses)
   
Expected: Only Food category expenses shown

✓ Test passes if all calculations are correct
""")


print("""
Test 4: visualization.py (Charts)
────────────────────────────────────────────────────────────────

Purpose: Verify charting functions create visualizations

Prerequisites: You should have data in CSV

Steps:
1. Open Python interpreter:
   python

2. Run:
   from visualization import plot_category_bar_chart
   plot_category_bar_chart()
   
Expected: Bar chart window opens showing category spending

3. Close chart window and try:
   from visualization import plot_category_pie_chart
   plot_category_pie_chart()
   
Expected: Pie chart opens

4. Try monthly trend:
   from visualization import plot_monthly_trend
   plot_monthly_trend()
   
Expected: Line chart opens

✓ Test passes if all charts display correctly
""")


# ==============================================================================
# INTEGRATION TESTING: Test Modules Working Together
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ INTEGRATION TESTING - Test Complete Workflows                   │
└─────────────────────────────────────────────────────────────────┘

Workflow 1: Add → View → Filter → Delete
────────────────────────────────────────────────────────────────

1. Start application:
   python app.py

2. Add expense:
   Select: 1 (Add Expense)
   Date: 2024-01-15
   Category: Food
   Amount: 45.50
   Note: Test lunch
   
   Expected: ✓ Expense added

3. View all:
   Select: 2 (View All Expenses)
   Expected: Table shows your expense

4. Filter by category:
   Select: 9 (Filter by Category)
   Category: Food
   Expected: Shows Food expenses

5. Delete:
   Select: 4 (Delete Expense)
   Row number: 0
   Expected: ✓ Expense deleted

6. Verify deleted:
   Select: 2 (View All Expenses)
   Expected: Expense no longer shows

✓ Workflow passes if all steps work correctly
""")


print("""
Workflow 2: Add Multiple → Analyze → Generate Report
────────────────────────────────────────────────────────────────

1. Generate sample data:
   python generate_sample_data.py
   
   Response: yes
   Expected: ✓ Successfully generated X sample expenses

2. Run application:
   python app.py

3. View summary report:
   Select: 5 (View Summary Report)
   
   Expected: Detailed statistics displayed

4. View category breakdown:
   Select: 6 (Category-wise Spending)
   
   Expected: All categories with amounts shown

5. View monthly trends:
   Select: 7 (Monthly Spending Trends)
   
   Expected: Monthly data displayed

6. View charts:
   Select: 12 (View Visualizations)
   Choose: 1-5
   
   Expected: Charts display

✓ Workflow passes if all data analysis works
""")


# ==============================================================================
# SYSTEM TESTING: Test Complete Application
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ SYSTEM TESTING - Full Application Test                          │
└─────────────────────────────────────────────────────────────────┘

Test Scenario 1: Fresh Install
────────────────────────────────────────────────────────────────

1. Delete old expenses.csv (if exists)
   
2. Start app:
   python app.py
   
   Expected: 
   - CSV file created ✓
   - Menu displays ✓
   
3. Add 5 expenses with different categories

4. Generate report
   
   Expected:
   - Shows 5 expenses ✓
   - Shows multiple categories ✓
   
✓ Test passes if fresh install works smoothly
""")


print("""
Test Scenario 2: Web Application (Streamlit)
────────────────────────────────────────────────────────────────

1. Generate sample data:
   python generate_sample_data.py

2. Start Streamlit:
   streamlit run streamlit_app.py

   Expected: Browser opens at http://localhost:8501

3. Verify all pages load:
   - Dashboard page ✓
   - Add Expense page ✓
   - View Expenses page ✓
   - Analysis page ✓
   - Reports page ✓

4. Test Dashboard:
   - Check metrics display ✓
   - Charts appear ✓
   - Budget status shows ✓

5. Test Add Expense:
   - Form displays ✓
   - Can submit ✓
   - Dashboard updates ✓

6. Test View Expenses:
   - Table displays ✓
   - Can download CSV ✓

7. Test Analysis tabs:
   - Category tab works ✓
   - Date range tab works ✓
   - Month tab works ✓
   - Statistics tab works ✓

✓ Test passes if all pages work correctly
""")


# ==============================================================================
# DATA VALIDATION TESTING
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ DATA VALIDATION TESTING - Verify Error Handling                 │
└─────────────────────────────────────────────────────────────────┘

Test 1: Invalid Date Format
────────────────────────────────────────────────────────────────

Steps:
1. Run CLI: python app.py
2. Select: 1 (Add Expense)
3. Enter date: 15-01-2024 (wrong format)

Expected: 
✗ Invalid date format. Use %Y-%m-%d
Expense NOT added

✓ Test passes if error is shown and data not added
""")


print("""
Test 2: Invalid Category
────────────────────────────────────────────────────────────────

Steps:
1. Run CLI: python app.py
2. Select: 1 (Add Expense)
3. Date: 2024-01-15 ✓
4. Category: InvalidCategory

Expected:
✗ Invalid category. Choose from: Food, Transportation, ...
Expense NOT added

✓ Test passes if error shown
""")


print("""
Test 3: Invalid Amount
────────────────────────────────────────────────────────────────

Steps:
1. Run CLI: python app.py
2. Select: 1 (Add Expense)
3. Date: 2024-01-15 ✓
4. Category: Food ✓
5. Amount: -50 (negative)

Expected:
✗ Amount must be positive
Expense NOT added

✓ Test passes if negative amount rejected
""")


print("""
Test 4: Non-numeric Amount
────────────────────────────────────────────────────────────────

Steps:
1. Run CLI: python app.py
2. Select: 1 (Add Expense)
3. Date: 2024-01-15 ✓
4. Category: Food ✓
5. Amount: abc

Expected:
✗ Amount must be a number
Expense NOT added

✓ Test passes if non-numeric rejected
""")


# ==============================================================================
# BOUNDARY TESTING
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ BOUNDARY TESTING - Test Edge Cases                              │
└─────────────────────────────────────────────────────────────────┘

Test 1: Very Small Amount
────────────────────────────────────────────────────────────────

Add expense with amount: 0.01
Expected: ✓ Added successfully

✓ Test passes if minimum amount accepted

Test 2: Very Large Amount
────────────────────────────────────────────────────────────────

Add expense with amount: 99999.99
Expected: ✓ Added successfully

✓ Test passes if large amount accepted

Test 3: Decimal Precision
────────────────────────────────────────────────────────────────

Add expense with amount: 45.567 (3 decimals)
Expected: Stored as 45.57 (rounded to 2 places)

✓ Test passes if properly rounded

Test 4: Very Long Note
────────────────────────────────────────────────────────────────

Add expense with very long note (100+ characters)
Expected: ✓ Stored successfully
✓ Displays properly in table

Test 5: Special Characters in Note
────────────────────────────────────────────────────────────────

Note: "Lunch @ restaurant! Cost was ¥50 & tip 10%"
Expected: ✓ Stored and displayed correctly

✓ Test passes if special chars handled
""")


# ==============================================================================
# PERFORMANCE TESTING
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ PERFORMANCE TESTING - Check Speed & Efficiency                  │
└─────────────────────────────────────────────────────────────────┘

Test 1: Large Dataset Performance
────────────────────────────────────────────────────────────────

1. Generate sample data for 12 months:
   - Modify generate_sample_data.py
   - Change: generate_sample_data(num_months=12)
   
2. Run app and test:
   - Menu navigation: <100ms ✓
   - View all expenses: <500ms ✓
   - Generate report: <1000ms ✓
   - Create charts: <2000ms ✓

✓ Test passes if app remains responsive

Test 2: Repeated Operations
────────────────────────────────────────────────────────────────

1. Add 100 expenses rapidly
2. View all expenses
3. Generate charts

Expected: No slowdown or memory issues

✓ Test passes if stable throughout
""")


# ==============================================================================
# COMPATIBILITY TESTING
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ COMPATIBILITY TESTING - Verify Cross-Platform                   │
└─────────────────────────────────────────────────────────────────┘

Test on Windows
────────────────────────────────────────────────────────────────
- CMD/PowerShell command works ✓
- File paths work correctly ✓
- Charts display in Windows ✓

Test on macOS
────────────────────────────────────────────────────────────────
- Terminal commands work ✓
- File paths work correctly ✓
- Streamlit displays properly ✓

Test on Linux
────────────────────────────────────────────────────────────────
- Terminal commands work ✓
- File paths work correctly ✓
- All features functional ✓

✓ All platforms compatible
""")


# ==============================================================================
# USER ACCEPTANCE TESTING
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ USER ACCEPTANCE TESTING - Real-World Usage                      │
└─────────────────────────────────────────────────────────────────┘

Real Scenario: Monthly Expense Tracking
────────────────────────────────────────────────────────────────

Day 1: Start tracking
  □ Add expense: Coffee ($5)
  □ View it displays correctly

Day 5: Track multiple categories
  □ Add: Food ($45)
  □ Add: Transport ($20)
  □ Add: Entertainment ($30)
  □ View summary by category
  □ All amounts correct

Day 15: Check budget status
  □ Check monthly spending
  □ Still within budget
  □ Budget warning not triggered

Day 28: End of month recap
  □ Generate full report
  □ View all categories
  □ Check which category highest
  □ Analyze trends
  □ Compare to last month

Expected: All functionality works seamlessly

✓ Test passes if real usage works smoothly
""")


# ==============================================================================
# TESTING CHECKLIST
# ==============================================================================

print("""
╔═════════════════════════════════════════════════════════════════╗
║ FINAL TESTING CHECKLIST                                         ║
╚═════════════════════════════════════════════════════════════════╝

UNIT TESTS (Each module):
☐ config.py - Constants accessible
☐ expense_manager.py - CSV operations work
☐ analysis.py - Calculations correct
☐ visualization.py - Charts appear
☐ app.py - CLI runs
☐ streamlit_app.py - Web app displays

INTEGRATION TESTS (Workflows):
☐ Add → View → Delete works
☐ Add multiple → Analyze works
☐ Data persists across sessions
☐ Charts use accurate data

SYSTEM TESTS (Full app):
☐ Fresh install works
☐ CLI app complete workflow
☐ Streamlit app complete workflow
☐ All pages/tabs functional

VALIDATION TESTS (Error handling):
☐ Invalid dates rejected
☐ Invalid categories rejected
☐ Invalid amounts rejected
☐ Non-numeric input rejected

BOUNDARY TESTS (Edge cases):
☐ Minimum amount (0.01)
☐ Maximum amount (99999.99)
☐ Decimal precision (2 places)
☐ Long notes (100+ chars)
☐ Special characters in notes

PERFORMANCE TESTS (Speed):
☐ Menu responsive (<100ms)
☐ Data display fast (<500ms)
☐ Reports generate quickly (<1s)
☐ Large datasets handled

✓ All tests passing = Production Ready!

═════════════════════════════════════════════════════════════════
""")


if __name__ == "__main__":
    print("\n" + "="*65)
    print("📋 TESTING GUIDE FOR PERSONAL EXPENSE TRACKER")
    print("="*65 + "\n")
    
    print("This guide helps you test every part of the application.\n")
    print("Follow the tests above to verify all functionality works!")
    print("\nQuick test checklist:")
    print("✓ Run: python app.py")
    print("✓ Add some expenses")
    print("✓ View reports")
    print("✓ Check budget status")
    print("✓ Run: streamlit run streamlit_app.py")
    print("✓ Explore dashboard")
    print("\nIf all tests pass, your app is ready! 🚀")
