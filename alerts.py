import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "sender@gmail.com"
SENDER_PASSWORD = "app_password"  
RECIPIENT_EMAIL = "recipient@gmail.com"

def send_alert(message):
    print(f"[ALERT] {message}")  

    try:
        
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = "Data Breach Alert"

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()

        print("[EMAIL] Alert email sent successfully.")
    except Exception as e:
        print(f"[EMAIL] Failed to send alert email: {e}")
