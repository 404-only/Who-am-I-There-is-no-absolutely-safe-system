import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from pyfiglet import Figlet


class EMAIL:

    def __init__(self):

        #smtp server
        self.mail_host = "xxxxx"
        #email sender
        self.mail_sender = "xxxxxxxx"
        #email license
        self.mail_license = "xxxxxxxx"
        #email receivers 
        self.mail_receivers = "xxxxxxxx"
        self.mm = MIMEMultipart('related')

    def text_email(self):

        subject_content = """xxxxxx"""
        self.mm["From"] = self.mail_sender
        self.mm["To"] = self.mail_receivers
        self.mm["Subject"] = Header(subject_content,'utf-8')
        self.text_email_do()

    def text_email_do(self):

        body_content = """xxxxxxxx"""
        message_text = MIMEText(body_content,"plain","utf-8")
        self.mm.attach(message_text)
        self.img_email_do()

    def img_email_do(self):

        image_data = open('8e4d940cc9ecbb9f'+'.jpg','rb')
        message_image = MIMEImage(image_data.read())
        image_data.close()
        self.mm.attach(message_image)
        self.send_email_do()

    def send_email_do(self):

        stp = smtplib.SMTP()
        stp.connect(self.mail_host, 25)
        stp.set_debuglevel(1)
        stp.login(self.mail_sender,self.mail_license)
        stp.sendmail(self.mail_sender, self.mail_receivers, self.mm.as_string())
        stp.quit()

        str_type = Figlet(font="Doom")
        print(str_type.renderText('Hello ! I\'ma hacker'))
