"""
Streamlit Web Application for Expense Tracker.

Why Streamlit?
- Easy to build web apps with minimal code
- No need to write HTML/CSS/JavaScript
- Auto-reloads on script changes
- Great for data visualization dashboards

How to run:
    streamlit run streamlit_app.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from expense_manager import (
    init_csv, add_expense, get_all_expenses,
    edit_expense, delete_expense, display_expenses
)
from analysis import (
    load_data, total_spending, category_wise_spending,
    monthly_spending, average_expense, highest_expense,
    lowest_expense, filter_by_category, filter_by_month,
    monthly_budget_status
)
from config import CATEGORIES, DATE_FORMAT, CURRENCY_SYMBOL, MONTHLY_BUDGET_LIMIT


# Configure Streamlit page
st.set_page_config(
    page_title="💰 Expense Tracker",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main {
        padding: 0px;
    }
    .metric-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0px;
    }
    </style>
    """, unsafe_allow_html=True)


def init_app():
    """Initialize the application."""
    init_csv()


def main():
    """Main Streamlit application."""
    
    # Initialize
    init_app()
    
    # Sidebar for navigation
    with st.sidebar:
        st.title("📊 Expense Tracker")
        page = st.radio(
            "Navigation",
            ["Dashboard", "Add Expense", "View Expenses", "Analysis", "Reports"]
        )
    
    # Load data
    df = load_data()
    
    if page == "Dashboard":
        dashboard_page(df)
    
    elif page == "Add Expense":
        add_expense_page()
    
    elif page == "View Expenses":
        view_expenses_page(df)
    
    elif page == "Analysis":
        analysis_page(df)
    
    elif page == "Reports":
        reports_page(df)


