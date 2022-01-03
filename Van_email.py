# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:43:51 2021

@author: micha
"""

#Mum's van email

#Plan

#1. Set up the template
#2. Send the email to a desired person
#3. Attach required documents
#4. Figure out how to let mum use it


from docx import Document
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

myName = 'Eve Stanway' #Name of person sending the email
myEmail = "michaelsstanway@gmail.com" #Email of the person sending the email  
password = "urmumgay" #Password to the email being used to send
smtpServer = "smtp.gmail.com" #This will need to be changed depending on the email site used
port = 587


def obtainInformation(docFileName): #Function to read and save the clients
    document = Document(docFileName) #Opens the required document
    finalText = [] #Empty list to store data
    for line in document.paragraphs:
        line = line.text
        stuff = line.split(': ')
        try:
            finalText.append(stuff[1]) #Saves the file to the list
        except:
            continue
    return finalText

def sendEmail(x, y): #Function to send emails
    context = ssl.create_default_context() #Not too sure what this means but its needed
    try: #Sends the message to desired place after accessing gmail server
        server = smtplib.SMTP(smtpServer, port)
        server.starttls(context = context)
        server.login(myEmail, password)
        server.sendmail(myEmail, y, x)
    except Exception as e: #In case the message cannot send for whatever reason
        print("the email could not be sent.")
    finally:
        server.quit() #Exits the server


information_values = obtainInformation('VanClients.docx')
first_name = information_values[0].split()
information = {'Name': information_values[0], 'First Name':first_name[0], 'ChosenTime': information_values[1], 'EarliestTime': information_values[2], 'DateOfCollection': information_values[3], 'Email': information_values[4], 'PeriodOfHire': information_values[5], 'Pets': information_values[6]}

subject = 'Anneliese Hire - ' + information['PeriodOfHire'] #Subject of the email
topic = "Subject: " + subject #Subject in the required useable format

if information['Pets'] == 'No':
    if information['EarliestTime'] == 'No':
        template = """
Hi {recipient},        
        

I hope all is well. Thank you very much for choosing Anneliese for your holiday.  

I am just preparing the paperwork and insurance.

I will email you a link for the driver hire form in case you haven't received it yet.

The insurance also requires two forms of ID as proof of address (e.g. bank statement, utility bills, council tax, etc and a photo of the front and back of your driving licence).  The address on the proofs should be the same as that on the driver's licence.  I need ID, etc for all named drivers.  I have attached the information we are sent from the insurers saying what ID is suitable.

If it is easier for you, you can send me screenshots via WhatsApp or send them by email.

My email address is evestanway@gmail.com and my phone number is 07977420861.

Regarding the hire, I notice you have a pick up time of {chosen_time} on {date_of_collection}.  Please let me know if there is any issue with that time.

If you have any questions or queries just let me know.  Handover takes about 45 minutes as we will need to complete the paperwork and I will give you a complete run through of all the equipment.  I will need you to bring your driving licences when you pick Anneliese up.

Here is a link to a van tour we recorded last year.  Some changes are that Anneliese now has windows in the rear doors, and my hair is back to being blonde! 

This tour is viewable here - https://www.youtube.com/watch?v=yxNcQr5KFOQ&t=19s

If you are arriving by car, my street is very quiet and there is no problem parking directly outside my house during your holiday.

I look forward to hearing from you.


All the best,

Eve and Anneliese
07977420861
        """

        message = template.format(recipient=information['First Name'], chosen_time=information['ChosenTime'], date_of_collection=information['DateOfCollection'])
    else:
        template = """
Hi {recipient},
        
        
I hope all is well. Thank you very much for choosing Anneliese for your holiday.  

I am just preparing the paperwork and insurance.

I will email you a link for the driver hire form in case you haven't received it yet.

The insurance also requires two forms of ID as proof of address (e.g. bank statement, utility bills, council tax, etc and a photo of the front and back of your driving licence).  The address on the proofs should be the same as that on the driver's licence.  I need ID, etc for all named drivers.  I have attached the information we are sent from the insurers saying what ID is suitable.

If it is easier for you, you can send me screenshots via WhatsApp or send them by email.

My email address is evestanway@gmail.com and my phone number is 07977420861.

Regarding the hire, I notice you have a pick up time of {chosen_time}.  I just wanted to let you know that Anneliese will be available from {earliest_time} on {date_of_collection}, if you would like to start your holiday a little earlier at no extra cost.   Please let me know if you want to start earlier.

If you have any questions or queries just let me know.  Handover takes about 45 minutes as we will need to complete the paperwork and I will give you a complete run through of all the equipment.  I will need you to bring your driving licences when you pick Anneliese up.

