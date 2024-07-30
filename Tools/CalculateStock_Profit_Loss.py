from pydantic import BaseModel,Field
from langchain.tools import tool

class CalculationInput(BaseModel):
    param1: float =Field(...,description="The current stock price")
    param2: float =Field(...,description="The stock price in future at particular timestamp")

@tool("Calculate profit/loss",args_schema=CalculationInput,return_direct=True)
def calculate(param1,param2):
    """

    :param param1: Current Stock Price
    :param param2: Stock Price in future

    Calculate the loss/profit using the current stock price and the stock price in future
    and return it.
    """
    return abs(param1-param2)

