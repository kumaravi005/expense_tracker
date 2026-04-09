# 💰 Personal Expense Tracker

A complete, beginner-friendly Python project that helps you track, analyze, and visualize your personal expenses.
## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [How to Use](#how-to-use)
- [Code Explanation](#code-explanation)
- [Learning Outcomes](#learning-outcomes)

---

## ✨ Features

### Core Features
- ✅ Add expenses (date, category, amount, note)
- ✅ Store data in CSV file
- ✅ View all expenses
- ✅ Edit and delete expenses

### Data Analysis
- 📊 Calculate total spending
- 📊 Category-wise spending breakdown
- 📊 Monthly spending trends
- 📊 Statistics (average, min, max)

### Data Visualization
- 📈 Bar chart for category-wise expenses
- 🥧 Pie chart for distribution
- 📉 Line chart for monthly trends
- 📊 Interactive dashboard

### Advanced Features
- 🚨 Budget limit warning system
- 🔍 Filter by date/month/category
- 📄 Summary report generation
- 💾 Export data (CSV, JSON)

### Web App
- 🌐 Interactive Streamlit dashboard
- 📱 Responsive design
- 💡 User-friendly interface

---

## 📁 Project Structure

```
expense_tracker/
├── config.py              # Configuration & constants
├── expense_manager.py     # Data management (CRUD)
├── analysis.py            # Pandas analysis
├── visualization.py       # Charts & visualization
├── app.py                 # CLI application
├── streamlit_app.py       # Web application
├── requirements.txt       # Dependencies
└── expenses.csv           # Data file (auto-created)
```

### File Purposes

| File | Purpose |
|------|---------|
| `config.py` | Budget limits, categories, date format |
| `expense_manager.py` | Add, edit, delete expenses |
| `analysis.py` | Pandas calculations & filtering |
| `visualization.py` | Matplotlib/Seaborn charts |
| `app.py` | CLI menu interface |
| `streamlit_app.py` | Web dashboard |

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `pandas` - Data manipulation
- `matplotlib` - Charting
- `seaborn` - Statistical visualization
- `plotly` - Interactive charts
- `streamlit` - Web app framework

### Step 2: Create Virtual Environment (Optional)

```bash
# Create
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

---

## 📖 How to Use

### Option A: Command Line Interface

```bash
python app.py
```

Features:
- Interactive menu
- Add expenses easily
- View all expenses
- Generate reports
- View charts

### Option B: Web Application

```bash
streamlit run streamlit_app.py
```

Opens in browser with:
- Dashboard (overview)
- Add expense form
- View expenses table
- Analysis & filtering
- Reports & exports

### Option C: Generate Sample Data

```bash
python generate_sample_data.py
```

Creates 3 months of test data to explore features.

---

## 💡 Code Explanation

### Module: config.py

Stores all settings in one place:

```python
CATEGORIES = ['Food', 'Transportation', 'Entertainment', ...]
MONTHLY_BUDGET_LIMIT = 5000
DATE_FORMAT = '%Y-%m-%d'
CURRENCY_SYMBOL = '$'
```

**Why?** Easy to customize without changing code.

---

### Module: expense_manager.py

Handles data storage using CSV:

```python
def add_expense(date, category, amount, note)
def get_all_expenses()
def edit_expense(row_number, ...)
def delete_expense(row_number)
```

**Why CSV?**
- Human readable
- Works in Excel
- No database needed
- Easy to backup

---

### Module: analysis.py

Uses Pandas for data analysis:

```python
def total_spending()           # Calculate total
def category_wise_spending()   # Group by category
def monthly_spending()         # Monthly totals
def filter_by_category()       # Filter data
```

**Key Pandas concepts:**
- DataFrames (like Excel in Python)
- groupby() - group data
- Filtering - select data
- Sum/Mean - calculations

---

### Module: visualization.py

Creates charts with Matplotlib/Seaborn:

```python
def plot_category_bar_chart()     # Bar chart
def plot_category_pie_chart()     # Pie chart
def plot_monthly_trend()          # Line chart
def create_dashboard_image()      # Combined dashboard
```

**Chart types:**
- Bar: Compare categories
- Pie: Show percentages
- Line: Show trends
- Dashboard: All combined

---

### Module: app.py

CLI (Command Line) interface:

```python
class ExpenseTrackerApp:
    def menu_add_expense()
    def menu_view_all()
    def menu_summary_report()
    def run()  # Main loop
```

**Design pattern:** Class organizes related functions.

---

### Module: streamlit_app.py

Web interface using Streamlit:

```python
def dashboard_page()      # Overview
def add_expense_page()    # Add form
def view_expenses_page()  # View data
def analysis_page()       # Analyze
def reports_page()        # Export
```

**Streamlit features:**
- Simple web apps
- Interactive widgets
- Auto-reloads
- No HTML/CSS needed

---

## 🎓 Learning Outcomes

### Python Skills
- ✅ Functions & modularity
- ✅ Classes & OOP
- ✅ File I/O (CSV files)
- ✅ Error handling
- ✅ Data structures

### Libraries
- ✅ Pandas - Data analysis
- ✅ Matplotlib - Charts
- ✅ Seaborn - Statistical plots
- ✅ Streamlit - Web apps

### Best Practices
- ✅ Modular design
- ✅ Configuration management
- ✅ Input validation
- ✅ Code documentation
- ✅ Error handling

---

## 🔧 Customization

Easy changes in `config.py`:

```python
# Change budget
MONTHLY_BUDGET_LIMIT = 3000

# Add categories
CATEGORIES = ['Food', 'Gaming', ...]

# Change currency
CURRENCY_SYMBOL = '₹'

# Change date format
DATE_FORMAT = '%d-%m-%Y'
```

---

## 🚀 Next Steps

### Day 1
1. Install dependencies
2. Run CLI app
3. Add 5 expenses
4. View reports

### Week 1
1. Read all documentation
2. Understand code structure
3. Generate sample data
4. Explore all features

### Week 2
1. Study each Python module
2. Modify settings
3. Add custom features
4. Build similar project

---

## 📚 Resources

### Documentation
- README.md - This guide
- QUICK_START.py - Quick setup
- PROJECT_OVERVIEW.md - Overview

### Learning
- [Python Docs](https://docs.python.org/3/)
- [Pandas Guide](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorial](https://matplotlib.org/)
- [Streamlit Docs](https://docs.streamlit.io/)

---

## ✅ Troubleshooting

**"ModuleNotFoundError: No module named 'pandas'"**
```bash
pip install -r requirements.txt
```

**"CSV file not found"**
- Normal! Created on first run. Just run again.

**"Port 8501 already in use"**
```bash
streamlit run streamlit_app.py --server.port 8502
```

---

## 📄 License

Open source for educational purposes.

---

**Happy Tracking! 💰**

Built with ❤️ for beginners and learners
