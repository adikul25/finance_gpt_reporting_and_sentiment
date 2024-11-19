import streamlit as st
from utils import fetch_data, display_data, generate_report

# Title for the app
#st.title('Stock Analysis')
st.sidebar.info(
    """
    ### Stock Analysis App
    This app allows you to analyze stock data by retrieving information from various endpoints through a FastAPI backend.
    
    #### Features:
    - **Fetch Information**: Retrieve details about a stock ticker.
    - **Financial Statements**: Get data on balance sheets, cash flows, and income statements.
    - **Insider & Institutional Holdings**: View insider purchases, transactions, and institutional holders.
    - **Recommendations**: See analyst recommendations and revenue estimates.
    
    #### Instructions:
    1. Enter a valid stock ticker in the text input field.
    2. Select the type of data you wish to retrieve from the dropdown menu.
    3. Press **Fetch Data** to display the information.
    4. Press **Generate Report** to create a custom report based on fetched data.
    
    Enjoy your analysis!
    """
)

st.sidebar.write("### Disclaimer")
st.sidebar.warning(
    """
    This application is for **educational purposes only**. 
    The data and reports provided are not intended for financial or investment advice. 
    Please consult a financial advisor for professional guidance.
    """
)

# Input field for stock ticker
ticker = st.text_input("Enter Stock Ticker:", "")
endpoints = [
    "fetch_info",
    "fetch_balance_sheet",
    "fetch_cash_flow",
    "fetch_earnings_history",
    "fetch_eps_trend",
    "fetch_financials",
    "fetch_income_statement",
    "fetch_insider_purchases",
    "fetch_insider_transactions",
    "fetch_institutional_holders",
    "fetch_mutualfund_holders",
    "fetch_recommendations",
    "fetch_revenue_estimate"
]

# Select box for endpoints
selected_endpoint = st.selectbox("Select the data to retrieve:", options=endpoints)

# Fetch Data button
if st.button('Fetch Data'):
    if ticker and selected_endpoint:
        data = fetch_data(ticker, selected_endpoint)
        if data:
            display_data(data, selected_endpoint)
    else:
        st.warning("Please enter a valid stock ticker and select an endpoint.")

# Generate Report button
if st.button('Generate Report'):
    if 'llm_input' in st.session_state and st.session_state['llm_input']:
        result = generate_report(ticker, st.session_state['llm_input'])
        if result:
            st.write(result)
    else:
        st.warning("Please fetch the data first by pressing 'Fetch Data' before generating the report.")
