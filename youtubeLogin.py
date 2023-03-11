from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-infobars")
driver = webdriver.Chrome('chromedriver.exe', options=options)

#Note that this example email if your a developer testing this script this example script won't allow you to continue.
email_addr = 'example@gmail.com'
passwrd = 'password_123'
phone_number = '+000000000'


driver.get("https://youtube.com")
time.sleep(3)
sign_in = driver.find_element(By.XPATH,value='/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a')
sign_in.click()
time.sleep(3)
#Note that you can replace the email_addr variable with your phone number or email address 
email = driver.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
email.send_keys(email_addr)
time.sleep(3)
next_1 = driver.find_element(By.XPATH,value='/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button')
next_1.click()
time.sleep(3)
password = driver.find_element(By.XPATH,value='/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
password.send_keys(passwrd)
time.sleep(3)

"""
#Show Password Option

show_password = driver.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/input")
show_password.click()
"""

"""
Forgot Password Option

forgot_password = driver.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/button")
forgot_password.click()
"""

next_2 = driver.find_element(By.XPATH,value='/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button')
next_2.click()

"""
If there is a security code option

security_code = driver.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/ul/li[2]/div")
security_code.click()
"""

"""
If there is a backup code option

backup_code = driver.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/ul/li[3]/div")
backup_code.click()
"""

"""
Account Recovery Option

acc_recovery = driver.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/a")
acc_recovery.click()
"""
time.sleep(3)
print("Excecution Done")
