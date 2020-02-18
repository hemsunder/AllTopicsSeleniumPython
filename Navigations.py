from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Softwares&Drivers/WebDriver/ChromeDriver Version79/chromedriver.exe")

driver.maximize_window()
driver.delete_all_cookies()
driver.set_page_load_timeout(30)
driver.implicitly_wait(30)

driver.get("https://www.w3schools.com/Python/default.asp")
time.sleep(3)
print(driver.title)

driver.get("https://www.w3schools.com/JAVA/default.asp")
time.sleep(3)
print(driver.title)

driver.back()
time.sleep(3)
print(driver.title)

driver.forward()
time.sleep(3)
print(driver.title)

driver.quit()