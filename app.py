import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_driver = ChromeDriverManager().install()
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)

papago_url = "https://papago.naver.com/"
driver.get(papago_url)
time.sleep(3)

ko_button = driver.find_element(By.CSS_SELECTOR, "button.btn_switch___x4Tcl").click()

while True:
    input_text = input("번역할 한국어를 입력하세요 (종료하려면 'exit' 입력): ")
    if input_text.lower() == 'exit':
        break

    form = driver.find_element(By.CSS_SELECTOR, "textarea#txtSource")
    form.clear()
    form.send_keys(input_text)
    button = driver.find_element(By.CSS_SELECTOR, "button.btn_text___3-laJ").click()  # 수정된 부분
    time.sleep(1)
    translated_text = driver.find_element(By.CSS_SELECTOR, "div#txtTarget").text
    
    # Check if input text is in Korean
    if ord(input_text[0]) >= ord('가') and ord(input_text[0]) <= ord('힣'):
        ko_button.click()  # Switch to English
        translated_text = driver.find_element(By.CSS_SELECTOR, "div#txtTarget").text
    
    print("번역 결과:", translated_text)

driver.quit()
