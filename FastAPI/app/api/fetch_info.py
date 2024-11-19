import yfinance as yf
import numpy as np
import pandas as pd
import json

class StockData:
    def __init__(self, ticker_symbol):
        self.ticker = yf.Ticker(ticker_symbol)
        
    def replace_nan_with_none(self, data):
        if isinstance(data, dict):
            return {k: self.replace_nan_with_none(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [self.replace_nan_with_none(v) for v in data]
        elif isinstance(data, (int, float)) and (np.isnan(data) or pd.isna(data)):
            return None
        elif data is pd.NA:
            return None
        else:
            return data
        
        
    def get_info(self):
        info = self.ticker.info
        return self.replace_nan_with_none(info)

    def get_balance_sheet(self):
        balance_sheet = self.ticker.balance_sheet
        return self.replace_nan_with_none(balance_sheet.to_dict())

    def get_cash_flow(self):
        cash_flow = self.ticker.cash_flow
        return self.replace_nan_with_none(cash_flow.to_dict())

    def get_earnings_history(self):
        earnings_history = self.ticker.earnings_history
        return self.replace_nan_with_none(earnings_history)

    def get_eps_trend(self):
        eps_trend = self.ticker.eps_trend
        return self.replace_nan_with_none(eps_trend)

    def get_financials(self):
        financials = self.ticker.financials
        return self.replace_nan_with_none(financials.to_dict())

    def get_income_statement(self):
        income_stmt = self.ticker.income_stmt
        return self.replace_nan_with_none(income_stmt.to_dict())

    def get_insider_purchases(self):
        insider_purchases = self.ticker.insider_purchases
        #json_str = insider_purchases.to_json(orient="records")
        #data = json.loads(json_str)
        return self.replace_nan_with_none(insider_purchases.to_dict())

    def get_insider_transactions(self):
        insider_transactions = self.ticker.insider_transactions
        # json_str = insider_transactions.to_json(orient="records")
        # data = json.loads(json_str)
        return self.replace_nan_with_none(insider_transactions.to_dict())

    def get_institutional_holders(self):
        institutional_holders = self.ticker.institutional_holders
        # data_test = self.replace_nan_with_none(institutional_holders)
        # json_str = data_test.to_json(orient="records")
        # #data = json.loads(json_str)
        return self.replace_nan_with_none(institutional_holders.to_dict())

    def get_mutualfund_holders(self):
        mutualfund_holders = self.ticker.mutualfund_holders
        # json_str = mutualfund_holders.to_json(orient="records")
        # data = json.loads(json_str)
        return self.replace_nan_with_none(mutualfund_holders.to_dict())

    def get_recommendations(self):
        recommendations = self.ticker.recommendations
        # json_str = recommendations.to_json(orient="records")
        # data = json.loads(json_str)
        return self.replace_nan_with_none(recommendations.to_dict())

    def get_revenue_estimate(self):
        revenue_estimate = self.ticker.revenue_estimate
        # json_str = revenue_estimate.to_json(orient="records")
        # data = json.loads(json_str)
        return self.replace_nan_with_none(revenue_estimate.to_dict())