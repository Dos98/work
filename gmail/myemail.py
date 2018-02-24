import smtplib
import csv
#r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'ayushdosaj2313@gmail.com'
PASSWORD = 'klfkgyskgfeiuisl'

def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r') as contacts_file:
        reader = csv.reader(contacts_file,delimiter=',')
        for a_contact in reader:
            for a in a_contact:
                pos = a.find('@')
                names.append(a[:pos])
                emails.append(a)
    return names, emails

def read_template(filename):
    with open(filename, 'r') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('mycontacts.csv') # read contacts
    message_template = read_template('message.txt')
    #message_template = Template("Hi!")
    #names, emails = ['ayush'], ['ayushdosaj2313@gmail.com']
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message
        message = message_template.substitute(PERSON_NAME=name.title())
        print(message)
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is TEST"
        msg.attach(MIMEText(message, 'plain'))

        s.sendmail(MY_ADDRESS, emails, msg.as_string())
        del msg
    s.quit()

if __name__ == '__main__':
    main()