Here is a link to a van tour we recorded last year.  Some changes are that Anneliese now has windows in the rear doors, and my hair is back to being blonde! 

This tour is viewable here - https://www.youtube.com/watch?v=yxNcQr5KFOQ&t=19s

If you are arriving by car, my street is very quiet and there is no problem parking directly outside my house during your holiday.

I look forward to hearing from you.


All the best,

Eve and Anneliese
07977420861
        """
        
        message = template.format(recipient=information['First Name'], chosen_time=information['ChosenTime'], earliest_time=information['EarliestTime'], date_of_collection=information['DateOfCollection'])
else:
    if information['EarliestTime'] == 'No':
        template = """
Hi {recipient},


I hope all is well. Thank you very much for choosing Anneliese for your holiday.  

I am just preparing the paperwork and insurance.

I will email you a link for the driver hire form in case you haven't received it yet.

The insurance also requires two forms of ID as proof of address (e.g. bank statement, utility bills, council tax, etc and a photo of the front and back of your driving licence).  The address on the proofs should be the same as that on the driver's licence.  I need ID, etc for all named drivers.  I have attached the information we are sent from the insurers saying what ID is suitable.

If it is easier for you, you can send me screenshots via WhatsApp or send them by email.

My email address is evestanway@gmail.com and my phone number is 07977420861.

Regarding the hire, I notice you have a pick up time of {chosen_time} on {date_of_collection}.  Please let me know if there is any issue with that time.

If you have any questions or queries just let me know.  Handover takes about 45 minutes as we will need to complete the paperwork and I will give you a complete run through of all the equipment.  I will need you to bring your driving licences when you pick Anneliese up.

Something about pets.

Here is a link to a van tour we recorded last year.  Some changes are that Anneliese now has windows in the rear doors, and my hair is back to being blonde! 

This tour is viewable here - https://www.youtube.com/watch?v=yxNcQr5KFOQ&t=19s

If you are arriving by car, my street is very quiet and there is no problem parking directly outside my house during your holiday.

I look forward to hearing from you.


All the best,

Eve and Anneliese
07977420861
        """
        
        message = template.format(recipient=information['First Name'], chosen_time=information['ChosenTime'], date_of_collection=information['DateOfCollection'])
    else:
        template = """
Hi {recipient},


I hope all is well. Thank you very much for choosing Anneliese for your holiday.  

I am just preparing the paperwork and insurance.

I will email you a link for the driver hire form in case you haven't received it yet.

The insurance also requires two forms of ID as proof of address (e.g. bank statement, utility bills, council tax, etc and a photo of the front and back of your driving licence).  The address on the proofs should be the same as that on the driver's licence.  I need ID, etc for all named drivers.  I have attached the information we are sent from the insurers saying what ID is suitable.

If it is easier for you, you can send me screenshots via WhatsApp or send them by email.

My email address is evestanway@gmail.com and my phone number is 07977420861.

Regarding the hire, I notice you have a pick up time of {chosen_time}.  I just wanted to let you know that Anneliese will be available from {earliest_time} on {date_of_collection}, if you would like to start your holiday a little earlier at no extra cost.   Please let me know if you want to start earlier.

If you have any questions or queries just let me know.  Handover takes about 45 minutes as we will need to complete the paperwork and I will give you a complete run through of all the equipment.  I will need you to bring your driving licences when you pick Anneliese up.

Something about pets.

Here is a link to a van tour we recorded last year.  Some changes are that Anneliese now has windows in the rear doors, and my hair is back to being blonde! 

This tour is viewable here - https://www.youtube.com/watch?v=yxNcQr5KFOQ&t=19s

If you are arriving by car, my street is very quiet and there is no problem parking directly outside my house during your holiday.

I look forward to hearing from you.


All the best,

Eve and Anneliese
07977420861
        """
        
        message = template.format(recipient=information['First Name'], chosen_time=information['ChosenTime'], earliest_time=information['EarliestTime'], date_of_collection=information['DateOfCollection'])


msg = MIMEMultipart()
msg['From'] = myName
msg['To'] = information['Name'] + ' ' + information['Email']
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))
 

pdfname = 'Driver_referencing.pdf'

# open the file in bynary
binary_pdf = open(pdfname, 'rb')

payload = MIMEBase('application', 'octate-stream', Name=pdfname)
payload.set_payload((binary_pdf).read())

# enconding the binary into base64
encoders.encode_base64(payload)

# add header with pdf name
payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
msg.attach(payload)

text = msg.as_string()

sendEmail(text, information['Email']) #Sends the final message

























