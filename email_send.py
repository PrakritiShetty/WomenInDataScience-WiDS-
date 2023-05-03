import pandas as pd
import smtplib

your_name = "Prakriti Shetty"
your_email = "prakritishetty02@gmail.com"
your_password = "quhtopoyvssvnrzm"

server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.ehlo()
server.login(your_email, your_password)

email_list = pd.read_excel('final.xlsx')

all_names = email_list['Name']
all_emails = email_list['Email Address']
all_subjects = email_list['Subject']
all_messages = email_list['Message']


for idx in range(len(all_emails)):

    name = all_names[idx]
    email = all_emails[idx]
    subject = all_subjects[idx]
    message = all_messages[idx]

    full_email = ("From: {0} <{1}>\n"
                  "To: {2} <{3}>\n"
                  "Subject: {4}\n\n"
                  "{5}").format(your_name, your_email, name, email, subject, message)
    
    try:
        server.sendmail(your_email, [email], full_email)
        print('Email to {} successfully sent!\n\n'.format(email))
    except Exception as e:
        print('Email to {} couldn\'t be sent because {}\n\n'.format(email, str(e)))

server.close()

