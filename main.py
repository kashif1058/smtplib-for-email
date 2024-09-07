BACKGROUND_COLOR = "#B1DDC6"

import smtplib
from email.mime.text import MIMEText

# Email settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'your_email@gmail.com'
password = 'your_password'
from_email = 'your_email@gmail.com'
to_email = 'recipient_email@example.com'
subject = 'Test Email'
body = 'This is a test email sent from Python!'

# Create the email
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = from_email
msg['To'] = to_email

# Send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(username, password)
        server.sendmail(from_email, to_email, msg.as_string())
        print('Email sent successfully!')
except Exception as e:
    print(f'Failed to send email: {e}')