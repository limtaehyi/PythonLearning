#-*- coding: utf-8 -*-
from email.header import decode_header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

import smtplib
import getpass
import imaplib
import email


# 사용자 정보


def showtext():
    # 네이버 메일 서버 접속
    imap = imaplib.IMAP4_SSL("imap.naver.com")
    imap.login(username, password)

    # 받은 편지함(Folder) 선택
    imap.select("INBOX")

    # 모든 메일 검색
    _, mails = imap.search(None, "ALL")

    # 메일 목록 출력
    for mail_id in mails[0].split():
        _, mail = imap.fetch(mail_id, "(RFC822)")

        # 메일 정보 파싱
        msg = email.message_from_bytes(mail[0][1])
        subject = decode_header(msg["Subject"])[0][0]
        sender = decode_header(msg["From"])[0][0]

        # 출력
        if isinstance(subject, bytes):
            try:
                print("Subject:", subject.decode("utf-8"))
            except UnicodeDecodeError:
                print("Subject:", subject)
        else:
            print("Subject:", subject)

        if isinstance(sender, bytes):
            try:
                print("From:", sender.decode("utf-8"))
            except UnicodeDecodeError:
                print("From:", sender)
        else:
            print("From:", sender)
        print("="*30)

    # 네이버 메일 서버 접속 종료
    imap.close()
    imap.logout()


def sendmail():
    # 메일 제목, 본문 내용 설정
    subject = '테스트 메일'
    content = '안녕하세요, 이것은 테스트 메일입니다.'

    # 메일 생성
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = username
    msg['To'] = yourmail
    text = MIMEText(content)
    msg.attach(text)

    # SMTP 서버 설정
    smtp_server = 'smtp.naver.com'
    smtp_port = 587
    smtp_tls = True

    # SMTP 서버 연결
    s = smtplib.SMTP(smtp_server, smtp_port)
    s.starttls()
    s.login(username, password)

    # 메일 발송
    s.sendmail(username, yourmail, msg.as_string())

    # SMTP 서버 연결 종료
    s.quit()


def sendfile():
    # 이메일 메시지 작성
    message = MIMEMultipart()
    message["Subject"] = input("subject : ")
    message["From"] = yourmail
    message["To"] = recipient

    text = MIMEText("안녕하세요, 이메일 보내기 테스트입니다.")
    message.attach(text)

    # 첨부 파일 추가
    filename = "txts/test.txt"
    with open(filename, "rb") as f:
        attachment = MIMEApplication(f.read(), _subtype="txt")
        attachment.add_header("Content-Disposition", "attachment", filename=filename)
        message.attach(attachment)

    # SMTP 서버 접속 및 이메일 보내기
    smtp = smtplib.SMTP("smtp.naver.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(yourmail, password)
    smtp.sendmail(yourmail, recipient, message.as_string())
    smtp.quit()

if __name__ == '__main__':
    global username, password, yourmail, recipient
    username = input("id : ")
    password = getpass.getpass("password : ")
    yourmail = username+'.naver.com'
    recipient = input("sendmail : ")
    showtext()
