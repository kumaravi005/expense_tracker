"""
╔═════════════════════════════════════════════════════════════════════════╗
║                                                                         ║
║          💰 PERSONAL EXPENSE TRACKER - START HERE 🎯                   ║
║                                                                         ║
║              A Complete Internship-Level Python Project                ║
║                                                                         ║
╚═════════════════════════════════════════════════════════════════════════╝

Welcome! This document guides you through all project files and how to use them.

═════════════════════════════════════════════════════════════════════════════
📁 PROJECT STRUCTURE - WHAT EACH FILE DOES
═════════════════════════════════════════════════════════════════════════════

APPLICATION FILES (Running the app)
──────────────────────────────────────────────────────────────────────────

1. app.py                          🖥️ CLI (Command Line Interface)
   └─ Command: python app.py
   └─ Interface: Menu-driven terminal app
   └─ When: Quick testing, learning basics
   └─ Features: Add, view, edit, delete, analyze
   
   EXAMPLE SESSION:
   $ python app.py
   ==========================================
   PERSONAL EXPENSE TRACKER
   ==========================================
   1. Add Expense
   2. View All Expenses
   ... (More options)
   
   Select option: 1
   Enter date (2024-01-15): 2024-01-15
   Enter category: Food
   Enter amount: 45.50
   Enter note: Lunch
   ✓ Expense added

2. streamlit_app.py                🌐 Web App (Beautiful Dashboard)
   └─ Command: streamlit run streamlit_app.py
   └─ Interface: Web browser (http://localhost:8501)
   └─ When: Visualizations, sharing, professional use
   └─ Features: Dashboard, charts, interactive forms
   
   Browser displays:
   - Dashboard with key metrics
   - Add expense form
   - Data table
   - Analysis tabs
   - Reports & exports

3. generate_sample_data.py         🎲 Test Data Generator
   └─ Command: python generate_sample_data.py
   └─ Purpose: Create sample data for testing
   └─ When: First time setup, demonstrations
   └─ Result: 3 months of realistic expenses


DATA MANAGEMENT FILES
──────────────────────────────────────────────────────────────────────────

4. config.py                        ⚙️ Configuration Hub
   └─ Purpose: All settings in one place
   └─ Contains: Categories, budget, date format
   └─ Modify to: Customize app behavior
   
   Example settings:
   - CATEGORIES = ['Food', 'Transport', ...]
   - MONTHLY_BUDGET_LIMIT = 5000
   - CURRENCY_SYMBOL = '$'

5. expense_manager.py              💾 Data Core (CRUD Operations)
   └─ Purpose: Handle file operations
   └─ Functions:
     • init_csv() - Create/initialize CSV
     • add_expense() - Add new expense
     • edit_expense() - Modify existing
     • delete_expense() - Remove expense
     • get_all_expenses() - Retrieve all
   └─ Data Format: CSV (easy to open in Excel)

6. analysis.py                     📊 Data Analysis (Pandas)
   └─ Purpose: Calculate statistics and trends
   └─ Functions:
     • total_spending() - Overall total
     • category_wise_spending() - By category
     • monthly_spending() - By month
     • filter_by_category() - Specific category
     • monthly_budget_status() - Budget check
   └─ Library: Pandas (powerful data tool)

7. visualization.py                📈 Charts & Graphs
   └─ Purpose: Create visual representations
   └─ Functions:
     • plot_category_bar_chart() - Bar chart
     • plot_category_pie_chart() - Pie chart
     • plot_monthly_trend() - Line chart
     • create_dashboard_image() - Combined view
   └─ Libraries: Matplotlib, Seaborn, Plotly


DOCUMENTATION FILES
──────────────────────────────────────────────────────────────────────────

8. README.md                        📚 Main Documentation
   └─ Sections: 40+
   └─ Contains:
     • Feature list
     • Installation guide
     • Detailed code explanation
     • Usage examples
     • Troubleshooting
   └─ Read: After installing

9. QUICK_START.py                  🚀 5-Minute Setup
   └─ Purpose: Get started quickly
   └─ Contains: Step-by-step setup
   └─ Read: Before running app
   └─ Command: python QUICK_START.py

10. TESTING_GUIDE.py               ✅ Complete Testing
    └─ Purpose: Test all features
    └─ Contains: Unit, integration, system tests
    └─ Read: After setup

11. PROJECT_OVERVIEW.md             📋 Project Summary
    └─ Purpose: High-level overview
    └─ Contains: Features, learning outcomes
    └─ Read: To understand what you have

12. expenses.csv                    💾 Data File
    └─ Auto-created: Yes (when app first runs)
    └─ Format: Comma-separated values
    └─ Editable: Open in Excel if needed
    └─ Structure: Date, Category, Amount, Note

═════════════════════════════════════════════════════════════════════════════
🚀 QUICK START - 3 SIMPLE STEPS
═════════════════════════════════════════════════════════════════════════════

STEP 1️⃣: Install Dependencies
────────────────────────────────────────────────────────────────────────
Run this command once:
    pip install -r requirements.txt

Installs: pandas, matplotlib, seaborn, plotly, streamlit

STEP 2️⃣: Choose Your Interface

Option A - CLI (Simple):
    python app.py

Option B - Web App (Beautiful):
    streamlit run streamlit_app.py

STEP 3️⃣: Start Using!
    - Add expenses
    - View reports
    - Create charts
    - Analyze spending

═════════════════════════════════════════════════════════════════════════════
📖 READING ORDER - HOW TO LEARN THE PROJECT
═════════════════════════════════════════════════════════════════════════════

For Beginners (New to Python):
────────────────────────────────────────────────────────────────────────
1. Read: QUICK_START.py
2. Read: README.md (Sections 1-3)
3. Run: generate_sample_data.py
4. Run: streamlit run streamlit_app.py
5. Explore web dashboard
6. Read: README.md (Code Explanation section)
7. Read: config.py (with comments)
8. Try: python app.py

For Intermediate (Know Python):
────────────────────────────────────────────────────────────────────────
1. Read: PROJECT_OVERVIEW.md
2. Skim: README.md (Sections 4-6)
3. Read & understand: expense_manager.py
4. Read & understand: analysis.py
5. Read & understand: app.py
6. Read & understand: streamlit_app.py
7. Try: TESTING_GUIDE.py
8. Modify: config.py, add features

For Advanced (Want to Extend):
────────────────────────────────────────────────────────────────────────
1. Read: PROJECT_OVERVIEW.md (Customization section)
2. Review: All Python files
3. Run: TESTING_GUIDE.py
4. Plan: What features to add
5. Code: New features
6. Test: Your additions
7. Deploy: To cloud (optional)

═════════════════════════════════════════════════════════════════════════════
🎯 COMMON TASKS - QUICK REFERENCE
═════════════════════════════════════════════════════════════════════════════

"I want to run the app"
    → Run: python app.py (CLI)
    → Or: streamlit run streamlit_app.py (Web)

"I want to add test data"
    → Run: python generate_sample_data.py

"I want to understand the code"
    → Read: README.md (Code Explanation section)
    → Then read: Individual .py files

"I want to change settings"
    → Edit: config.py
    → Modify: CATEGORIES, MONTHLY_BUDGET_LIMIT, CURRENCY_SYMBOL

"I want to add a new feature"
    → Edit: expense_manager.py (for data)
    → Or: analysis.py (for calculations)
    → Or: visualization.py (for charts)

"The app isn't working"
    → Check: TESTING_GUIDE.py
    → Or: README.md (Troubleshooting section)

═════════════════════════════════════════════════════════════════════════════
📊 FEATURE GUIDE - WHAT CAN YOU DO?
═════════════════════════════════════════════════════════════════════════════

Basic Operations
  ✅ Add expense (date, category, amount, note)
  ✅ View all expenses
  ✅ Edit existing expense
  ✅ Delete expense

Analysis Features
  ✅ View total spending
  ✅ See spending by category
  ✅ View monthly trends
  ✅ Calculate average expense
  ✅ Find highest/lowest expense

Filtering
  ✅ Filter by category
  ✅ Filter by date range
  ✅ Filter by month

Visualization
  ✅ Bar chart (categories)
  ✅ Pie chart (distribution)
  ✅ Line chart (trends)
  ✅ Budget gauge
  ✅ Dashboard (all combined)

Advanced
  ✅ Budget status check
  ✅ Budget warnings
  ✅ Generate reports
  ✅ Export data (CSV, JSON)

═════════════════════════════════════════════════════════════════════════════
💾 DATA FLOW - HOW DATA MOVES THROUGH THE APP
═════════════════════════════════════════════════════════════════════════════

You Add Expense (app.py)
        ↓
Validated Against Rules (config.py)
        ↓
Stored in CSV (expense_manager.py)
        ↓
Read When Needed (expense_manager.py → analysis.py)
        ↓
Analyzed with Pandas (analysis.py)
        ↓
Visualized as Charts (visualization.py)
        ↓
Displayed to You (app.py or streamlit_app.py)

═════════════════════════════════════════════════════════════════════════════
🔧 CUSTOMIZATION GUIDE - EASY CHANGES
═════════════════════════════════════════════════════════════════════════════

All customizations are in config.py

Change Budget Limit:
    MONTHLY_BUDGET_LIMIT = 3000  (was 5000)

Add New Category:
    'Gaming' in CATEGORIES list

Change Currency:
    CURRENCY_SYMBOL = '₹'  (instead of '$')

Change Date Format:
    DATE_FORMAT = '%d-%m-%Y'  (was '%Y-%m-%d')

═════════════════════════════════════════════════════════════════════════════
🚨 TROUBLESHOOTING - COMMON ISSUES
═════════════════════════════════════════════════════════════════════════════

"ImportError: No module named 'pandas'"
    → Solution: Run: pip install -r requirements.txt

"FileNotFoundError: expenses.csv not found"
    → Solution: Normal! CSV created on first run. Try again.

"Port 8501 already in use" (Streamlit)
    → Solution: streamlit run streamlit_app.py --server.port 8502

"Charts not showing"
    → Solution: Use Streamlit instead: streamlit run streamlit_app.py

More help → See README.md (Troubleshooting section)

═════════════════════════════════════════════════════════════════════════════
📚 LEARNING RESOURCES
═════════════════════════════════════════════════════════════════════════════

Python Docs: https://docs.python.org/3/
Real Python: https://realpython.com/
Pandas Docs: https://pandas.pydata.org/docs/
Matplotlib: https://matplotlib.org/
Streamlit: https://docs.streamlit.io/
Stack Overflow: https://stackoverflow.com/

═════════════════════════════════════════════════════════════════════════════
✅ YOUR NEXT STEPS
═════════════════════════════════════════════════════════════════════════════

TODAY:
  1. Install: pip install -r requirements.txt
  2. Run: python app.py (or streamlit run streamlit_app.py)
  3. Add 5 expenses
  4. View reports

THIS WEEK:
  1. Read: README.md thoroughly
  2. Generate sample data
  3. Explore all features
  4. Understand code structure

THIS MONTH:
  1. Study each Python file
  2. Modify configuration
  3. Add custom features
  4. Build similar projects

═════════════════════════════════════════════════════════════════════════════
🎉 YOU'RE ALL SET!
═════════════════════════════════════════════════════════════════════════════

Your Personal Expense Tracker is ready to use!

✅ Has 6 Python modules (modular design)
✅ Supports 2 interfaces (CLI + Web)
✅ Includes data analysis (Pandas)
✅ Creates visualizations (Matplotlib/Seaborn/Plotly)
✅ Well documented (40+ sections)
✅ Production ready (error handling)
✅ Beginner friendly (detailed comments)
✅ Internship quality (professional standards)

READY TO GET STARTED?

Quick start:
    pip install -r requirements.txt
    python app.py

Web version:
    streamlit run streamlit_app.py

Sample data:
    python generate_sample_data.py

═════════════════════════════════════════════════════════════════════════════

Happy tracking! 💰

Questions? Check README.md or TESTING_GUIDE.py

═════════════════════════════════════════════════════════════════════════════
"""

def main():
    """Print the welcome guide."""
    print(__doc__)

if __name__ == "__main__":
    main()
