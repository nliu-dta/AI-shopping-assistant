"""
Smart Shopping Assistant - Main Application
Location-aware AI-powered shopping recommendations for Australian shoppers
"""

import os
from dotenv import load_dotenv
from location import find_nearby_stores
from pricing import get_prices
from ai_recommender import generate_shopping_list
# Load environment variables
load_dotenv()

# Product list
MY_PRODUCTS = [
    "Omo Liquid 2L",
    "Colgate Toothpaste 110g",
    "Pantene Shampoo 375ml"
]


def main():
    """Main application entry point"""
    print("\n" + "="*60)
    print("🛒 SMART SHOPPING ASSISTANT")
    print("="*60)
    
    # Get user location
    location = input("\nEnter your location (e.g., 'Belconnen, ACT'): ").strip()
    if not location:
        location = "Belconnen, ACT"
    
    # Find nearby stores
    print(f"\n🔍 Finding stores near {location}...")
    stores = find_nearby_stores(location)
    
    if not stores:
        print("❌ No stores found nearby")
        return
    
    print(f"✓ Found: {', '.join(stores)}\n")
    
    # Get prices for all products
    print(f"🛒 Checking {len(MY_PRODUCTS)} products...")
    all_data = {}
    
    for product in MY_PRODUCTS:
        print(f"  • {product}...", end=" ")
        prices = get_prices(product)
        
        # Filter to nearby stores
        local_prices = [p for p in prices if p['store'] in stores]
        
        if local_prices:
            cheapest = min(local_prices, key=lambda x: x['price'])
            print(f"✓ ${cheapest['price']:.2f}")
            all_data[product] = local_prices
        else:
            print("✗")
            all_data[product] = []
    
    # Generate AI recommendation
    print("\n" + "="*60)
    print("🤖 AI SHOPPING RECOMMENDATION")
    print("="*60 + "\n")
    
    recommendation = generate_shopping_list(location, stores, all_data)
    print(recommendation)
    print("\n" + "="*60)


if __name__ == "__main__":
    main()
