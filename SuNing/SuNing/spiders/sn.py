# -*- coding: utf-8 -*-
import scrapy
from SuNing.items import SuningItem


class SnSpider(scrapy.Spider):
    name = 'sn'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com']

    def parse(self, response):
        # 取一级分类
        item = SuningItem()
        first_category_list = response.xpath("//div[@class='menu-list']//div[@class='menu-item']")
        all_category_list = []
        for firsi_cat in first_category_list:
            first_category = {}
            first_category_name = firsi_cat.xpath(".//h3/a/text()").extract_first()
            first_category_url = firsi_cat.xpath(".//h3/a/@href").extract_first()
            first_category["firstCategoryName"] = first_category_name
            first_category["firstCategoryUrl"] = first_category_url
            all_category_list.append(first_category)
            item["library"] = all_category_list
            # 取二级分类
            second_category_list = response.xpath(".//dd")
            second_category_lists = []
            for second_item in second_category_list:
                second_category = {}
                second_category_url = second_item.xpath("./a/@href").extract_first()
                second_category_name = second_item.xpath("./a/text()").extract_first()
                second_category["secondCategoryName"] = second_category_name
                second_category["secondCategoryUrl"] = second_category_url
                second_category_lists.append(second_category)
                first_category["secondCategory"] = second_category_lists

            # 取副二级分类
            sub_second_category_list = response.xpath(
                "//div[@class='menu-list']//div[@class='menu-sub']//div[@class='submenu-left']//p")
            sub_second_category_lists = []
            for p in sub_second_category_list:
                sub_second_category = {}
                sub_second_category_url = p.xpath("./a/@href").extract_first()
                sub_second_category_name = p.xpath("./a/text()").extract_first()
                sub_second_category["subSecondCategoryName"] = sub_second_category_name
                sub_second_category["subSecondCategoryUrl"] = sub_second_category_url
                sub_second_category_lists.append(sub_second_category)
                first_category["subSecondCategoryName"] = sub_second_category_lists

                third_category_li_list = p.xpath("./following-sibling::ul[1]//li")
                third_category_list = []
                for li in third_category_li_list:
                    third_category = {}
                    third_category_url = li.xpath("./a/@href").extract_first()
                    third_category_name = li.xpath("./a/text()").extract_first()
                    third_category["thirdCategoryName"] = third_category_name
                    third_category["thirdCategoryUrl"] = third_category_url
                    third_category_list.append(third_category)
                    sub_second_category["thirdCategory"] = third_category_list

                # 取副二级分类
                # sub_second_category_list = response.xpath(
                #     "//div[@class='menu-list']//div[@class='menu-sub menu-sub-down']//div[@class='submenu-left']//p")
                # for p in sub_second_category_list:
                #     sub_second_category_url = p.xpath("./a/@href").extract_first()
                #     sub_second_category_name = p.xpath("./a/text()").extract_first()
                #     third_second_li_list = p.xpath("./following-sibling::ul[1]//li")
                #     for li in third_second_li_list:
                #         third_second_url = li.xpath("./a/@href").extract_first()
                #         third_second_name = li.xpath("./a/text()").extract_first()

        yield item