def dashboard_page(df):
    """Main dashboard with key metrics and charts."""
    
    st.title("💰 Expense Tracker Dashboard")
    
    # Display key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Spent",
            value=f"{CURRENCY_SYMBOL}{total_spending():,.2f}",
            delta=None
        )
    
    with col2:
        st.metric(
            label="Average Expense",
            value=f"{CURRENCY_SYMBOL}{average_expense():,.2f}",
            delta=None
        )
    
    with col3:
        st.metric(
            label="Total Transactions",
            value=len(df),
            delta=None
        )
    
    with col4:
        today = datetime.now()
        status = monthly_budget_status(today.year, today.month)
        st.metric(
            label="Budget Used",
            value=f"{status['percentage']:.1f}%",
            delta=f"{status['spent']} of {status['budget']}"
        )
    
    st.divider()
    
    if df.empty:
        st.info("📝 No expenses recorded yet. Start by adding expenses!")
        return
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Category-wise Spending")
        cat_spending = category_wise_spending()
        
        fig = px.pie(
            values=cat_spending.values,
            names=cat_spending.index,
            title="Distribution by Category",
            hole=0.3  # Creates donut chart
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Category Spending Amount")
        cat_spending = category_wise_spending()
        
        fig = px.bar(
            x=cat_spending.index,
            y=cat_spending.values,
            labels={'x': 'Category', 'y': f'Amount ({CURRENCY_SYMBOL})'},
            color=cat_spending.values,
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Monthly trend
    st.subheader("Monthly Spending Trend")
    monthly = monthly_spending()
    
    if not monthly.empty:
        # Convert period index to string
        monthly_str = pd.Series(
            monthly.values,
            index=[str(m) for m in monthly.index]
        )
        
        fig = go.Figure()
        
        # Add spending line
        fig.add_trace(go.Scatter(
            x=monthly_str.index,
            y=monthly_str.values,
            mode='lines+markers',
            name='Monthly Spending',
            line=dict(color='royalblue', width=3),
            marker=dict(size=10)
        ))
        
        # Add budget limit line
        fig.add_hline(
            y=MONTHLY_BUDGET_LIMIT,
            line_dash="dash",
            line_color="red",
            annotation_text="Budget Limit",
            annotation_position="right"
        )
        
        fig.update_layout(
            title="Monthly Spending Trend",
            xaxis_title="Month",
            yaxis_title=f"Amount ({CURRENCY_SYMBOL})",
            hovermode='x unified',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Budget Status
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Current Month Budget Status")
        today = datetime.now()
        status = monthly_budget_status(today.year, today.month)
        
        # Progress bar
        st.progress(min(status['percentage'] / 100, 1.0))
        
        # Display breakdown
        col_disp1, col_disp2, col_disp3 = st.columns(3)
        
        with col_disp1:
            st.metric("Budget Limit", f"{CURRENCY_SYMBOL}{status['budget']:,.2f}")
        
        with col_disp2:
            st.metric("Spent", f"{CURRENCY_SYMBOL}{status['spent']:,.2f}")
        
        with col_disp3:
            st.metric("Remaining", f"{CURRENCY_SYMBOL}{status['remaining']:,.2f}")
        
        st.caption(status['status'])
    
    with col2:
        st.subheader("Quick Stats")
        highest = highest_expense()
        lowest = lowest_expense()
        
        st.write(f"**Highest:** {CURRENCY_SYMBOL}{highest[0]:.2f}")
        st.caption(f"({highest[1]})")
        
        st.write(f"**Lowest:** {CURRENCY_SYMBOL}{lowest[0]:.2f}")
        st.caption(f"({lowest[1]})")


def add_expense_page():
    """Page for adding new expenses."""
    
    st.title("➕ Add New Expense")
    
    with st.form("expense_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            date = st.date_input(
                "Date",
                value=datetime.now(),
                max_value=datetime.now()
            )
            
            amount = st.number_input(
                "Amount",
                min_value=0.01,
                step=0.01,
                format="%.2f"
            )
        
        with col2:
            category = st.selectbox(
                "Category",
                CATEGORIES
            )
        
        note = st.text_input(
            "Note (optional)",
            placeholder="e.g., Lunch with friends"
        )
        
        submitted = st.form_submit_button("Add Expense", use_container_width=True)
        
        if submitted:
            # Convert date to string
            date_str = date.strftime(DATE_FORMAT)
            
            if add_expense(date_str, category, amount, note):
                st.success("✅ Expense added successfully!")
                st.balloons()
                # Rerun to update data
                st.rerun()
            else:
                st.error("❌ Failed to add expense")


def view_expenses_page(df):
    """Page for viewing and managing expenses."""
    
    st.title("👀 View & Manage Expenses")
    
    if df.empty:
        st.info("📝 No expenses recorded yet.")
        return
    
    # Preparation of data for display
    display_df = df.copy()
    display_df['Date'] = display_df['Date'].dt.strftime(DATE_FORMAT)
    
    # Sort by date descending
    display_df = display_df.sort_values('Date', ascending=False)
    
    # Display as table
    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )
    
    st.divider()
    
    # Download CSV
    csv = df.to_csv(index=False)
    st.download_button(
        label="📥 Download as CSV",
        data=csv,
        file_name=f"expenses_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )
    
    # Edit/Delete operations
    st.subheader("Edit or Delete Expense")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("⚠️ Edit/Delete functionality requires row numbers. Display raw data for selection.")
        
        if st.checkbox("Show edit/delete options"):
            expenses = get_all_expenses()
            
            row_num = st.number_input(
                "Select expense row number to edit/delete",
                min_value=0,
                max_value=len(expenses)-1 if expenses else 0,
                step=1
            )
            
            if expenses and row_num < len(expenses):
                selected = expenses[row_num]
                st.write(f"Selected: {selected}")
                
                col_edit, col_del = st.columns(2)
                
                with col_edit:
                    if st.button("Edit"):
                        st.session_state.edit_mode = True
                        st.session_state.edit_row = row_num
                
                with col_del:
                    if st.button("Delete"):
                        delete_expense(row_num)
                        st.success("✅ Expense deleted")
                        st.rerun()


def analysis_page(df):
    """Page for detailed analysis."""
    
    st.title("📈 Detailed Analysis")
    
    if df.empty:
        st.info("📝 No expenses recorded yet.")
        return
    
    # Tabs for different analyses
    tab1, tab2, tab3, tab4 = st.tabs(
        ["By Category", "By Date Range", "By Month", "Statistics"]
    )
    
    with tab1:
        st.subheader("Filter by Category")
        
        selected_category = st.selectbox(
            "Select Category",
            CATEGORIES,
            key="category_filter"
        )
        
        filtered = filter_by_category(selected_category)
        
        if filtered.empty:
            st.info(f"No expenses in {selected_category}")
        else:
            st.write(f"**Total in {selected_category}: {CURRENCY_SYMBOL}{filtered['Amount'].sum():.2f}**")
            st.write(f"**Number of transactions: {len(filtered)}**")
            st.write(f"**Average: {CURRENCY_SYMBOL}{filtered['Amount'].mean():.2f}**")
            
            filtered['Date'] = filtered['Date'].dt.strftime(DATE_FORMAT)
            st.dataframe(filtered, use_container_width=True, hide_index=True)
    
    with tab2:
        st.subheader("Filter by Date Range")
        
        col1, col2 = st.columns(2)
        
        with col1:
            start_date = st.date_input("Start Date")
        
        with col2:
            end_date = st.date_input("End Date")
        
        if start_date <= end_date:
            start_str = start_date.strftime(DATE_FORMAT)
            end_str = end_date.strftime(DATE_FORMAT)
            
            # Manual filtering using Pandas
            mask = (df['Date'].dt.date >= start_date) & (df['Date'].dt.date <= end_date)
            filtered = df[mask]
            
            if filtered.empty:
                st.info("No expenses in this date range")
            else:
                st.write(f"**Total: {CURRENCY_SYMBOL}{filtered['Amount'].sum():.2f}**")
                st.write(f"**Number of transactions: {len(filtered)}**")
                
                filtered_display = filtered.copy()
                filtered_display['Date'] = filtered_display['Date'].dt.strftime(DATE_FORMAT)
                st.dataframe(filtered_display, use_container_width=True, hide_index=True)
        else:
            st.error("Start date must be before end date")
    
    with tab3:
        st.subheader("Filter by Month")
        
        col1, col2 = st.columns(2)
        
        with col1:
            year = st.number_input("Year", min_value=2000, value=datetime.now().year)
        
        with col2:
            month = st.slider("Month", 1, 12, value=datetime.now().month)
        
        filtered = filter_by_month(year, month)
        
        if filtered.empty:
            st.info(f"No expenses in {month}/{year}")
        else:
            status = monthly_budget_status(year, month)
            
            col_stat1, col_stat2, col_stat3 = st.columns(3)
            
            with col_stat1:
                st.metric("Total Spent", f"{CURRENCY_SYMBOL}{status['spent']:.2f}")
            
            with col_stat2:
                st.metric("Budget", f"{CURRENCY_SYMBOL}{status['budget']:.2f}")
            
            with col_stat3:
                st.metric("Remaining", f"{CURRENCY_SYMBOL}{status['remaining']:.2f}")
            
            st.progress(min(status['percentage'] / 100, 1.0))
            
            filtered_display = filtered.copy()
            filtered_display['Date'] = filtered_display['Date'].dt.strftime(DATE_FORMAT)
            st.dataframe(filtered_display, use_container_width=True, hide_index=True)
    
    with tab4:
        st.subheader("Overall Statistics")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Expenses", len(df))
            st.metric("Average Expense", f"{CURRENCY_SYMBOL}{average_expense():.2f}")
        
        with col2:
            highest = highest_expense()
            st.metric("Highest Expense", f"{CURRENCY_SYMBOL}{highest[0]:.2f}")
            st.metric("Lowest Expense", f"{CURRENCY_SYMBOL}{lowest_expense()[0]:.2f}")
        
        with col3:
            st.metric("Total Spending", f"{CURRENCY_SYMBOL}{total_spending():.2f}")
            date_range = f"{df['Date'].min().strftime('%Y-%m-%d')} to {df['Date'].max().strftime('%Y-%m-%d')}"
            st.caption(f"Period: {date_range}")


def reports_page(df):
    """Page for generating reports."""
    
    st.title("📄 Reports & Exports")
    
    if df.empty:
        st.info("📝 No expenses recorded yet.")
        return
    
    # Summary Report
    st.subheader("Summary Report")
    
    summary = f"""
    **EXPENSE SUMMARY REPORT**
    
    📊 Overall Statistics:
    - Total Expenses: {len(df)}
    - Total Amount Spent: {CURRENCY_SYMBOL}{total_spending():,.2f}
    - Average per Expense: {CURRENCY_SYMBOL}{average_expense():,.2f}
    - Highest Expense: {CURRENCY_SYMBOL}{highest_expense()[0]:,.2f}
    - Lowest Expense: {CURRENCY_SYMBOL}{lowest_expense()[0]:,.2f}
    - Date Range: {df['Date'].min().strftime('%Y-%m-%d')} to {df['Date'].max().strftime('%Y-%m-%d')}
    
    💰 Category Breakdown:
    """
    
    cat_spending = category_wise_spending()
    total = cat_spending.sum()
    
    for category, amount in cat_spending.items():
        percentage = (amount / total * 100) if total > 0 else 0
        summary += f"\n    - {category}: {CURRENCY_SYMBOL}{amount:,.2f} ({percentage:.1f}%)"
    
    st.markdown(summary)
    
    # Download Report
    st.download_button(
        label="📥 Download Summary Report (Text)",
        data=summary,
        file_name=f"expense_report_{datetime.now().strftime('%Y%m%d')}.txt"
    )
    
    st.divider()
    
    # Export Options
    st.subheader("Export Data")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # CSV Export
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download as CSV",
            data=csv,
            file_name=f"expenses_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    
    with col2:
        # JSON Export
        json = df.to_json(orient='records', indent=2)
        st.download_button(
            label="📥 Download as JSON",
            data=json,
            file_name=f"expenses_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json"
        )


if __name__ == "__main__":
    main()
