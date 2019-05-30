# __author:  Administrator
# __date:  2019/5/28/028

from selenium import webdriver
import time


# selenium通过元素获取属性或者文本要使用get_attribute()或者text
# 首先要下载各种驱动
# chromedriver的版本要和本机浏览器的谷歌浏览器版本一致
# driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()

# selenium.common.exceptions.SessionNotCreatedException: Message: Unable to find a matching set
# 原因是浏览器和火狐驱动不匹配
driver = webdriver.Firefox()
# driver.set_window_size(1920, 1080)
driver.maximize_window()
# 发送请求
driver.get("http://www.baidu.com")

# 使用PhantomJS截屏
# driver.save_screenshot("./baidu.png")

driver.save_screenshot("huohu.png")
# 获取cookies
cookies = driver.get_cookies()
print(cookies)

# HTML字符串
print(driver.page_source)

# 定位元素
# element1 = driver.find_element_by_id("kw")
# element1.send_keys("python")

#
# element2 = driver.find_element_by_id("su")
# element2.click()

time.sleep(5)

# 退出当前页面 相当于在浏览器上点击X
# driver.close()
# 退出浏览器
driver.quit()
