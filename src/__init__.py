"""Smart Shopping Assistant - AI-powered shopping recommendations"""

__version__ = "0.1.0"

from .shopping_assistant import main
from .location import find_nearby_stores
from .pricing import get_prices
from .ai_recommender import generate_shopping_list

__all__ = [
    'main',
    'find_nearby_stores',
    'get_prices',
    'generate_shopping_list',
]
