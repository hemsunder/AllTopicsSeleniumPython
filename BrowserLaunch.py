from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Softwares&Drivers/WebDriver/ChromeDriver Version79/chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.set_page_load_timeout(30)
driver.implicitly_wait(30)

driver.get("https://www.w3schools.com/Python/default.asp")
print(driver.title)
print("====================================================================")
print(driver.current_url)
print("====================================================================")
#print(driver.page_source)

#driver.close()
driver.quit()