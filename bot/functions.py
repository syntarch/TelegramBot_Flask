import requests
from config import Config


URL = f"https://api.telegram.org/bot{Config.TOKEN}/"


def send_message(chat_id, text="blabla"):
    url = URL + "sendMessage"
    answer = {"chat_id": chat_id, "text": text}
    r = requests.post(url, json=answer)
    return r.json()
