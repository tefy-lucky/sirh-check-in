import selenium.webdriver as webdriver
import time
import os

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

time.sleep(15)

attendance_sign_out.click()
