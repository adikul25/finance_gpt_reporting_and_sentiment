# Import Packages
from fastapi import APIRouter

'''Defining Global variables'''
router = APIRouter()

'''This endpoint keeps the server active'''
@router.get(
        "/healthcheck",
        name="healthcheck")
def get_healthcheck():
    healthcheck = {'is_alive':True}
    
    return healthcheck