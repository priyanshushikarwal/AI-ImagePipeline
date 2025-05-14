import smtplib
from email.message import EmailMessage

sender_email = '#####@gmail.com'
receiver_email = '#####@gmail.com'
app_password = ''
subject = 'Your Enhanced Ford Image'
body = 'Here is your AI-enhanced Ford Endeavour image.'


image_path = r'C:\Users\Pri yanshu\Desktop\QuitIt\ford_scenic.jpg'  # 

msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email
msg.set_content(body)


with open(image_path, 'rb') as img:
    img_data = img.read()
    msg.add_attachment(img_data, maintype='image', subtype='jpeg', filename='FordEnhanced.jpg')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, app_password)
    smtp.send_message(msg)

print("✅ Email sent successfully!")
