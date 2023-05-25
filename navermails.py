import imaplib
import email
from email.header import decode_header

# 사용자 정보
username = "lt75355"
password = ""

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
    
    print("Subject:", subject)
    print("From:", sender)
    print("="*30)

# 네이버 메일 서버 접속 종료
imap.close()
imap.logout()
