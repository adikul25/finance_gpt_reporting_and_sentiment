# Import Packages
from fastapi import APIRouter
from api import endpoint
from api import healthcheck
from api import llm_endpoint

"""Defining API Routers"""
api_router = APIRouter()
api_router.include_router(healthcheck.router)
api_router.include_router(endpoint.router)
api_router.include_router(llm_endpoint.router)