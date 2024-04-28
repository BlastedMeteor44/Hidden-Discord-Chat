import requests
import base64

webhook_url = 'YOUR_WEBHOOK_URL_HERE'

username = "YOUR_USERNAME_HERE"

def send_discord_message(message):
    payload = {
        "content": message
    }
    r = requests.post(webhook_url, json=payload)
    
    if r.status_code == 204:
        print("done")
    else:
        print("Error: ", r.status_code)

def encode_7_times(text):
    encoded_text = text
    for _ in range(7):
        encoded_text = base64.b64encode(encoded_text.encode()).decode()
    return encoded_text

run = True

while run:
    inputed_message = input("Enter message: ")
    encoded_message = encode_7_times(f"Message from {username}: {inputed_message}")
    send_discord_message(encoded_message)