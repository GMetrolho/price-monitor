# 💰 Price Monitor

A Python script that automatically monitors product prices on any website and sends an email alert when the price drops below your target.

## ✨ Features

- 🔍 **Automatic price monitoring** — checks the price at regular intervals
- 📧 **Email alerts** — sends an email when the target price is reached
- ⚙️ **Fully configurable** — set your own URL, target price and check interval
- 🔒 **Secure** — credentials stored in a `.env` file, never exposed in the code

## 🛠️ Tech Stack

- Python 3
- Requests
- BeautifulSoup4
- smtplib
- python-dotenv

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- A Gmail account with 2-Step Verification enabled
- A Gmail App Password ([how to generate one](https://support.google.com/accounts/answer/185833))

### Installation

1. Clone the repository
```bash
git clone https://github.com/GMetrolho/price-monitor.git
cd price-monitor
```

2. Install dependencies
```bash
pip install requests beautifulsoup4 python-dotenv
```

3. Create your `.env` file from the example
```bash
copy .env.example .env
```

4. Edit the `.env` file with your details
```
SENDER_EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_16_char_app_password
RECEIVER_EMAIL=your_email@gmail.com
TARGET_PRICE=60
CHECK_INTERVAL_MINUTES=60
```

5. Set the URL of the product you want to monitor in `monitor.py`
```python
URL = "https://www.example.com/product"
```

6. Run the script
```bash
python monitor.py
```

## 📌 How it works

1. The script fetches the product page at the defined interval
2. It extracts the price using BeautifulSoup
3. If the price is below the target → sends you an email alert
4. If not → waits and checks again

## 💼 Available for Freelance

Need a custom price monitor for your favourite store? Feel free to reach out!

📧 gmetrolho@gmail.com