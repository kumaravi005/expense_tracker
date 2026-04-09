"""
QUICK START GUIDE FOR PERSONAL EXPENSE TRACKER

Follow these steps to get your expense tracker running in 5 minutes!
"""

# ==============================================================================
# STEP 1: INSTALL DEPENDENCIES
# ==============================================================================

# Open terminal/command prompt and run:
# pip install -r requirements.txt

# This installs:
# - pandas (data analysis)
# - matplotlib, seaborn (visualization)
# - plotly (interactive charts)  
# - streamlit (web app)

print("""
┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: Install Dependencies                                    │
└─────────────────────────────────────────────────────────────────┘

Run this command:
    pip install -r requirements.txt

Wait for installation to complete (1-2 minutes).
✓ You'll see "Successfully installed" message.
""")


# ==============================================================================
# STEP 2: CHOOSE YOUR INTERFACE
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ STEP 2: Pick Your Interface                                     │
└─────────────────────────────────────────────────────────────────┘

OPTION A: Command Line Interface (CLI) - Simple & Direct
    python app.py
    
    Pros: Easy to learn, works everywhere, fast
    Best for: Learning, testing, quick data entry

OPTION B: Web Application (Streamlit) - Beautiful & Interactive
    streamlit run streamlit_app.py
    
    Pros: Professional looking, great visuals, fun to use
    Best for: Analysis, sharing with others, demos

Choose what you want to do:
1. Start with CLI? → Go to STEP 3A
2. Start with Streamlit? → Go to STEP 3B
3. Try both? → Start with CLI, then try Streamlit
""")


# ==============================================================================
# STEP 3A: RUN CLI APPLICATION
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ STEP 3A: Using Command Line Interface                           │
└─────────────────────────────────────────────────────────────────┘

1. Open terminal and run:
    python app.py

2. You'll see main menu:
    1. Add Expense
    2. View All Expenses
    3. Edit Expense
    ... etc

3. Start by adding expenses:
    - Select option 1
    - Enter date: 2024-01-15
    - Enter category: Food
    - Enter amount: 45.50
    - Enter note: Lunch
    
4. After adding few expenses, try:
    - Option 2: View all expenses
    - Option 5: See summary report
    - Option 12: View charts
    
5. Press 0 to exit

TIP: Don't worry about making mistakes - you can edit or delete!
""")


# ==============================================================================
# STEP 3B: RUN WEB APPLICATION
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ STEP 3B: Using Web Application (Streamlit)                      │
└─────────────────────────────────────────────────────────────────┘

1. Open terminal and run:
    streamlit run streamlit_app.py

2. Web browser automatically opens at:
    http://localhost:8501

3. You'll see dashboard with multiple tabs:
    - Dashboard: Overview with charts
    - Add Expense: Form to add expenses
    - View Expenses: Table of all expenses
    - Analysis: Advanced filtering
    - Reports: Export data

4. Start by:
    - Click "Add Expense" tab
    - Fill the form
    - Click "Add Expense" button
    - Go back to Dashboard to see updates

5. Explore other tabs and features!

TIP: The web app auto-refreshes when you close it and reopen!
""")


# ==============================================================================
# STEP 4: GENERATING SAMPLE DATA (OPTIONAL)
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ STEP 4: Generate Sample Data (Optional)                         │
└─────────────────────────────────────────────────────────────────┘

To quickly see how the app works with data, generate samples:

Run this command:
    python generate_sample_data.py

This creates 3 months of realistic sample expenses!

After generating:
1. Run CLI: python app.py
   - View reports with lots of data
   - See impressive visualizations

2. Run Streamlit: streamlit run streamlit_app.py
   - Beautiful dashboard with charts
   - Analyze the sample data
""")


# ==============================================================================
# STEP 5: EXPLORING THE CODE
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ STEP 5: Understanding the Code Structure                        │
└─────────────────────────────────────────────────────────────────┘

Project has 6 main Python files:

1. config.py (Settings)
   └─ Contains: Budget limit, categories, date format
   └─ Read this first to understand configuration

2. expense_manager.py (Data Storage)
   └─ Functions: add_expense(), get_all_expenses(), edit_expense()
   └─ Handles CSV file operations

3. analysis.py (Pandas Analysis)
   └─ Functions: category_wise_spending(), monthly_trends()
   └─ Does calculations and filtering

4. visualization.py (Charts & Graphs)
   └─ Functions: plot_category_bar_chart(), plot_pie_chart()
   └─ Creates visual representations

5. app.py (CLI Application)
   └─ Complete menu-driven interface
   └─ Brings all modules together

6. streamlit_app.py (Web Application)
   └─ Beautiful web interface
   └─ Dashboard and tabs

Each file has detailed comments explaining every function!
""")


# ==============================================================================
# STEP 6: CUSTOMIZATION TIPS
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ STEP 6: Customize for Your Needs                                │
└─────────────────────────────────────────────────────────────────┘

Easy Customizations (No coding needed)

1. Change Budget Limit:
   - Open config.py
   - Find: MONTHLY_BUDGET_LIMIT = 5000
   - Change to your amount: MONTHLY_BUDGET_LIMIT = 3000
   - Save and restart app

2. Add New Category:
   - Open config.py
   - Find CATEGORIES list
   - Add your category: 'Gaming', 'Insurance', etc.
   - Save and restart app

3. Change Currency:
   - Open config.py
   - Find: CURRENCY_SYMBOL = '$'
   - Change to: CURRENCY_SYMBOL = '₹'  (or any symbol)
   - Save and restart app

4. Change Date Format:
   - Open config.py
   - Find: DATE_FORMAT = '%Y-%m-%d'
   - Change to: DATE_FORMAT = '%d-%m-%Y'  (or your format)
   - Save and restart app

After each change, restart the app to see effects!
""")


