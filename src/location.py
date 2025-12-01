"""Location services using Google Maps API"""

import os
import requests
import googlemaps


def find_nearby_stores(location: str) -> list[str]:
    """
    Find supermarkets near a given location
    
    Args:
        location: Address or suburb (e.g., "Belconnen, ACT")
        
    Returns:
        List of store names (e.g., ["Coles", "Woolworths"])
    """
    api_key = os.getenv('GOOGLE_MAPS_KEY')
    if not api_key:
        print("❌ GOOGLE_MAPS_KEY not found in environment")
        return []
    
    gmaps = googlemaps.Client(key=api_key)
    
    try:
        # Geocode location
        geocode = gmaps.geocode(location)
        if not geocode:
            return []
        
        lat = geocode[0]['geometry']['location']['lat']
        lng = geocode[0]['geometry']['location']['lng']
        
        # Search nearby supermarkets using NEW Places API
        url = "https://places.googleapis.com/v1/places:searchNearby"
        
        headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": api_key,
            "X-Goog-FieldMask": "places.displayName"
        }
        
        data = {
            "includedTypes": ["supermarket"],
            "maxResultCount": 20,
            "locationRestriction": {
                "circle": {
                    "center": {"latitude": lat, "longitude": lng},
                    "radius": 3000.0
                }
            }
        }
        
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code != 200:
            print(f"❌ Places API error: {response.status_code}")
            return []
        
        # Extract and normalize store names
        stores = set()
        for place in response.json().get('places', []):
            name = place.get('displayName', {}).get('text', '').lower()
            
            if 'coles' in name:
                stores.add('Coles')
            elif 'woolworths' in name or 'woolies' in name:
                stores.add('Woolworths')
            elif 'aldi' in name:
                stores.add('Aldi')
            elif 'iga' in name:
                stores.add('IGA')
            elif 'chemist warehouse' in name:
                stores.add('Chemist Warehouse')
        
        return sorted(list(stores))
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return []
