# FAQ Bot - Snitch Knowledge Base Crawler

A Python-based FAQ data extraction tool that fetches structured FAQ data from Snitch's API and organizes it for use in RAG (Retrieval-Augmented Generation) systems.

## 🚀 Features

- **API-based data extraction** - Uses Snitch's official FAQ API for clean, structured data
- **Multiple output formats** - Generates both human-readable and machine-readable formats
- **Category organization** - Automatically organizes FAQs by categories
- **RAG-ready format** - Structured JSON output perfect for vector databases
- **Rich metadata** - Includes slots, patterns, and timestamps for each FAQ

## 📁 Project Structure

```
faqBot/
├── Crawl_kb.py              # Main crawler script
├── README.md                # This file
├── .gitignore              # Git ignore rules
├── faq_all.txt             # All FAQs in readable format
├── faq_exchange_returns.txt # Exchange/Returns category
├── faq_refunds.txt         # Refunds category
├── faq_offline_store.txt   # Offline Store category
├── faq_payments.txt        # Payments category
├── faq_sizing.txt          # Sizing category
└── venv/                   # Virtual environment
```

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-github-repo-url>
   cd faqBot
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install requests beautifulsoup4
   ```

4. **Run the crawler**
   ```bash
   python Crawl_kb.py
   ```

## 📊 Output Files

The crawler generates three types of output files:

### 1. Category-specific Text Files
- `faq_all.txt` - All FAQs in markdown format
- `faq_exchange_returns.txt` - Exchange/Returns specific FAQs
- `faq_refunds.txt` - Refunds specific FAQs
- `faq_offline_store.txt` - Offline Store specific FAQs
- `faq_payments.txt` - Payments specific FAQs
- `faq_sizing.txt` - Sizing specific FAQs

### 2. Complete API Response
- `snitch_faq_complete_[timestamp].json` - Full API response with all metadata

### 3. Structured Format (Perfect for RAG)
- `structured_faqs_[timestamp].json` - Clean, processed format with:
  - Category classification
  - Question-answer pairs
  - Related links (slots)
  - Pattern information
  - Extraction timestamps

## 🔧 Usage

### Basic Usage
```python
python Crawl_kb.py
```

### Programmatic Usage
```python
from Crawl_kb import fetch_faq_data, save_structured_faqs

# Fetch FAQ data
faq_data = fetch_faq_data()

# Save in structured format
save_structured_faqs(faq_data)
```

## 📈 Data Structure

Each FAQ item in the structured format contains:

```json
{
  "category": "All",
  "question": "WHERE IS MY ORDER?",
  "answer": "We ship 99% of orders within 24 hours...",
  "slots": ["MY_ORDERS"],
  "has_patterns": true,
  "source": "snitch_api",
  "extracted_at": "2025-09-06T00:29:18.055270"
}
```

## 🎯 Use Cases

- **RAG Systems** - Use structured JSON for vector database ingestion
- **Customer Support** - Quick reference for support agents
- **Documentation** - Automated FAQ documentation
- **Chatbots** - Training data for conversational AI
- **Knowledge Management** - Organized knowledge base

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 API Information

- **Endpoint**: `https://zik7xvmn77.ap-south-1.awsapprunner.com/v1/public/faq`
- **Method**: GET
- **Response**: JSON with structured FAQ data
- **Rate Limiting**: No known limits (be respectful)

## 🐛 Troubleshooting

### Common Issues

1. **Connection Error**
   - Check internet connection
   - Verify API endpoint is accessible

2. **Import Error**
   - Ensure virtual environment is activated
   - Install required packages: `pip install requests beautifulsoup4`

3. **Permission Error**
   - Check file write permissions in the project directory

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👥 Team

- **Atish** - Project Creator
- **Your Friends** - Collaborators

## 🔄 Updates

- **v1.0** - Initial release with API-based FAQ extraction
- **v1.1** - Added structured JSON output for RAG systems
- **v1.2** - Improved error handling and documentation

---

**Happy Crawling! 🕷️**
