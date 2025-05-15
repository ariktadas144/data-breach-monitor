import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "sender@gmail.com"
SENDER_PASSWORD = "app_password"  
RECIPIENT_EMAIL = "recipient@gmail.com"

GRAPH_FILE = "failed_attempts_plot.png"

def send_alert(message):
    print(f"[ALERT] {message}")

    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = "Data Breach Alert"

        msg.attach(MIMEText(message, 'plain'))
        
        try:
            with open(GRAPH_FILE, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={GRAPH_FILE}")
                msg.attach(part)
        except FileNotFoundError:
            print(f"[EMAIL] Warning: File '{GRAPH_FILE}' not found. Email will be sent without attachment.")

        print("[EMAIL] Connecting to SMTP...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("[EMAIL] Alert email sent successfully.")

    except Exception as e:
        print(f"[EMAIL] Failed to send alert email: {e}")
