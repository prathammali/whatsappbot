from django.http import JsonResponse
from .main import send_whatsapp_message

def send_message(request):
    result = send_whatsapp_message()
    return JsonResponse(result)
