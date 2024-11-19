from fastapi import APIRouter
from api.fetch_info import StockData
from api.models import UserInput

router = APIRouter()

@router.post("/fetch_info")
def ep_retrive_stock_info(input:UserInput):
    response = StockData(input.name)
    info = response.get_info()
    return info

@router.post("/fetch_balance_sheet")
def ep_retrieve_balance_sheet(input: UserInput):
    response = StockData(input.name)
    return response.get_balance_sheet()

@router.post("/fetch_cash_flow")
def ep_retrieve_cash_flow(input: UserInput):
    response = StockData(input.name)
    return response.get_cash_flow()

@router.post("/fetch_earnings_history")
def ep_retrieve_earnings_history(input: UserInput):
    response = StockData(input.name)
    return response.get_earnings_history()

@router.post("/fetch_eps_trend")
def ep_retrieve_eps_trend(input: UserInput):
    response = StockData(input.name)
    return response.get_eps_trend()

@router.post("/fetch_financials")
def ep_retrieve_financials(input: UserInput):
    response = StockData(input.name)
    return response.get_financials()

@router.post("/fetch_income_statement")
def ep_retrieve_income_statement(input: UserInput):
    response = StockData(input.name)
    return response.get_income_statement()

@router.post("/fetch_insider_purchases")
def ep_retrieve_insider_purchases(input: UserInput):
    response = StockData(input.name)
    return response.get_insider_purchases()

@router.post("/fetch_insider_transactions")
def ep_retrieve_insider_transactions(input: UserInput):
    response = StockData(input.name)
    return response.get_insider_transactions()

@router.post("/fetch_institutional_holders")
def ep_retrieve_institutional_holders(input: UserInput):
    response = StockData(input.name)
    return response.get_institutional_holders()

@router.post("/fetch_mutualfund_holders")
def ep_retrieve_mutualfund_holders(input: UserInput):
    response = StockData(input.name)
    return response.get_mutualfund_holders()

@router.post("/fetch_recommendations")
def ep_retrieve_recommendations(input: UserInput):
    response = StockData(input.name)
    return response.get_recommendations()

@router.post("/fetch_revenue_estimate")
def ep_retrieve_revenue_estimate(input: UserInput):
    response = StockData(input.name)
    return response.get_revenue_estimate()