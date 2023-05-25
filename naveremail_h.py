import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 보내는 사람 계정 설정
me = 'lt75355@naver.com'
password = '---'

# 받는 사람 계정 설정
you = 'lt75355@naver.com'

# 메일 제목, 본문 내용 설정
subject = '테스트 메일'
content = '안녕하세요, 이것은 테스트 메일입니다.'

# 메일 생성
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = me
msg['To'] = you
text = MIMEText(content)
msg.attach(text)

# SMTP 서버 설정
smtp_server = 'smtp.naver.com'
smtp_port = 587
smtp_tls = True

# SMTP 서버 연결
s = smtplib.SMTP(smtp_server, smtp_port)
s.starttls()
s.login(me, password)

# 메일 발송
s.sendmail(me, you, msg.as_string())

# SMTP 서버 연결 종료
s.quit()
