import requests
import json
from datetime import datetime

# Snitch FAQ API endpoint
FAQ_API_URL = "https://zik7xvmn77.ap-south-1.awsapprunner.com/v1/public/faq"

def fetch_faq_data():
    """Fetch FAQ data from Snitch API"""
    try:
        response = requests.get(FAQ_API_URL, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching FAQ data: {e}")
        return None

def save_faq_by_category(faq_data):
    """Save FAQ data organized by category"""
    if not faq_data or not faq_data.get('success'):
        print("No valid FAQ data received")
        return
    
    data = faq_data['data']
    categories = data['categories']
    faq_data_dict = data['faqData']
    
    print(f"Found {len(categories)} categories: {[cat['name'] for cat in categories]}")
    
    # Save each category to a separate file
    for category in categories:
        category_name = category['name']
        if category_name in faq_data_dict:
            faqs = faq_data_dict[category_name]
            
            # Create structured content
            content = f"# {category_name} FAQ\n\n"
            content += f"Total FAQs: {len(faqs)}\n"
            content += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            content += "=" * 50 + "\n\n"
            
            for i, faq in enumerate(faqs, 1):
                content += f"## FAQ {i}\n"
                content += f"**Question:** {faq['q']}\n\n"
                content += f"**Answer:** {faq['a']}\n\n"
                
                # Add metadata if available
                if 'slots' in faq and faq['slots']:
                    content += f"**Related Links:** {', '.join(faq['slots'])}\n\n"
                
                content += "-" * 30 + "\n\n"
            
            # Save to file
            filename = f"faq_{category_name.lower().replace('/', '_').replace(' ', '_')}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"Saved {len(faqs)} FAQs for category '{category_name}' to {filename}")

def save_all_faqs_json(faq_data):
    """Save complete FAQ data as JSON for programmatic use"""
    if not faq_data or not faq_data.get('success'):
        return
    
    filename = f"snitch_faq_complete_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(faq_data, f, indent=2, ensure_ascii=False)
    
    print(f"Saved complete FAQ data to {filename}")

def save_structured_faqs(faq_data):
    """Save FAQs in a structured format for easy processing"""
    if not faq_data or not faq_data.get('success'):
        return
    
    data = faq_data['data']
    faq_data_dict = data['faqData']
    
    # Create a structured format
    structured_faqs = []
    
    for category_name, faqs in faq_data_dict.items():
        for faq in faqs:
            structured_faq = {
                "category": category_name,
                "question": faq['q'],
                "answer": faq['a'],
                "slots": faq.get('slots', []),
                "has_patterns": faq.get('processedAnswer', {}).get('hasPatterns', False),
                "source": "snitch_api",
                "extracted_at": datetime.now().isoformat()
            }
            structured_faqs.append(structured_faq)
    
    # Save structured data
    filename = f"structured_faqs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(structured_faqs, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(structured_faqs)} structured FAQs to {filename}")

if __name__ == "__main__":
    print("Fetching FAQ data from Snitch API...")
    faq_data = fetch_faq_data()
    
    if faq_data:
        print("Successfully fetched FAQ data!")
        
        # Save data in different formats
        save_faq_by_category(faq_data)
        save_all_faqs_json(faq_data)
        save_structured_faqs(faq_data)
        
        print("\nAll FAQ data has been saved successfully!")
    else:
        print("Failed to fetch FAQ data")
