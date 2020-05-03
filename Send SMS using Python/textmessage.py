# Author: Akrash Sharma
# For this code to run you will have to create an account on Twilio

from twilio.rest import Client
import config  # Create a file called config.py which contains your acc_sid and auth_token stored as strings

client = Client(config.acc_sid, config.auth_token)
receiver_phone_num = ""  # Type the receiver's phone number in the empty string
twilio_phone_num = ""  # Type your twilio phone number
text = client.messages.create(
    to=receiver_phone_num,
    from_=twilio_phone_num,
    body="My message from Python"
)
print(text.sid)
