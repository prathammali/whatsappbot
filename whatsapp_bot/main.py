import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
DEFAULT_TO = os.getenv("DEFAULT_TO")

def send_whatsapp_message(to=DEFAULT_TO, template="hello_world", language="en_US"):
    url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "template",
        "template": {
            "name": template,
            "language": { "code": language }
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
