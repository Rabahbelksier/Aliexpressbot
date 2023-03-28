'''import telebot

apiKey = "6055626308:AAGzUX-NVvmrzDNRzF6g8Z-dumwf6S-iiXg"
bot = telebot.TeleBot(apiKey)

def send_messageG(group_id, message):
    bot.send_message(group_id, message)
send_messageG(-1001589209127, "Mensagem enviada a partir de um bot no Telegram")'''
'''{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "104839609223244",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "15550294026",
              "phone_number_id": "102861919422010"
            },
            "statuses": [
              {
                "id": "wamid.HBgMNTU1NDk2OTU1MjgyFQIAERgSQzkyNzRENjA3Q0ZEMkQ3NjQyAA==",
                "status": "read",
                "timestamp": "1678050225",
                "recipient_id": "555496955282"
              }
            ]
          },
          "field": "messages"
        }
      ]
    }
  ]
}
{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "104839609223244",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "15550294026",
              "phone_number_id": "102861919422010"
            },
            "contacts": [
              {
                "profile": {
                  "name": "MS DIEGO"
                },
                "wa_id": "555496955282"
              }
            ],
            "messages": [
              {
                "from": "555496955282",
                "id": "wamid.HBgMNTU1NDk2OTU1MjgyFQIAEhgSRUVCN0M0Njg3Q0RGODYyOEIzAA==",
                "timestamp": "1678050234",'''''''
                "text": {
                  "body": "Hello Word"
                },
                "type": "text"
              }
            ]
          },
          "field": "messages"
        }
      ]
    }
  ]
}'''
import requests
import json
from flask import Flask, request


app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = {
        "VERIFY_TOKEN": "APP",
        "WHATSAPP_TOKEN": "EAAHCfwtIFoEBAKz8J6emizmNFHiFxDzXxjbdedZAESZCDaBaipgcCfuAX52dSvE0VEfYb6ZBGKAMOv2t62BLShNTTWKR6R9a6d4S5jdgwa6pEW6Eqq7sgZArexHfLYAZBmRlgQEVGn3kGJ4ZB2uPYkUOEk2RszW6WBhUOv1hgQRPkpxjZBNBGbdN6aeZBd0ozKiBJ6Ji2RMUqb6BF5BIkoC0ENDXYxqpgKgZD"
    }
    print(data)
    return True

webhook()
if __name__ == '__main__':
    app.run(debug=True)
