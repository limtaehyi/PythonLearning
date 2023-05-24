import zipfile

def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        print(f"비밀번호가 '{password}'로 맞춰졌습니다.")
    except Exception as e:
        print(f"비밀번호 '{password}'는 틀렸습니다. 다음 비밀번호 시도 중...")
        return False

def brute_force_zip(zip_file_path, password_list):
    zip_file = zipfile.ZipFile(zip_file_path)

    for password in password_list:
        if extract_zip(zip_file, password):
            break

    zip_file.close()

# 메인 코드
zip_file_path = "파일명.zip"  # 본인이 사용할 zip 파일의 경로와 파일명을 입력하세요
password_list = ["1234", "password", "qwerty", "123456"]  # 비밀번호 후보 리스트를 입력하세요

brute_force_zip(zip_file_path, password_list)
