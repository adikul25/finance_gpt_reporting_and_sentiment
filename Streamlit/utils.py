import json
import requests
import pandas as pd
import streamlit as st

# FastAPI base URL
BASE_URL = 'http://fastapi:8000'

def fetch_data(ticker, endpoint):
    """Fetch data from the specified endpoint."""
    input_data = {"name": ticker}
    try:
        res = requests.post(f"{BASE_URL}/{endpoint}", data=json.dumps(input_data))
        res.raise_for_status()
        data = json.loads(res.text)
        st.session_state['llm_input'] = data  # Store data in session state
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching data: {e}")
        return None

def display_data(data, endpoint):
    """Display the fetched data as JSON or DataFrame based on endpoint."""
    if endpoint == 'fetch_info':
        st.write(data)
    else:
        df = pd.DataFrame(data)
        st.write(df)
    st.success(f"Data fetched successfully from '{endpoint}' endpoint.")

def generate_report(ticker, llm_input):
    """Generate a report by sending metrics to FastAPI."""
    try:
        metrics_str = json.dumps(llm_input)
        tickers = json.dumps(ticker)
        request_data = {"ticker": tickers, "metrics": metrics_str}
        
        response = requests.post(f"{BASE_URL}/generate_report", data=json.dumps(request_data))
        response.raise_for_status()
        
        result = response.json()
        return result["llm_output"]
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while generating the report: {e}")
        return None
