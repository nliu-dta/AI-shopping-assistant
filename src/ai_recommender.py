"""AI recommendations using Google Gemini"""

import os
import google.generativeai as genai


def generate_shopping_list(location: str, stores: list[str], 
                          products_data: dict) -> str:
    """
    Generate AI-powered shopping recommendations
    
    Args:
        location: User's location
        stores: List of nearby stores
        products_data: Dict mapping product names to price lists
        
    Returns:
        AI-generated shopping recommendation as string
    """
    api_key = os.getenv('GEMINI_KEY')
    if not api_key:
        return "❌ GEMINI_KEY not found in environment"
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    # Build context for AI
    summary = f"Location: {location}\n"
    summary += f"Nearby stores: {', '.join(stores)}\n\n"
    summary += "Products and prices:\n"
    
    for product, prices in products_data.items():
        if prices:
            summary += f"\n{product}:\n"
            for p in prices[:3]:
                summary += f"  ${p['price']:.2f} at {p['store']}\n"
    
    prompt = f"""
{summary}

Create a smart shopping list:

1. 🛒 SHOPPING PLAN - Group items by store to minimize trips
2. 💰 TOTAL COST - Calculate total cost
3. 🎯 BEST STRATEGY - Recommend: one store or multiple stores?

Consider convenience vs savings. Be brief and practical.
"""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ AI generation failed: {e}"
