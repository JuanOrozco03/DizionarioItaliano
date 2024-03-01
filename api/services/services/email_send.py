from email.message import EmailMessage
import ssl
import smtplib

class Email:
    def __init__(self, email_receiver, word, definition, synonyms):
        self.email_sender = 'paroleitalianeeveryday@gmail.com'
        self.email_password = 'mcjk ttsf ahyh juxb'
        self.email_receiver = email_receiver
        self.em = EmailMessage()
        self.word = word
        self.definition = definition
        self.synonyms = synonyms
    
    def email_creation(self):
        subject = 'La tua parola ha arrivato'

        body = """
        La parola è: {}

        La definizione è: {}

        i sinonimi è: {}

        Grazie per aver preso parte al nostro progetto
        """.format(self.word, self.definition, self.synonyms)

        self.em['From'] = self.email_sender
        self.em['To'] = self.email_receiver
        self.em['subject'] = subject
        self.em.set_content(body)

    def send_email(self):
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, self.email_receiver, self.em.as_string())

# email_sender = 'juanorozco0310@gmail.com'
# email_password = 'pfjx gmck umaa lvoc'

# email_receiver = 'juanalejandro.orozco@utp.edu.co'

# subject = 'La tua parola ha arrivato'
# body = """

# """

# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['subject'] = subject
# em.set_content(body)


# context = ssl.create_default_context()

# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())