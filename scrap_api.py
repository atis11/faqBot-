import requests
import json
from datetime import datetime
import os

# Define all endpoints for the brand
BRAND_APIS = {
    "About_Gift_Card" : "https://mxemjhp3rt.ap-south-1.awsapprunner.com/gift-card/terms-and-conditions",
    "Stores_location" : "https://u6dwgkszzd.ap-south-1.awsapprunner.com/v1/stores/public"
}

OUTPUT_DIR = "snitch_raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_and_save(name, url):
    """Fetch from API and save raw response"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        filename = os.path.join(
            OUTPUT_DIR, f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f" Saved {name} data to {filename}")
        return True

    except Exception as e:
        print(f" Failed to fetch {name} from {url}: {e}")
        return False


if __name__ == "__main__":
    print(" Fetching Snitch data from all APIs...")
    for name, url in BRAND_APIS.items():
        fetch_and_save(name, url)
    print("\ All available API responses saved in 'snitch_raw/' folder")
