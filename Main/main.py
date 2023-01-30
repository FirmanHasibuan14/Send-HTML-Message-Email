import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = input("Enter your email account: \n")
email_password = str(input("Enter your password (NOT YOUR EMAIL PASSWORD): \n"))
to_email = input("Enter the destination of your email account: \n")
subject = input("Send your subject: \n")

html_msg = html = '''
    <html>
        <body>
            <h1>HELLO BRO HOW ARE YOU</h1>
            <p>this is your friend bro</p>
            <p>don't forget to subs this channel </p>
            <a href = "https://www.youtube.com/@Jebreeetmediatv">THIS CHANNEL</a>
        </body>
    </html>
'''

email_msg = MIMEMultipart()
email_msg['From'] = sender_email
email_msg['To'] = to_email
email_msg['Subject'] = subject
email_msg.attach(MIMEText(html, "html"))
email_str = email_msg.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context) as smtp:
    try:
        smtp.login(sender_email,email_password)
        smtp.set_debuglevel(1)
        print("login success")
        smtp.sendmail(sender_email,to_email,email_str)
        print("Has successfully sent the email message to", to_email)
    except ValueError:
        print("Error")
    print("GOOD JOB")
    smtp.quit()


