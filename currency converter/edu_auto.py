from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By


class demoAutoTest:
    driver = webdriver.Chrome(service=Service('chromedriver.exe'))
    print(driver)
    driver.maximize_window()
    driver.get('https://web-dev.edualpha.jp/ja')
    time.sleep(7)
    txtSearch = driver.find_element(by=By.CLASS_NAME, value='types_teacher')
    txtSearch.click()
    txtEmail = driver.find_element(by=By.ID, value='email')
    txtEmail.send_keys("nui@edu.jp")
    txtPassword = driver.find_element(by=By.ID, value='password')
    txtPassword.send_keys("Nagi1234")
    btnLogin = driver.find_element(by=By.CLASS_NAME, value='btn-submit-login')
    btnLogin.click()
    time.sleep(5)
    btnHydrated = driver.find_element(by=By.ID, value='arrow_back_ios_black_24dp')
    btnHydrated.click()
    # test = driver.find_element(by=By.XPATH, value="//td[@title='2022-07-22']/div/button")
    # test.click()