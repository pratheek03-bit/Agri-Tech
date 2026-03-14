# services/__init__.py

"""
Services Package Initialization

This module initializes all backend services such as:
- Location tracking service
- Weather data service

It allows easy imports in other files like app.py.
"""

# Import service classes/functions

from .locations import LocationService
from .weather_service import get_weather


# Export services for easy access
__all__ = [
    "LocationService",
    "get_weather"
]