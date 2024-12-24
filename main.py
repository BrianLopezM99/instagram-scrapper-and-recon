import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

with open("proxies_cleaned.txt", "r") as file:
    proxy_list = [line.strip() for line in file.readlines()]

proxy_address = random.choice(proxy_list)
chrome_options = Options()

chrome_options.add_argument(f'--proxy-server={proxy_address}')

service = Service('D:/chromedriver-win64/chromedriver.exe')

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://httpbin.org/ip")

time.sleep(5)

driver.get('https://tempail.com/es/')
time.sleep(2)
email = driver.find_element(By.ID, 'eposta_adres')
emailValue =email.get_attribute('value')
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
driver.get('https://www.instagram.com/')
time.sleep(2)

driver.get('https://www.instagram.com/accounts/emailsignup/')
time.sleep(2)

inputs = driver.find_elements(By.CLASS_NAME, '_aa4b')
button_register = driver.find_element(By.CLASS_NAME, '_acan')
select_date_birthday = driver.find_elements(By.CLASS_NAME, '_aau-')

inputs[0].send_keys(emailValue)
inputs[1].send_keys('123123??')
inputs[2].send_keys('chuy salas rios')
inputs[3].send_keys('elchuyitodosuwu')
button_register[3].click()
time.sleep(2)

select_month_element = select_date_birthday[0]
select_day_element = select_date_birthday[1]
select_year_element = select_date_birthday[2]

select_month = Select(select_month_element)
select_day = Select(select_day_element)
select_year = Select(select_year_element)
    
select_month.select_by_visible_text('mayo')
select_day.select_by_visible_text('5')
select_year.select_by_visible_text('2001')

time.sleep(2)

driver.quit()



# driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input').send_keys(emailValue)
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input').send_keys('123456')

# time.sleep(2)