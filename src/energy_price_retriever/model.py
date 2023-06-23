"""Module with the data model.

This module contains the data model for the application. The model uses
Pydantic for data validation.
"""
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class PriceType(int, Enum):
    POWER = 1
    GAS = 2

class Price(BaseModel):
    """Model for a Price.
    
    Defines how a price is modeled. Contains the type of price (Power or Gas),
    the datetime object for the start of the price and the price iteself.

    Attributes:
        start_datetime: when the price starts.
        type: the type of the price (Power or Gas).
        price_in_eurocents: the price in Eurocents.
    """
    start_datetime: datetime
    price_type: PriceType
    price_in_eurocents: int

    class Config:
        validate_assignment = True