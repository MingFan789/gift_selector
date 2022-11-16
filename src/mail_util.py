import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pydantic import BaseModel


class MailContext(BaseModel):
    to: str
    content: str
    subject: str


class MailConfig(BaseModel):
    mail_from: str
    password: str
    host: str
    port: int


def send_mail(mail_context: MailContext, config: MailConfig):
    # mail_content = """Hello,
    # This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
    # Thank You
    # """
    mail_content = mail_context.content

    # The mail addresses and password
    sender_address = "mingfan789@gmail.com"

    # Remember to use application password
    # Not your own password
    sender_pass = "dheacdzydehpgnzs"
    receiver_address = "mingfan789@gmail.com"

    # Setup the MIME
    message = MIMEMultipart()
    message["From"] = config.mail_from
    message["To"] = mail_context.to
    message["Subject"] = mail_context.subject
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, "plain"))

    # message[
    #     "Subject"
    # ] = "A test mail sent by Python. It has an attachment."  # The subject line

    # Create SMTP session for sending the mail
    # session = smtplib.SMTP("smtp.gmail.com", 587)  # use gmail with port
    session = smtplib.SMTP(config.host, config.port)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print("Mail Sent")
