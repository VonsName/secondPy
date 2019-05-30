# __author:  Administrator
# __date:  2019/5/29/029

from selenium import webdriver
from lxml import etree

driver = webdriver.Chrome()
driver.get("https://mail.163.com/")
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)
driver.find_element_by_name("email").send_keys("vons0828")
driver.find_element_by_name("password").send_keys("isdcr82828*/.")
driver.find_element_by_id("dologin").click()

cookies = {i["name"]: i["value"] for i in driver.get_cookies()}
print(cookies)
