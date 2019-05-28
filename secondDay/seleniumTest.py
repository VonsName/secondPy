# __author:  Administrator
# __date:  2019/5/28/028

from selenium import webdriver
import time

# chromedriver的版本要和本机浏览器的谷歌浏览器版本一致
driver = webdriver.Chrome()

# 发送请求
driver.get("http://www.baidu.com")

# 定位元素
element1 = driver.find_element_by_id("kw")
element1.send_keys("python")

#
element2 = driver.find_element_by_id("su")
element2.click()

time.sleep(5)
# 退出
driver.quit()
