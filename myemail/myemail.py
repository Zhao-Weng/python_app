
import smtplib

def send_email():
    sender = input("Please input the Sender email: (gmail only) \n")
    recipients = input("Please input the Recipients' email, seperated by comma:\n")

    recipients = recipients.replace(" ","").split(",")



    subject = ("Subject: "+ input("Input your subject: \n"))

    message = subject + "\n\n" + \
    (input("Input your main body: (new line is '\\n'): (email will be sent once you pressed enter) \n"))
                              

    repeat = 1
    getout = 0
    while(repeat != 5 and getout == 0):
        try:
            server = smtplib.SMTP("smtp.gmail.com:587")
            server.ehlo() #let the client and server know about each other’s
            #privileged status. not necessary 
            server.starttls()#for security in email. tls protocol for email security.

            server.login("w2280518650@gmail.com", "jkymylmnwulugqik")
            server.sendmail(sender,recipients,message)
            print("Mail sent succesful")
            getout = 1
        except:
             repeat += 1
             
    print("mail sent failed.")


send_email()
while(input("want to send another email?(type 'yes' if you want)") == 'yes'):
    send_email()
    



####bug_log
#1 I first use the same name email.py which is in conflict with the file
#in python lib.
#in addition, have to enable two step verification to set up a app password for
#login

#strip() strips away whitespaces, but space is not counted as whitespace,
#only tab or multiple space is counted as whitespace.


#skills: use try except, let you specify what to use once exception happens, for users,
# except content makes much more sense.


          
    
