from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Softwares&Drivers/WebDriver/ChromeDriver Version79/chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.set_page_load_timeout(30)
driver.implicitly_wait(30)

driver.get("http://newtours.demoaut.com/")

username = driver.find_element_by_name("userName")
print(username.is_enabled())
print(username.is_displayed())
username.send_keys("mercury")

password = driver.find_element_by_name("password")
print(password.is_displayed())
print(password.is_enabled())
password.send_keys("mercury")

signin = driver.find_element_by_name("login")
signin.click()

roundtrp_dd = driver.find_element_by_css_selector("input[value=roundtrip]")
print(roundtrp_dd.is_selected())

driver.quit()