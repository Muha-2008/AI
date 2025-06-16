import requests

def search_unsplash_images(query):
    access_key = "wUJejRO7znWvme0ASk_AT0nVJF2IT10hYLXVFAZ6F7U"
    url = "https://api.unsplash.com/search/photos"
    
    params = {
        "query": query,
        "per_page": 12,
        "client_id": access_key
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        for i, result in enumerate(data['results'], 1):
            print(f"{i}. {result['urls']['regular']}")
    else:
        print("Error:", response.status_code, response.text)

# Example
search_unsplash_images("cats")