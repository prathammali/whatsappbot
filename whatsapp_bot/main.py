import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
API_VERSION = os.getenv("WHATSAPP_API_VERSION", "v22.0")

def send_whatsapp_message(to, message):
    url = f"https://graph.facebook.com/{API_VERSION}/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print(f"Message sent to {to}: {message}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error sending WhatsApp message:", e)
        return {"error": str(e)}
