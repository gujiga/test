"""
Daily Joke Package

A simple package to get daily jokes.
"""

from .utils import get_random_joke, get_daily_joke

__version__ = "0.1.0"
__all__ = ["get_random_joke", "get_daily_joke"]