from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Chrome 브라우저를 실행하는 WebDriver 객체 생성
driver = webdriver.Chrome()

# 구글 검색 페이지 열기
driver.get("https://www.google.com/")

# 검색어 입력란 찾기
search_box = driver.find_element(By.NAME, "q")

'''
search_box.clear()
----------------------------------------------------------------------------------------
upload = driver.find_element_by_tag('input')
upload.send_keys(file_path)
----------------------------------------------------------------------------------------
posting = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/article/p[51]')
posting.click()
----------------------------------------------------------------------------------------
select = Select(driver.find_element_by_name('select_name'))

select.select_by_index(index=2)
select.select_by_visible_text(text="option_text")
select.select_by_value(value='고리오')

select.deselect_all()
----------------------------------------------------------------------------------------
from selenium.webdriver import ActionChains

action_chains = ActionChains(driver)
action_chains.drag_and_drop(source, target).perform()
----------------------------------------------------------------------------------------
driver.execute_script("document.getElementsByName('id')[0].value=\'"+query+"\'")
----------------------------------------------------------------------------------------
driver.forward()
driver.back()
----------------------------------------------------------------------------------------
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
----------------------------------------------------------------------------------------
driver.minimize_window()
driver.maximize_window()
----------------------------------------------------------------------------------------
driver.save_screenshot('screenshot.png')
----------------------------------------------------------------------------------------
# Go to the correct domain
driver.get('http://www.example.com')

# Now set the cookie. This one's valid for the entire domain
cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’}
driver.add_cookie(cookie)

# And now output all the available cookies for the current URL
driver.get_cookies()
'''
# 검색어 입력
search_box.send_keys("Python Selenium", Keys.RETURN)

# 검색 결과 출력
search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")

time.sleep(10)

# 브라우저 종료
driver.quit()
