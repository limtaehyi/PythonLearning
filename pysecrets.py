import secrets
import string

#url-safe 텍스트 문자열 생성
print(secrets.token_urlsafe(16))


#랜덤 정수 생성
random_num = secrets.randbelow(100)
print(random_num)


#비교
a = "test"
b = "test"

if secrets.compare_digest(a, b):
    print("Strings are same.")
else:
    print("Strings are different.")


#토큰 비교
token1 = secrets.token_hex(16)
token2 = secrets.token_hex(16)

if secrets.compare_digest(token1, token2):
    print("Tokens are same.")
else:
    print("Tokens are different.")


#32바이트 랜덤 바이트 시퀀스 생성
random_bytes = secrets.token_bytes(32)

print(random_bytes)


#비번 생성
alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(10))

print(password)


#비번 생성(고급)
#최소 하나의 소문자, 대문자, 숫자 및 특수 문자를 포함하는 비밀번호를 생성
def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    if length < 4:
        print("Password length should be at least 4.")
        return None
    
    password = [secrets.choice(all_chars) for _ in range(length)]
    
    # Ensure the password has at least one lowercase, one uppercase, one digit and one special char.
    password[0] = secrets.choice(string.ascii_lowercase)
    password[1] = secrets.choice(string.ascii_uppercase)
    password[2] = secrets.choice(string.digits)
    password[3] = secrets.choice(string.punctuation)

    
    return ''.join(password)

print(generate_password(10))
