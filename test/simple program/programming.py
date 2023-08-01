# -*- encoding: utf-8 -*-
import os

import zipfile

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def websearch():
    driver = webdriver.Chrome()
    
    driver.get("https://www.google.com/")
    
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Python Selenium", Keys.RETURN)
    search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
    
    print("press enter to continute...")
    pause = input()

    driver.quit()

def unzip():
    zip_file_path = "ziptest.zip" 
    password_list = ["1234", "password", "qwerty", "123456"]

    def extract_zip(zip_file, password):
        try:
            zip_file.extractall(pwd=password.encode())
            print(f" ## 비밀번호 '{password}'로 맞춰졌습니다.")
            with open("Flag.txt","r") as savedfile:
                print("")
                print("")
                print(savedfile.read())
                print("")
                print("")
                print("press enter to continute...")
                pause = input()
        except Exception as e:
            print(f" -- 비밀번호 '{password}'는 틀렸습니다.")
            return False

    def brute_force_zip(zip_file_path, password_list):
        zip_file = zipfile.ZipFile(zip_file_path)

        for password in password_list:
            if extract_zip(zip_file, password):
                break

        zip_file.close()
    brute_force_zip(zip_file_path, password_list)
    
def main():
    while 1:
        os.system("cls")
        print("""
                                                      __             
 .-----.----.-----.-----.----.---.-.--------.--------|__.-----.-----.
 |  _  |   _|  _  |  _  |   _|  _  |        |        |  |     |  _  |
 |   __|__| |_____|___  |__| |___._|__|__|__|__|__|__|__|__|__|___  |
 |__|             |_____|                                     |_____|
                                                                    


""")
        print("1. unzip")
        print("2. websearch")
        print("0. exit")
        print("")
        val = int(input("number : "))

        if val == 0:
            break
        elif val == 1:
            unzip()
        elif val == 2:
            websearch()


if __name__ == '__main__':
    main()
