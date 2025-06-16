import requests
import os

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

        # Create a folder for images if it doesn’t exist
        folder_name = query.replace(" ", "_")
        os.makedirs(folder_name, exist_ok=True)

        for i, result in enumerate(data['results'], 1):
            image_url = result['urls']['regular']
            image_data = requests.get(image_url).content

            file_path = os.path.join(folder_name, f"{query}_{i}.jpg")
            with open(file_path, 'wb') as f:
                f.write(image_data)
            
            print(f"Downloaded: {file_path}")
    else:
        print("Error:", response.status_code, response.text)