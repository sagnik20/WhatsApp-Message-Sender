import os

from twilio.rest import Client 
 
account_sid = 'ACbfd72c46135436f72c5668788182fa88' 
auth_token = 'ceb72e2bffb403145ba1a01d2676b65f' 
client = Client(account_sid, auth_token) 
 
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number ='whatsapp:+917665337313'

message = client.messages.create( 
                              from_=from_whatsapp_number,  
                              body='Hey! Hello World',      
                              to=to_whatsapp_number 
                          ) 
 
print(message.sid)