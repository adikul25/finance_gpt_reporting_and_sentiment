from langchain_google_genai import GoogleGenerativeAI

class FinancialAnalyzer:
    def __init__(self, model="gemini-1.5-flash-8b", temperature=0.2):
        self.llm = GoogleGenerativeAI(model=model, google_api_key='', temperature=temperature)

    def create_report(self, company_name, financial_data):
        prompt = f"""
                You are a financial analyst, whose reports investors read for market insights. Below are the financial metrics of {company_name}. Analyze the data and generate a report with insights.

                Financial Metrics:
                {financial_data}

                Instructions:
                - Analyze the metrics and its value, listing out key points for investor.
                - Identify any trends, strengths, or weaknesses for investor.
                - Provide a comprehensive report with actionable insights and recommendations for investor.

                Report:

                Output should be well formatted
                """
        report = self.llm(prompt)
        return report

    def query_llm(self, query):
        answer = self.llm(query)
        return answer
