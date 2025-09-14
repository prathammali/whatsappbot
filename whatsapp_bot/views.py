from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .main import send_whatsapp_message
import os

VERIFY_TOKEN = "pm"

@csrf_exempt
def webhook(request):
    if request.method == "GET":
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return HttpResponse(challenge)
        return HttpResponse("Verification failed", status=403)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print("Incoming webhook:", json.dumps(data, indent=2))

            messages = data['entry'][0]['changes'][0]['value'].get('messages')
            if messages:
                from_number = messages[0]['from']
                user_text = messages[0]['text']['body'].strip().lower()

                if user_text == "hi":
                    reply = "Hiii"
                elif user_text == "hello":
                    reply = "How can I help?"
                elif user_text == "find tender":
                    reply = "Yes Sure, please Tell me in which location?"
                else:
                    reply = "I can only reply to 'Hi' or 'Hello'."

                send_whatsapp_message(to=from_number, message=reply)
        except Exception as e:
            print("Error processing webhook:", e)

        return HttpResponse(status=200)
