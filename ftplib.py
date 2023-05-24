import ftplib

# FTP 서버 접속 정보
ftp_server = "ftp.example.com"
ftp_user = "username"
ftp_password = "password"

# FTP 서버 연결
ftp = ftplib.FTP(ftp_server)
ftp.login(ftp_user, ftp_password)
print(ftp.getwelcome())

# 파일 다운로드
filename = "example.txt"
with open(filename, "wb") as file:
    ftp.retrbinary(f"RETR {filename}", file.write)

# 파일 업로드
filename = "example.txt"
with open(filename, "rb") as file:
    ftp.storbinary(f"STOR {filename}", file)

# 디렉토리 내 파일 목록 조회
ftp.cwd("/")
print(ftp.nlst())

# FTP 서버 연결 종료
ftp.quit()
