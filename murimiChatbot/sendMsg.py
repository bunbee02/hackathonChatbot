from twilio.rest import Client

account_sid = 'AC37cebed5e43eb81f4c0345dda4da8a4d'
auth_token = '104ba6f60c47dcdbaf0291e03d7f219d'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Welcome to Murimi bot please select the region you are coming',
  to='whatsapp:+263713872372'
)

print(message.sid)