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
    mail_content = mail_context.content

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
    session.login(config.mail_from, config.password)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(config.mail_from, mail_context.to, text)
    session.quit()
