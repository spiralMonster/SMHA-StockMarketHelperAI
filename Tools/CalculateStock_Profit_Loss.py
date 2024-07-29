from pydantic import BaseModel,Field
from langchain.tools import tool

class CalculationInput(BaseModel):
    param1: float =Field(description="The current stock price")
    param2: float =Field(description="The stock price in future at particular timestamp")

@tool("Calculate profit/loss",args_schema=CalculationInput,return_direct=True)
def calculate(param1,param2):
    return abs(param1-param2)

