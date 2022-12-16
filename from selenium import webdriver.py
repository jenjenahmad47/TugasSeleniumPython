from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time  

print("Test case now started")
options = webdriver.ChromeOptions()
options.add_argument("start-maximized");
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
myemail = "blindfolded17@gmail.com" #please change email for further running script
driver.get("http://barru.pythonanywhere.com/daftar")
driver.find_element(By.ID, "signUp").click()
time.sleep(7)
driver.find_element(By.ID, "name_register").send_keys("Jenjen Ahmad Zaeni")
time.sleep(3)
driver.find_element(By.ID, "email_register").send_keys(myemail)
time.sleep(3)
driver.find_element(By.ID, "password_register").send_keys("password123")
time.sleep(3)
driver.find_element(By.ID, "signup_register").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
time.sleep(7)
driver.find_element(By.ID, "name_register").clear()
time.sleep(3)
driver.find_element(By.ID, "email_register").clear()
time.sleep(3)
driver.find_element(By.ID, "password_register").clear()
time.sleep(3)
driver.find_element(By.ID, "signup_register").click()
time.sleep(7)
driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
time.sleep(3)
driver.find_element(By.ID, "signIn").click()
time.sleep(3)
driver.find_element(By.ID, "email").send_keys(myemail)
time.sleep(3)
driver.find_element(By.ID, "password").send_keys("password123")
time.sleep(3)
driver.find_element(By.ID, "signin_login").click()
time.sleep(7)
driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
time.sleep(5)
driver.find_element(By.ID, "email").clear()
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "email").send_keys(myemail)
time.sleep(3)
driver.find_element(By.ID, "password").send_keys("randomwrongpassword")
time.sleep(3)
driver.find_element(By.ID, "signin_login").click()
time.sleep(7)
driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
time.sleep(5)
driver.find_element(By.ID, "email").clear()
time.sleep(3)
driver.find_element(By.ID, "password").clear()
time.sleep(3)
driver.find_element(By.ID, "signin_login").click()
time.sleep(7)
driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
time.sleep(5)
driver.close()
print("\nTest case successfully completed")