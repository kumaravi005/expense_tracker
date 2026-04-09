# 💰 Personal Expense Tracker

A complete, beginner-friendly Python project that helps you track, analyze, and visualize your personal expenses. Built with clean code principles and designed for internship-level quality.
  
## 📋 Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [How to Use](#how-to-use)
- [Code Explanation](#code-explanation)
- [Learning Outcomes](#learning-outcomes)
- [Future Improvements](#future-improvements)

---

## ✨ Features

### Core Features
- ✅ **Add Expenses** - Record date, category, amount, and notes
- ✅ **CSV Storage** - Data persists in CSV format (easy to understand and share)
- ✅ **View Expenses** - Display all recorded expenses in table format
- ✅ **Edit Expenses** - Modify existing expense records
- ✅ **Delete Expenses** - Remove unwanted entries

### Data Analysis
- 📊 **Total Spending** - Calculate overall expenses
- 📊 **Category Analysis** - See which categories cost the most
- 📊 **Monthly Trends** - Track spending patterns month-by-month
- 📊 **Statistics** - Average, highest, lowest expenses

### Data Visualization
- 📈 **Bar Charts** - Category-wise spending comparison
- 🥧 **Pie Charts** - Expense distribution visualization
- 📉 **Line Charts** - Monthly spending trends
- 📊 **Dashboard** - Comprehensive overview of all metrics

### Advanced Features
- 🚨 **Budget Warnings** - Alert when spending exceeds budget limits
- 🔍 **Filtering** - Filter expenses by date, category, or month
- 📄 **Reports** - Generate comprehensive summary reports
- 💾 **Export** - Download data in CSV/JSON format

### Web Interface
- 🌐 **Streamlit Dashboard** - Interactive web application
- 📱 **Responsive Design** - Works on desktop and mobile
- 💡 **Intuitive UI** - Easy to navigate and use

---

## 📁 Project Structure

```
expense_tracker/
│
├── config.py                 # Configuration & constants
├── expense_manager.py        # Core CRUD operations
├── analysis.py               # Pandas analysis functions
├── visualization.py          # Matplotlib/Seaborn charts
├── app.py                    # CLI application
├── streamlit_app.py          # Web application
├── requirements.txt          # Dependencies
├── expenses.csv              # Data file (created automatically)
└── README.md                 # This file
```

### File Purposes

| File | Purpose | Key Functions |
|------|---------|---|
| `config.py` | Configuration variables | Categories, budget limits, file paths |
| `expense_manager.py` | Data management | add_expense(), edit_expense(), delete_expense() |
| `analysis.py` | Pandas analysis | category_wise_spending(), monthly_trends() |
| `visualization.py` | Charts & graphs | plot_bar_chart(), plot_pie_chart() |
| `app.py` | CLI menu | User interaction & navigation |
| `streamlit_app.py` | Web dashboard | Interactive web interface |

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone/Download Project
```bash
# Navigate to desired directory
cd "path/to/expense_tracker"
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

**Why virtual environment?**
- Keeps project dependencies isolated
- Prevents conflicts with other projects
- Easy to replicate setup on other machines

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**What gets installed?**
- `pandas` - Data manipulation and analysis
- `matplotlib` & `seaborn` - Data visualization
- `plotly` - Interactive charts
- `streamlit` - Web application framework

---

## 📖 How to Use

### Option 1: Command Line Interface (CLI)

**Run the CLI app:**
```bash
python app.py
```

**Features:**
- Interactive menu system
- Add, view, edit, delete expenses
- View analytics and charts
- Generate reports

**Example Walkthrough:**
```
1. Select "Add Expense"
2. Enter date: 2024-01-15
3. Enter category: Food
4. Enter amount: 45.50
5. Enter note: Lunch at restaurant
✓ Expense added successfully

6. Select "View Summary Report"
7. See all statistics and breakdowns
```

### Option 2: Streamlit Web App

**Run the web app:**
```bash
streamlit run streamlit_app.py
```

**Browser automatically opens at:** `http://localhost:8501`

**Features:**
- Beautiful dashboard with charts
- Add expenses through form
- View/manage all expenses
- Analyze data with multiple filters
- Download reports and data

**Tabs Available:**
1. **Dashboard** - Overview with key metrics
2. **Add Expense** - Form to add new expenses
3. **View Expenses** - Table of all expenses
4. **Analysis** - Advanced filtering and statistics
5. **Reports** - Export and download data

---

## 💡 Code Explanation

### Module 1: config.py
**Purpose:** Store all constant values in one place

```python
# Example: Constants used throughout app
CATEGORIES = ['Food', 'Transportation', 'Entertainment', ...]
MONTHLY_BUDGET_LIMIT = 5000
DATE_FORMAT = '%Y-%m-%d'
```

**Why?**
- Easy to modify settings without changing code
- Single source of truth for configuration
- Follows DRY (Don't Repeat Yourself) principle

---

### Module 2: expense_manager.py
**Purpose:** Handle file I/O and basic CRUD operations

**Key Functions:**

```python
def add_expense(date, category, amount, note):
    """ Add new expense to CSV """
    # Validates input
    # Writes to CSV file
    # Returns success status
```

**How CSV works:**
```
Date,Category,Amount,Note
2024-01-15,Food,45.50,Lunch
2024-01-16,Transport,20.00,Uber
```

**Why CSV?**
- Human-readable format
- Can open in Excel
- Easy to share and backup
- No database setup needed

**Error Handling:**
```python
# Validates date format
# Validates category exists
# Validates amount is positive
# Catches file I/O errors
```

---

### Module 3: analysis.py
**Purpose:** Analyze expense data using Pandas

**Key Concept: DataFrame**
```python
import pandas as pd
df = pd.read_csv('expenses.csv')
# df is like an Excel spreadsheet in Python
```

**Key Functions:**

```python
# Group expenses by category and sum
category_spending = df.groupby('Category')['Amount'].sum()

# Filter by date range
filtered = df[(df['Date'] >= start) & (df['Date'] <= end)]

# Calculate statistics
average = df['Amount'].mean()
total = df['Amount'].sum()
```

**Why Pandas?**
- Makes calculations easy (powerful groupby, filtering)
- Fast processing even with large datasets
- Integrates well with visualization libraries
- Industry standard for data analysis

---

### Module 4: visualization.py
**Purpose:** Create charts for visual analysis

**Library Comparison:**
- **Matplotlib** - Low-level control, more code
- **Seaborn** - High-level, better styling (built on Matplotlib)
- **Plotly** - Interactive charts (for Streamlit)

**Example: Bar Chart**
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data
ax.bar(categories, amounts, color='steelblue')

# Customize
ax.set_title('Spending by Category')
ax.set_xlabel('Category')
ax.set_ylabel('Amount ($)')

plt.show()
```

**Chart Types & When to Use:**
| Chart | Use Case |
|-------|----------|
| Bar Chart | Compare values across categories |
| Pie Chart | Show proportion of total |
| Line Chart | Show trends over time |
| Gauge/Progress | Show progress towards limit |

---

### Module 5: app.py
**Purpose:** CLI interface bringing all modules together

**Design Pattern: Class-Based**
```python
class ExpenseTrackerApp:
    def __init__(self):
        self.running = True
    
    def menu_add_expense(self):
        # Get user input
        # Call add_expense() from expense_manager
        # Display result
    
    def run(self):
        # Main loop
        while self.running:
            # Show menu
            # Get user choice
            # Call appropriate function
```

**Why class-based?**
- Organizes related methods together
- Maintains state (like self.running)
- Easy to extend with new features
- Professional coding practice

---

### Module 6: streamlit_app.py
**Purpose:** Web interface for the application

**Key Streamlit Concepts:**

```python
# Display text
st.title("My Title")
st.write("Regular text")

# Input forms
name = st.text_input("Enter name")
amount = st.number_input("Enter amount", min_value=0)
category = st.selectbox("Choose category", categories)

# Display data
st.dataframe(df)  # Table

# Charts
st.plotly_chart(fig)

# Buttons & Downloads
if st.button("Click me"):
    # Code to run on click
    pass

st.download_button("Download", data=csv_data, file_name="data.csv")
```

**Why Streamlit?**
- Minimal code for web apps
- No HTML/CSS/JavaScript needed
- Auto-reloads on changes
- Great for data dashboards
- Looks professional without effort

---

## 📚 Learning Outcomes

By completing this project, you learn:

### Python Concepts
- ✅ Functions and modular programming
- ✅ Classes and object-oriented design
- ✅ File I/O operations (reading/writing CSV)
- ✅ Error handling (try/except)
- ✅ Data structures (lists, dictionaries)

### Data Science Libraries
- ✅ **Pandas** - Data manipulation and groupby operations
- ✅ **Matplotlib/Seaborn** - Data visualization
- ✅ **Plotly** - Interactive charts

### Web Development
- ✅ **Streamlit** - Building web applications quickly
- ✅ UI/UX basics - Creating user-friendly interfaces

### Best Practices
- ✅ Clean code principles (modularity, documentation)
- ✅ Error handling and validation
- ✅ Configuration management
- ✅ Code comments and docstrings

---

## 🔧 Customization & Modifications

### Change Budget Limit
```python
# In config.py
MONTHLY_BUDGET_LIMIT = 3000  # Change from 5000 to 3000
```

### Add New Expense Category
```python
# In config.py
CATEGORIES = [
    'Food',
    'Transportation',
    'Entertainment',
    'Gaming',  # New category
    'Other'
]
```

### Change Currency
```python
# In config.py
CURRENCY_SYMBOL = '₹'  # Indian Rupee instead of $
```

### Modify Date Format
```python
# In config.py
DATE_FORMAT = '%d-%m-%Y'  # DD-MM-YYYY instead of YYYY-MM-DD
```

---

## 🚀 Future Enhancements

### Level 1: Basic Improvements
1. **Database** - Replace CSV with SQLite for better performance
2. **Password Protection** - Encrypt sensitive data
3. **Recurring Expenses** - Add automatic monthly expenses
4. **Email Reminders** - Notify when budget limit approaching

### Level 2: Advanced Features
1. **AI Predictions** - Use ML to predict future spending
2. **Budget Optimization** - Suggest where to cut spending
3. **Receipt OCR** - Extract amount/category from receipt photos
4. **Multi-User Support** - Share expenses with family

### Level 3: Professional Features
1. **Mobile App** - Flutter/React Native version
2. **Cloud Sync** - Sync across devices (Google Drive/AWS)
3. **Investment Tracking** - Track savings and investments
4. **Tax Reports** - Generate tax deduction reports

---

## 📝 Sample Workflow

### Example 1: Adding Expenses
```bash
$ python app.py

# Select Option: 1 (Add Expense)
# Date: 2024-01-15
# Category: Food
# Amount: 45.50
# Note: Dinner at restaurant

✓ Expense added: Food - 45.50 on 2024-01-15
```

### Example 2: View Summary
```bash
# Select Option: 5 (View Summary Report)

EXPENSE SUMMARY REPORT
============================================================
📊 OVERALL STATISTICS
- Total Expenses: 12
- Total Amount Spent: $523.45
- Average per Expense: $43.62
- Highest Expense: $125.00 (Entertainment)
- Lowest Expense: $5.50 (Transportation)

💰 CATEGORY BREAKDOWN
- Food: $245.30 (46.9%)
- Transportation: $89.50 (17.1%)
- Entertainment: $125.00 (23.9%)
- Other: $63.65 (12.2%)
```

---

## 🐛 Troubleshooting

### Issue: Module not found error
```
ModuleNotFoundError: No module named 'pandas'
```
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: CSV file not found
```
FileNotFoundError: expenses.csv not found
```
**Solution:** Run the CLI app first - it creates the file automatically

### Issue: Chart not displaying
```
# Matplotlib issues on some systems
```
**Solution:** Use Streamlit instead (displays interactive charts)

### Issue: Streamlit can't find modules
```bash
# Make sure virtual environment is activated
# Then run streamlit
streamlit run streamlit_app.py
```

---

## 📚 Resources & Learning

### Online Documentation
- [Pandas Tutorial](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)

### Books
- "Python for Data Analysis" by Wes McKinney
- "Automate the Boring Stuff with Python" by Al Sweigart

### YouTube Channels
- Corey Schafer (Data Science Python)
- freeCodeCamp (Full Python Courses)
- Real Python (In-depth tutorials)

---

## 📞 Support & Contribution

### Getting Help
1. Check the "Troubleshooting" section above
2. Read code comments and docstrings
3. Review official library documentation
4. Search Stack Overflow for similar issues

### Contributing Improvements
Feel free to:
- Fix bugs
- Add new features
- Improve documentation
- Suggest better code practices
- Share your enhancements

---

## 📄 License

This project is open source and available for educational purposes.

---

## 🎯 Next Steps

1. **Setup the project** - Follow installation steps
2. **Run CLI app** - Add some sample expenses
3. **Explore code** - Read through each module
4. **Try Streamlit** - Run the web app
5. **Modify it** - Customize for your needs
6. **Enhance it** - Add features from "Future Enhancements"

---

## ✅ Checklist for Beginner

- [ ] Install Python 3.8+
- [ ] Clone/download the project
- [ ] Create virtual environment
- [ ] Install dependencies (pip install -r requirements.txt)
- [ ] Run CLI app (python app.py)
- [ ] Add a few sample expenses
- [ ] Generate a summary report
- [ ] View some charts
- [ ] Run Streamlit app (streamlit run streamlit_app.py)
- [ ] Explore the web dashboard
- [ ] Read through the code files
- [ ] Customize configuration (budget, categories)
- [ ] Add your own features

---

## 🎓 Learning Tips

1. **Don't just read code - run it**
   - Execute each function
   - Try different inputs
   - See error messages

2. **Understand the flow**
   - Trace how data moves between modules
   - Understand when each function is called
   - Check what data is returned

3. **Experiment**
   - Modify code and see what breaks
   - Add print statements for debugging
   - Create sample data and analyze it

4. **Document your learning**
   - Write comments explaining code
   - Create your own examples
   - Build on this foundation

---

**Happy Tracking! 💰**

*Built with ❤️ for beginners ready to learn internship-level Python*
#   e x p e n s e _ t r a c k e r 
 
 
