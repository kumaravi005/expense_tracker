"""
Data Visualization module using Matplotlib and Seaborn.

Why these libraries?
- Matplotlib: Low-level plotting library, full control over plots
- Seaborn: Built on Matplotlib, provides higher-level interface, better styling
- Both integrate well with Pandas DataFrames

This module creates charts for visual analysis of expense data.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from analysis import (
    load_data, category_wise_spending, monthly_spending,
    total_spending, filter_by_category, monthly_budget_status
)
from config import CURRENCY_SYMBOL, MONTHLY_BUDGET_LIMIT
from datetime import datetime


# Set default style for all plots
sns.set_style("whitegrid")  # Add grid background
plt.rcParams['figure.figsize'] = (12, 6)  # Default figure size


def plot_category_bar_chart(save_path=None):
    """
    Create a bar chart showing spending by category.
    
    Why bar chart?
    - Easy to compare values across categories
    - Visual representation of which categories cost the most
    
    Args:
        save_path (str): Optional path to save the plot
    """
    cat_spending = category_wise_spending()
    
    if cat_spending.empty:
        print("No data to plot")
        return
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create bar chart
    # color='steelblue': Nice blue color for bars
    bars = ax.bar(cat_spending.index, cat_spending.values, color='steelblue', edgecolor='navy', alpha=0.7)
    
    # Customize plot
    ax.set_title('Spending by Category', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Category', fontsize=12, fontweight='bold')
    ax.set_ylabel(f'Amount ({CURRENCY_SYMBOL})', fontsize=12, fontweight='bold')
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{CURRENCY_SYMBOL}{height:.2f}',
                ha='center', va='bottom', fontsize=10)
    
    # Rotate x-axis labels for readability
    plt.xticks(rotation=45, ha='right')
    
    # Add gridlines
    ax.grid(axis='y', alpha=0.3)
    
    # Tight layout to prevent label cutoff
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Chart saved to {save_path}")
    
    plt.show()


def plot_category_pie_chart(save_path=None):
    """
    Create a pie chart showing distribution of expenses by category.
    
    Why pie chart?
    - Shows proportion/percentage of total
    - Easy to see which category takes up the largest share
    
    Args:
        save_path (str): Optional path to save the plot
    """
    cat_spending = category_wise_spending()
    
    if cat_spending.empty:
        print("No data to plot")
        return
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create pie chart
    # autopct='%1.1f%%': Show percentage labels with 1 decimal place
    # startangle=90: Start pie chart from top
    wedges, texts, autotexts = ax.pie(
        cat_spending.values,
        labels=cat_spending.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=sns.color_palette('Set2', len(cat_spending))
    )
    
    # Customize text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)
    
    for text in texts:
        text.set_fontsize(11)
        text.set_fontweight('bold')
    
    ax.set_title('Expense Distribution by Category', fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Chart saved to {save_path}")
    
    plt.show()


def plot_monthly_trend(save_path=None):
    """
    Create a line chart showing spending trends over months.
    
    Why line chart?
    - Shows trends over time
    - Easy to identify seasonal patterns
    - See if spending is increasing or decreasing
    
    Args:
        save_path (str): Optional path to save the plot
    """
    monthly_data = monthly_spending()
    
    if monthly_data.empty:
        print("No data to plot")
        return
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Convert period index to strings for plotting
    months = [str(m) for m in monthly_data.index]
    
    # Create line plot
    # marker='o': Add circle markers at data points
    # linewidth=2: Make line thicker
    ax.plot(months, monthly_data.values, marker='o', linewidth=2.5, 
            markersize=8, color='darkgreen', markerfacecolor='lightblue')
    
    # Add budget limit line for reference
    ax.axhline(y=MONTHLY_BUDGET_LIMIT, color='red', linestyle='--', 
               linewidth=2, label=f'Budget Limit ({CURRENCY_SYMBOL}{MONTHLY_BUDGET_LIMIT})', alpha=0.7)
    
    # Customize plot
    ax.set_title('Monthly Spending Trend', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Month', fontsize=12, fontweight='bold')
    ax.set_ylabel(f'Amount ({CURRENCY_SYMBOL})', fontsize=12, fontweight='bold')
    
    # Add value labels on points
    for i, value in enumerate(monthly_data.values):
        ax.text(i, value, f'{CURRENCY_SYMBOL}{value:.2f}', 
                ha='center', va='bottom', fontsize=10)
    
    # Add legend
    ax.legend(fontsize=10, loc='best')
    
    # Add gridlines
    ax.grid(True, alpha=0.3)
    
    # Rotate x-axis labels
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Chart saved to {save_path}")
    
    plt.show()


def plot_budget_gauge(year, month, save_path=None):
    """
    Create a gauge chart showing budget status.
    Alternative to pie: shows current spending against limit.
    
    Args:
        year (int): Year
        month (int): Month (1-12)
        save_path (str): Optional path to save the plot
    """
    status = monthly_budget_status(year, month)
    spent = status['spent']
    budget = status['budget']
    percentage = status['percentage']
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Create horizontal bar showing spent vs remaining
    remaining = max(0, budget - spent)
    
    ax.barh([0], [spent], color='#ff6b6b', label=f'Spent: {CURRENCY_SYMBOL}{spent:.2f}')
    ax.barh([0], [remaining], left=[spent], color='#51cf66', label=f'Remaining: {CURRENCY_SYMBOL}{remaining:.2f}')
    
    # Customize
    ax.set_xlim(0, budget * 1.1)
    ax.set_ylim(-0.5, 0.5)
    ax.set_yticks([])
    ax.set_xlabel(f'Amount ({CURRENCY_SYMBOL})', fontsize=12, fontweight='bold')
    ax.set_title(f'Budget Status - {month}/{year} ({percentage:.1f}% used)', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Add percentage text
    ax.text(budget/2, 0, f'{percentage:.1f}%', ha='center', va='center', 
            fontsize=20, fontweight='bold', color='white')
    
    # Add legend
    ax.legend(loc='upper right', fontsize=10)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Chart saved to {save_path}")
    
    plt.show()


def plot_category_over_time(category, save_path=None):
    """
    Create a line chart for spending trend of a specific category.
    
    Args:
        category (str): Category name
        save_path (str): Optional path to save the plot
    """
    df = load_data()
    
    if df.empty:
        print("No data to plot")
        return
    
    # Filter data for the category
    cat_data = df[df['Category'] == category].copy()
    
    if cat_data.empty:
        print(f"No data found for category: {category}")
        return
    
    # Sort by date
    cat_data = cat_data.sort_values('Date')
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot
    ax.scatter(cat_data['Date'], cat_data['Amount'], s=100, alpha=0.6, color='purple')
    ax.plot(cat_data['Date'], cat_data['Amount'], alpha=0.3, color='purple')
    
    # Customize
    ax.set_title(f'{category} Spending Over Time', fontsize=14, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax.set_ylabel(f'Amount ({CURRENCY_SYMBOL})', fontsize=12, fontweight='bold')
    
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Chart saved to {save_path}")
    
    plt.show()


def create_dashboard_image(save_path='expense_dashboard.png'):
    """
    Create a comprehensive dashboard with multiple charts.
    
    Args:
        save_path (str): Path to save the dashboard image
    """
    df = load_data()
    
    if df.empty:
        print("No data to create dashboard")
        return
    
    # Create a 2x2 grid of subplots
    fig = plt.figure(figsize=(16, 12))
    
    # 1. Category Bar Chart
    ax1 = plt.subplot(2, 2, 1)
    cat_spending = category_wise_spending()
    ax1.bar(cat_spending.index, cat_spending.values, color='steelblue', edgecolor='navy', alpha=0.7)
    ax1.set_title('Spending by Category', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Category')
    ax1.set_ylabel(f'Amount ({CURRENCY_SYMBOL})')
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
    ax1.grid(axis='y', alpha=0.3)
    
    # 2. Category Pie Chart
    ax2 = plt.subplot(2, 2, 2)
    ax2.pie(cat_spending.values, labels=cat_spending.index, autopct='%1.1f%%',
            colors=sns.color_palette('Set2', len(cat_spending)))
    ax2.set_title('Expense Distribution', fontsize=12, fontweight='bold')
    
    # 3. Monthly Trend
    ax3 = plt.subplot(2, 2, 3)
    monthly = monthly_spending()
    months = [str(m) for m in monthly.index]
    ax3.plot(months, monthly.values, marker='o', linewidth=2, markersize=6, color='darkgreen')
    ax3.axhline(y=MONTHLY_BUDGET_LIMIT, color='red', linestyle='--', linewidth=1.5, alpha=0.7)
    ax3.set_title('Monthly Spending Trend', fontsize=12, fontweight='bold')
    ax3.set_xlabel('Month')
    ax3.set_ylabel(f'Amount ({CURRENCY_SYMBOL})')
    plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45, ha='right')
    ax3.grid(True, alpha=0.3)
    
    # 4. Statistics Box
    ax4 = plt.subplot(2, 2, 4)
    ax4.axis('off')
    
    stats_text = f"""
    EXPENSE STATISTICS
    {'─' * 35}
    
    Total Expenses:     {len(df)}
    Total Spending:     {CURRENCY_SYMBOL}{total_spending():,.2f}
    Average Expense:    {CURRENCY_SYMBOL}{df['Amount'].mean():,.2f}
    Highest Expense:    {CURRENCY_SYMBOL}{df['Amount'].max():,.2f}
    Lowest Expense:     {CURRENCY_SYMBOL}{df['Amount'].min():,.2f}
    """
    
    ax4.text(0.1, 0.5, stats_text, fontsize=11, family='monospace',
            verticalalignment='center', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.suptitle('EXPENSE TRACKER DASHBOARD', fontsize=18, fontweight='bold', y=0.995)
    plt.tight_layout()
    
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Dashboard saved to {save_path}")
    
    plt.show()


def show_all_charts_interactive():
    """
    Display all charts one by one in interactive mode.
    User can navigate through charts.
    """
    print("\n" + "="*60)
    print("INTERACTIVE CHART VIEWER")
    print("="*60)
    
    charts = [
        ("1. Category Bar Chart", plot_category_bar_chart),
        ("2. Expense Distribution Pie Chart", plot_category_pie_chart),
        ("3. Monthly Spending Trend", plot_monthly_trend),
        ("4. Full Dashboard", create_dashboard_image)
    ]
    
    for name, func in charts:
        print(f"\nDisplaying: {name}")
        try:
            if name == "4. Full Dashboard":
                func()
            else:
                func()
            input("Press Enter to continue to next chart...")
        except Exception as e:
            print(f"Error displaying chart: {e}")
    
    print("\nChart viewer complete!")