# ==============================================================================
# STEP 7: TROUBLESHOOTING
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ STEP 7: Common Issues & Solutions                               │
└─────────────────────────────────────────────────────────────────┘

Problem: "ModuleNotFoundError: No module named 'pandas'"
Solution: Run: pip install -r requirements.txt

Problem: "FileNotFoundError: expenses.csv"
Solution: This is normal! CSV is created when you run the app for
          the first time. Just run python app.py again.

Problem: "Port 8501 already in use" (Streamlit)
Solution: Kill the existing process or run:
          streamlit run streamlit_app.py --server.port 8502

Problem: Charts not showing in CLI
Solution: Try Streamlit instead: streamlit run streamlit_app.py

Problem: Module imports not working
Solution: Make sure you're in the right directory (expense_tracker/)
          and using the correct Python environment

Problem: Can't add more than one expense today
Solution: That's normal for our basic setup. Each day can have 
          multiple expenses but they may not display separately
          in summary. This is a feature!
""")


# ==============================================================================
# STEP 8: NEXT STEPS
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ STEP 8: What to Do Next                                         │
└─────────────────────────────────────────────────────────────────┘

Level 1: Get Comfortable (Week 1)
☐ Run the app multiple times
☐ Add 20-30 sample expenses manually
☐ View reports and charts
☐ Try filtering by category/date

Level 2: Understand Code (Week 2)
☐ Read through each Python file
☐ Understand how modules work together
☐ Try modifying values in config.py
☐ Add print statements to understand flow

Level 3: Extend Features (Week 3)
☐ Add new functions to analysis.py
☐ Create new chart types
☐ Add budget alert emails
☐ Export to Excel instead of CSV

Level 4: Build Similar Projects
☐ Fitness tracker (calories, weight)
☐ Study tracker (hours, topics)
☐ Reading tracker (books, pages)
☐ Movie tracker (ratings, genres)
""")


# ==============================================================================
# STEP 9: PROJECT STRUCTURE VISUALIZATION
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ STEP 9: How Everything Works Together                           │
└─────────────────────────────────────────────────────────────────┘

Data Flow:

User Input (app.py)
        ↓
    Validation (config.py)
        ↓
    Storage (expense_manager.py) → CSV File
        ↓
    Analysis (analysis.py)
        ↓
    Visualization (visualization.py)
        ↓
    Display (app.py or streamlit_app.py)


When you add an expense:
1. CLI/Web shows form
2. Data is validated
3. Data is sent to expense_manager
4. CSV file is updated
5. You get confirmation

When you view reports:
1. App calls analysis.py
2. Analysis reads CSV using Pandas
3. Calculations are done
4. Results sent to visualization
5. Charts/tables displayed


When you view charts:
1. Analysis gets data from CSV
2. Visualization creates chart using matplotlib/seaborn
3. Chart displayed to user
""")


# ==============================================================================
# FINAL CHECKLIST
# ==============================================================================

print("""
┌─────────────────────────────────────────────────────────────────┐
│ FINAL CHECKLIST ✓                                               │
└─────────────────────────────────────────────────────────────────┘

Before you start, make sure:
☐ Python 3.8+ installed (python --version)
☐ In correct directory (expense_tracker/)
☐ Dependencies installed (pip install -r requirements.txt)

Quick Start (choose one):
☐ CLI App: python app.py
☐ Web App: streamlit run streamlit_app.py
☐ Generate Data: python generate_sample_data.py

First Time Users:
☐ Run generate_sample_data.py for test data
☐ Then explore the app with populated data
☐ Read comments in code for learning

Stuck?
☐ Check README.md for detailed explanations
☐ Read code comments and docstrings
☐ Check troubleshooting section above
☐ Run sample data generator for examples

Ready? Let's go! 🚀
""")


# ==============================================================================
# QUICK REFERENCE
# ==============================================================================

print("""
╔═════════════════════════════════════════════════════════════════╗
║ QUICK REFERENCE GUIDE                                           ║
╚═════════════════════════════════════════════════════════════════╝

COMMANDS TO REMEMBER:

Install dependencies:
    pip install -r requirements.txt

Run CLI app:
    python app.py

Run web app:
    streamlit run streamlit_app.py

Generate sample data:
    python generate_sample_data.py

FILES TO UNDERSTAND:

Read FIRST: README.md
Then READ: config.py (simple settings)
Then READ: expense_manager.py (data operations)
Then READ: analysis.py (Pandas operations)
Then READ: visualization.py (charts)
Finally: app.py (or streamlit_app.py)

KEYBOARD SHORTCUTS:

CLI app:
    - Type 1-13 to select menu options
    - Type 0 to exit
    
Streamlit web app:
    - Ctrl+C to stop server
    - F5 to refresh
    - Click any button to interact

COMMON DATE FORMATS:

    2024-01-15  (YYYY-MM-DD) ← Our default
    15-01-2024  (DD-MM-YYYY)
    01/15/2024  (MM/DD/YYYY)

═════════════════════════════════════════════════════════════════

REMEMBER: This is a learning project!
- Don't worry about perfect code
- Experiment and break things
- Fix errors to learn
- Modify and customize
- Build on this foundation

Happy tracking! 💰

═════════════════════════════════════════════════════════════════
""")


if __name__ == "__main__":
    print("\n" + "="*65)
    print("👋 Welcome to Personal Expense Tracker Quick Start Guide!")
    print("="*65 + "\n")
    
    print("This file contains everything you need to get started.\n")
    print("To see the full guide, check the output above!")
    print("\nNext step: Open terminal and run:")
    print("    pip install -r requirements.txt")
    print("\nThen choose:")
    print("    python app.py (for CLI)")
    print("    OR")
    print("    streamlit run streamlit_app.py (for web app)")
