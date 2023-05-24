import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 보내는 이메일 주소, 비밀번호, 받는 이메일 주소 설정
email = "보내는_이메일_주소"
password = "보내는_이메일_비밀번호"
recipient = "받는_이메일_주소"

# 이메일 메시지 작성
message = MIMEMultipart()
message["Subject"] = "네이버 이메일 보내기 테스트"
message["From"] = email
message["To"] = recipient

text = MIMEText("안녕하세요, 이메일 보내기 테스트입니다.")
message.attach(text)

# 첨부 파일 추가
filename = "test.txt"
with open(filename, "rb") as f:
    attachment = MIMEApplication(f.read(), _subtype="txt")
    attachment.add_header("Content-Disposition", "attachment", filename=filename)
    message.attach(attachment)

# SMTP 서버 접속 및 이메일 보내기
smtp = smtplib.SMTP("smtp.naver.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.login(email, password)
smtp.sendmail(email, recipient, message.as_string())
smtp.quit()
