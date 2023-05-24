import smtplib
from email.mime.text import MIMEText

smtp_server = 'smtp.gmail.com'  # SMTP 서버 주소
smtp_port = 587  # SMTP 포트 번호
smtp_user = 'your_email@gmail.com'  # 보내는 메일 계정
smtp_password = 'your_email_password'  # 보내는 메일 계정의 비밀번호

sender = 'your_email@gmail.com'  # 보내는 사람
recipient = 'recipient_email@example.com'  # 받는 사람
subject = 'Test Email'  # 메일 제목
body = 'Hello, this is a test email.'  # 메일 본문

# MIMEText 객체 생성
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient

# SMTP 서버 연결
s = smtplib.SMTP(smtp_server, smtp_port)
s.starttls()
s.login(smtp_user, smtp_password)

# 메일 전송
s.sendmail(sender, [recipient], msg.as_string())
s.quit()
