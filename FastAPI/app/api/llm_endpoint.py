from fastapi import APIRouter
from api.llm_operations import FinancialAnalyzer
from api.models import LLMInput

router = APIRouter()

@router.post("/generate_report")
async def ep_retrive_stock_info(input:LLMInput):
        """This endpoint generates a report based on the input provided by the user."""
        analyzer = FinancialAnalyzer()
        info = analyzer.create_report(input.ticker, input.metrics)
        return {"llm_output":info}