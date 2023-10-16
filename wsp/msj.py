from twilio.rest import Client

account_sid = 'AC952bdfe7f819969a976ce8b9195d8ea3'
auth_token = '146d49bab93021f3812d6c75072c634a'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Este mensaje fue enviado desde python por mi ajjajajaja',
  to='whatsapp:+56962267828'
)

print(message.sid)