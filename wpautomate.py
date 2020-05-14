import os

from twilio.rest import Client 
 
account_sid = 'ACbfd72xxxxxxxxxxxx668788182fa88' 
auth_token = 'ceb72e2bffxxxxxxxxxxxd2676b65f' 
client = Client(account_sid, auth_token) 
 
from_whatsapp_number = 'whatsapp:+1415xxxx8886'
to_whatsapp_number ='whatsapp:+9176xxxx37313'

message = client.messages.create( 
                              from_=from_whatsapp_number,  
                              body='Hey! Hello World',      
                              to=to_whatsapp_number 
                          ) 
 
print(message.sid)
