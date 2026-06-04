import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ─── SETTINGS ────────────────────────────────────────────────
URL = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
TARGET_PRICE = float(os.getenv("TARGET_PRICE", 60))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
CHECK_INTERVAL_MINUTES = int(os.getenv("CHECK_INTERVAL_MINUTES", 60))
# ─────────────────────────────────────────────────────────────


def get_price(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    price_tag = soup.find("p", class_="price_color")
    if not price_tag:
        return None

    price_text = price_tag.get_text().strip().replace("£", "").replace("Â", "")
    return float(price_text)


def send_email(current_price):
    message = MIMEText(
        f"🚨 Price Alert!\n\n"
        f"The product dropped to {current_price}€\n\n"
        f"Check it out: {URL}"
    )
    message["Subject"] = f"Price dropped to {current_price}€!"
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.send_message(message)
    print("✅ Email sent!")


def monitor():
    print(f"🔍 Monitoring: {URL}")
    while True:
        try:
            price = get_price(URL)
            if price is None:
                print("Could not retrieve the price.")
            elif price <= TARGET_PRICE:
                print(f"Target price reached: {price}€ — sending email...")
                send_email(price)
            else:
                print(f"Current price: {price}€ (target: {TARGET_PRICE}€)")
        except Exception as e:
            print(f"Error: {e}")

        print(f"⏳ Next check in {CHECK_INTERVAL_MINUTES} minutes...\n")
        time.sleep(CHECK_INTERVAL_MINUTES * 60)


if __name__ == "__main__":
    monitor()