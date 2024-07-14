from mailjet_rest import Client
import os

API_KEY = os.environ.get('MAILJET_API_KEY')
API_SECRET = os.environ.get('MAILJET_API_SECRET')

mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')

def send_email(to, subject, text, html):
    data = {
      'Messages': [
        {
          "From": {
            "Email": "app@diarme.online",
            "Name": "You Can Write"
          },
          "To": [
            {
              "Email": to,
              "Name": "You"
            }
          ],
          "Subject": subject,
          "TextPart": text,
          "HTMLPart": html
        }
      ]
    }
    result = mailjet.send.create(data=data)
    is_sent = result.status_code == 200
    return is_sent