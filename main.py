import selenium.webdriver as webdriver
import time
import os
import datetime as dt
from datetime import datetime

noon = dt.time(12, 0, 0)
print(noon)
time_now = datetime.now().time()
print("morning = ", time_now < noon)

driver = webdriver.Chrome()
driver.implicitly_wait(30)

driver.get("https://intranet.etechconsulting-mg.com/web/login")

login = driver.find_element_by_xpath("/html/body/div[1]/main/div/form/div[1]/input")
password = driver.find_element_by_xpath("/html/body/div[1]/main/div/form/div[2]/input")
submit = driver.find_element_by_xpath("/html/body/div[1]/main/div/form/div[3]/button")

login.send_keys(os.environ.get("SIRH_LOGIN"))
password.send_keys(os.environ.get("SIRH_PASSWORD"))
submit.click()

driver.get("https://intranet.etechconsulting-mg.com/my/attendances")

attendance_sign_in = driver.find_element_by_xpath("/html/body/div[1]/main/div/div[2]/div[3]/a[2]")
attendance_sign_out = driver.find_element_by_xpath("/html/body/div[1]/main/div/div[2]/div[3]/a[1]")

attendance = attendance_sign_in if time_now < noon else attendance_sign_out

time.sleep(15)

attendance.click()
