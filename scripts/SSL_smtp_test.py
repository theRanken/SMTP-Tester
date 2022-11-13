#!/usr/bin/python

import smtplib, ssl

####-----------------------------------------------------####
####--- SETTINGS DICTIONARY FOR MAIL SERVER VARIABLES----####
####-----------------------------------------------------####
smtp_server_settings = {
	'host':'mail.example.com',
	'port':465,
	'username':'site@example.com',
	'password':'',
}

####-----------------------------------------------------####
####------------ SENDER AND RECIEVER DETAILS ------------####
####-----------------------------------------------------####
sender = smtp_server_settings['username']   #The Sender of the Email

receivers = [                               # A list of recipients of the email
	'receiver1@gmail.com',                 # Just add yours to the list
]
message = f'A Test Email from {sender}'     # The Message The recipeints get in their mailbox

####-----------------------------------------------------####
####------------   SEND TEST MAIL FUNCTION   ------------####
####-----------------------------------------------------####
def send_mail():
    global smtp_server_settings # Get the global smtp settings 
    settings = smtp_server_settings # localize global smtp settings
    
    #### Context processor to simplify things which basically sets up a secure SSL Layer
    with smtplib.SMTP_SSL(settings['host'], settings['port'], context=ssl.create_default_context()) as server:
        #Error Handling 
        try:
            server.login(settings['username'], settings['password'])
            server.sendmail(sender, receivers, message)
            print('mail successfully sent')
        except Exception as e:
            print(f'Error: {e}')
 
#Runs the 'send_mail' function when this script is run in the terminal
if __name__ == '__main__':
    send_mail()