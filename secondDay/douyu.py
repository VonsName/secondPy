# __author:  Administrator
# __date:  2019/5/29/029

from selenium import webdriver
import time


class DouYu:
    def __init__(self):
        self.url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome()

    def run(self):
        self.driver.get(self.url)
        li_list = self.driver.find_elements_by_xpath(
            "//*[@id='listAll']/section[2]/div[2]/ul//li")

        for li in li_list:
            print(self.driver.find_element_by_xpath("./div/a[@class='DyListCover-wrap']/div[class='DyListCover-content']/div/span").text)


if __name__ == '__main__':
    douyu = DouYu()
    douyu.run()
