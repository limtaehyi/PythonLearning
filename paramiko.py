import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# SSH 연결
ssh.connect(hostname='127.0.0.1', username='root', password='12356')

# 명령 실행
stdin, stdout, stderr = ssh.exec_command('ls')

# 출력 결과 확인
print(stdout.read().decode())

# 연결 종료
ssh.close()
