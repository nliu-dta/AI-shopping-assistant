"""Price comparison using SerpAPI"""

import os
from serpapi import GoogleSearch


def get_prices(product_name: str) -> list[dict]:
    """
    Get current prices from Google Shopping
    
    Args:
        product_name: Product to search for
        
    Returns:
        List of price dictionaries with keys: name, price, store
    """
    api_key = os.getenv('SERPAPI_KEY')
    if not api_key:
        print("❌ SERPAPI_KEY not found in environment")
        return []
    
    params = {
        "engine": "google_shopping",
        "q": f"{product_name} Australia",
        "location": "Sydney, Australia",
        "gl": "au",
        "api_key": api_key
    }
    
    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        items = results.get('shopping_results', [])
        
        prices = []
        for item in items[:15]:
            try:
                price_str = str(item.get('extracted_price', item.get('price', '0')))
                price = float(price_str.replace('$', '').replace(',', ''))
                
                prices.append({
                    'name': item.get('title', 'N/A'),
                    'price': price,
                    'store': item.get('source', 'Unknown')
                })
            except:
                continue
        
        return prices
    
    except Exception as e:
        print(f"❌ Error getting prices: {e}")
        return []
