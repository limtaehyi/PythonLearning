#-*- encoding: utf-8 -*-

import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import zipfile


def unzip():
    zip_file_path="ziptest.zip"
    password_list = ["1234", "password", "qwerty", "123456"]

    def extract_zip(zip_file, password):
        try:
            zip_file.extractall(pwd=password.encode())
            print(f"비밀번호가 '{password}'로 맞춰졌습니다.")
            return True
        except Exception as e:
            print(f"비밀번호 '{password}'는 틀렸습니다. 다음 비밀번호 시도 중...")
            return False

    def brute_force_zip(zip_file_path, password_list):
        zip_file = zipfile.ZipFile(zip_file_path)

        for password in password_list:
            if extract_zip(zip_file, password):
                break

        zip_file.close()
    brute_force_zip(zip_file_path, password_list)
    
    

def websearch():
    driver = webdriver.Chrome()
    
    driver.get("https://www.google.com/")
    
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Python Selenium", Keys.RETURN)
    search_results = driver.find_elements(By.ID, "result-stats")
    print(search_results)
    
    print("press enter to continute...")
    pause = input()

    driver.quit()

def main():
    os.system("cls")
    while 1:
        print("simple programming")
        print("")
        print("1 : unzip")
        print("2 : websearch")
        print("0 : exit")
        number = int(input("input number : "))

        if number == 1:
            unzip()
        elif number == 2:
            websearch()
        else:
            break

    
    

if __name__ == '__main__':
    main()
