import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration (Replace these placeholders with your actual details)
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@gmail.com"
password = "your_app_password"  # Do NOT use your regular Gmail password here

# Create the email content
subject = "Test Email"
body = "Hello this is a test email from Python!"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Connect to the server and send the email
import ssl

try:

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("://gmail.com", 465, context=context) as server:


        server.login(sender_email, password) # Log in to your email account
        server.send_message(message) # Send the email
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")