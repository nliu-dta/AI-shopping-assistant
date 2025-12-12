🛒 Smart Shopping Assistant with AI
An intelligent shopping assistant that helps Australian shoppers find the best deals by combining price comparison, location awareness, and AI-powered recommendations.
🌟 Overview
Living costs are rising, and comparing catalogues manually is time-consuming. This tool acts as a "Cost of Living Copilot," automating the search for the best prices on your specific grocery list across major Australian retailers (Coles, Woolworths, Aldi). It uses Generative AI not just to find prices, but to reason about them—calculating whether the fuel cost of driving to a second store is worth the savings.
✨ Key Features
🗺️ Location-Aware Shopping: Finds supermarkets near your specific coordinates using Google Maps (New Places API).
💰 Real-Time Price Comparison: Scrapes and compares prices across Coles, Woolworths, Aldi, and IGA.
🤖 AI-Powered Strategy: Uses Google Gemini to analyze the total cart and suggest the optimal logistics (e.g., "Save $15 by splitting the trip, or pay $3 extra to save 20 minutes at one store").
📋 Smart Shopping Lists: Automatically categorizes items to minimize time in-aisle.
🛡️ Privacy First: Runs locally; no data is sent to third-party servers other than necessary API calls.
🚀 Demo
code
Text
🗺️  LOCATION-SMART SHOPPING ASSISTANT
============================================================
Enter your location: Belconnen, ACT

🔍 Finding stores near Belconnen, ACT...
✓ Found: Aldi (1.2km), Coles (1.5km), Woolworths (1.6km)

🛒 Checking Shopping List...
  • Omo Liquid 2L......... $13.50 (Coles) | $22.00 (Woolies)
  • Tim Tams Original..... $2.50 (Woolies) | $4.50 (Coles)
  • Weet-Bix 1.2kg........ $5.00 (Aldi)    | $5.50 (Coles)
  • Devondale Milk 3L..... $4.50 (All stores)
  • Bananas (1kg)......... $3.50 (Aldi)

============================================================
🤖 AI SHOPPING RECOMMENDATION (GEMINI)
============================================================

🛒 STRATEGY: SPLIT TRIP (High Savings)
---------------------------------------
1. STOP 1: WOOLWORTHS
   - Buy: Tim Tams (Half price!)
   - Cost: $2.50

2. STOP 2: ALDI (Primary Shop)
   - Buy: Weet-Bix, Bananas, Milk
   - Cost: $13.00

3. STOP 3: COLES
   - Buy: Omo Liquid (Huge special)
   - Cost: $13.50

💰 Total Spend: $29.00
📉 Savings vs Single Store: You save $12.50 by avoiding the full price Omo at Woolworths.
🚗 Fuel Impact: Stores are within 500m of each other; split trip is recommended.
🛠️ Tech Stack
Core: Python 3.10+
Package Manager: uv (Modern, high-performance replacement for pip)
APIs:
Google Maps Places API: Geo-location context.
SerpAPI: Real-time product pricing.
Google Gemini Pro: Logic and recommendation engine.
Environment: python-dotenv for secure key management.
🔮 Roadmap & Next Steps
I am actively developing this tool. Upcoming features include:

👨‍🍳 AI "Chef Mode": Since the AI knows what is in your cart (e.g., Mince, Pasta, Tomato Paste), it will automatically generate 3 dinner recipes using only the ingredients you just bought.

📊 Historical Price Tracking: Building a local database (SQLite) to track price inflation on staple items over time.

🐳 Docker Support: Containerizing the application for easy deployment.

📱 Telegram/WhatsApp Bot: Moving the interface from Terminal to a Chatbot for on-the-go checks.
📦 Installation
This project uses uv for fast, reliable dependency management.
Prerequisites
Install uv: curl -LsSf https://astral.sh/uv/install.sh | sh
A Google Cloud Project (for Maps & Gemini)
Quick Start
code
Bash
# 1. Clone the repository
git clone https://github.com/nliu-dta/AI-shopping-assistant.git
cd AI-shopping-assistant

# 2. Sync dependencies (creates virtualenv automatically)
uv sync

# 3. Set up environment variables
cp .env.example .env
# (Open .env and paste your API keys)

# 4. Run the application
uv run src/main.py
🔑 API Configuration
You will need three API keys (all offer free tiers sufficient for personal use).
Google Maps API (Cloud Console): Enable "Places API (New)".
Google Gemini API (Google AI Studio): Get a free API key.
SerpAPI: Sign up for a free account (100 searches/month).
Security Note: API keys are stored in .env and added to .gitignore. They are never hardcoded.
🎮 Usage
To customize your grocery list, edit the MY_PRODUCTS list in src/main.py:
code
Python
MY_PRODUCTS = [
    "Omo Liquid 2L",
    "Colgate Toothpaste 110g",
    "Arnott's Tim Tams Original",
    "Sanitarium Weet-Bix 1.2kg",
    "Devondale Full Cream Milk 3L",
    "Cavendish Bananas 1kg"
]
💰 Cost Estimate
For typical weekly shopping (checking ~10 products once per week):
Service	Free Tier	Monthly Usage	Cost
Google Maps	$200 credit	~8 requests	$0.00
Gemini AI	15 req/min	~40 requests	$0.00
SerpAPI	100 searches	~60 searches	$0.00
Total			$0.00
⚠️ Disclaimer
This tool is for personal educational use. Please respect the Terms of Service of all APIs used.
Made with ❤️ in Canberra 🇦🇺
