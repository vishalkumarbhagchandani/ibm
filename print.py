

# mess= 'hello world'

# print(mess)




# from twilio.rest import TwilioRestClient

# account_sid = 'AC07e3ac874a7d06b70450f9ffebd897f6' # Found on Twilio Console Dashboard
# auth_token = 'ca40687074320706764ebed5095eb94c' # Found on Twilio Console Dashboard

# myPhone = '8121951698' # Phone number you used to verify your Twilio account
# TwilioNumber = '+19852384498' # Phone number given to you by Twilio
# destCellPhone = '9618158671'

# client = Client(account_sid, auth_token)

# # client.messages.create(
# #   to=myPhone,
# #   from_=TwilioNumber,
# #   body='I sent a text message from Python! ' + u'\U0001f680')

# myMessage = twilioClient.messages.create(body = "whatever", from_=TwilioNumber, to=destCellPhone)
# Download the helper library from https://www.twilio.com/docs/python/install
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC07e3ac874a7d06b70450f9ffebd897f6'
auth_token = 'ca40687074320706764ebed5095eb94c'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='hello bro',
         from_='+19852384498',
         to='+918121951698'
     )

print(message.sid)