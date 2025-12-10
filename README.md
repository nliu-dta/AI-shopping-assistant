# 🛒 Smart Shopping Assistant with AI

An intelligent shopping assistant that helps Australian shoppers find the best deals by combining price comparison, location awareness, and AI-powered recommendations.

## 🌟 Features

- **🗺️ Location-Aware Shopping**: Finds supermarkets near your location using Google Maps
- **💰 Real-Time Price Comparison**: Searches prices across major Australian retailers (Coles, Woolworths, Aldi, Chemist Warehouse)
- **🤖 AI-Powered Recommendations**: Uses Google's Gemini AI to analyze deals and suggest optimal shopping strategies
- **📋 Smart Shopping Lists**: Automatically groups items by store to minimize trips
- **💡 Deal Analysis**: AI explains whether prices are good based on current market comparison

## 🎯 What Makes This Different

Unlike existing Australian shopping apps (Frugl, WiseList, Grocerize), this assistant:
- Uses AI to provide intelligent, context-aware recommendations
- Considers your physical location to optimize shopping routes
- Groups items by nearby stores to save time and fuel
- Analyzes whether splitting purchases across stores is worth the extra effort
- Completely free and customizable

## 🚀 Demo
```
🗺️  LOCATION-SMART SHOPPING ASSISTANT
============================================================

Enter your location: Belconnen, ACT

🔍 Finding stores near Belconnen, ACT...
✓ Found: Aldi, Coles, Woolworths

🛒 Checking 3 products...
  • Omo Liquid 2L... ✓ $13.50
  • Colgate Toothpaste 110g... ✓ $3.50
  • Pantene Shampoo 375ml... ✓ $4.99

============================================================
🤖 AI SHOPPING RECOMMENDATION
============================================================

🛒 ONE-STOP SHOP at Coles Belconnen:
  - Omo 2L: $13.50
  - Colgate: $3.50
  - Pantene: $4.99

💰 Total: $21.99
🎯 Strategy: Everything's available at competitive prices 
at Coles. Shop there to save time!
```

## 🛠️ Tech Stack

- **Python 3.10+**
- **Google Maps Places API (New)**: Location-based store discovery
- **SerpAPI**: Google Shopping price scraping
- **Google Gemini AI**: Intelligent recommendation engine
- **googlemaps**: Python client for Google Maps
- **python-dotenv**: Secure environment variable management

## 📦 Installation

🛠️ Development Setup
This project uses uv for modern, high-performance dependency management.
Prerequisites
uv installed (curl -LsSf https://astral.sh/uv/install.sh | sh)
Quick Start
code
Bash
# 1. Clone the repository
git clone https://github.com/yourusername/smart-shopping-assistant.git
cd smart-shopping-assistant

# 2. Sync dependencies (creates virtualenv automatically)
uv sync

# 3. Set up environment variables
cp .env.example .env
# (Edit .env with your API keys)

# 4. Run the application
uv run src/main.py

### 3. Set Up API Keys

You'll need three API keys (all have free tiers):

#### a) Google Maps API Key
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable these APIs:
   - Places API (New)
   - Geocoding API
4. Create credentials → API Key
5. **Free tier**: $200/month credit (plenty for personal use)

#### b) Google Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create API Key
3. **Free tier**: 15 requests/minute

#### c) SerpAPI Key
1. Go to [SerpAPI](https://serpapi.com/)
2. Sign up for free account
3. **Free tier**: 100 searches/month

### 4. Configure Environment Variables

Create a `.env` file in the project root:
```bash
GOOGLE_MAPS_KEY=your_google_maps_api_key_here
GEMINI_KEY=your_gemini_api_key_here
SERPAPI_KEY=your_serpapi_key_here
```

**Important**: Never commit `.env` to Git! It's already in `.gitignore`.

## 🎮 Usage

### Basic Usage
```bash
python shopping_assistant.py
```

### Customize Your Shopping List

Edit the `MY_PRODUCTS` list in the code:
```python
MY_PRODUCTS = [
    "Omo Liquid 2L",
    "Colgate Toothpaste 110g",
    "Pantene Shampoo 375ml",
 
]
```

### Check Single Product
```python
from shopping_assistant import check_single_product

check_single_product("Finish Dishwasher Tablets")
```

## 🗂️ Project Structure
```
smart-shopping-assistant/
├── shopping_assistant.py       # Main application
├── .env                        # API keys (not in repo)
├── .env.example               # Template for API keys
├── .gitignore                 # Git ignore rules
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── tests/                     # Unit tests (optional)
```

## 🧪 Running in Google Colab

Prefer Colab? Use Colab Secrets for better security:

1. Open notebook in Colab
2. Click 🔑 (Secrets) in left sidebar
3. Add your three API keys as secrets
4. Run the code - it will auto-detect and use Colab Secrets

## 💰 Cost Estimate

For typical weekly shopping (checking ~10 products once per week):

| Service | Free Tier | Monthly Usage | Cost |
|---------|-----------|---------------|------|
| Google Maps | $200 credit | ~8 requests | $0.00 |
| Gemini AI | 15 req/min | ~40 requests | $0.00 |
| SerpAPI | 100 searches | ~40 searches | $0.00 |
| **Total** | | | **$0.00** |

## 🔒 Security Best Practices

- ✅ API keys stored in `.env` (excluded from Git)
- ✅ HTTP referrer restrictions on Google Maps API
- ✅ API usage monitoring enabled
- ✅ Billing alerts set at $10/month
- ✅ Rate limiting implemented


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built as a learning project exploring AI applications in everyday life
- Inspired by the high cost of living in Australia and the need for smarter shopping tools



## ⚠️ Disclaimer

This tool is for personal use only. Please respect the terms of service of all APIs used. Price data may not always be accurate or up-to-date. Always verify prices at the store.

---

**Made with ❤️ in Australia 🇦🇺**

*Last updated: Dec 2025*
