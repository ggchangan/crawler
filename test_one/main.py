#!/usr/bin/python
# -*- coding: UTF-8 -*-


import time
import os
from selenium import webdriver
from urllib import urlretrieve

#IMG_SAVE_PATH = "images"
#IMG_SAVE_PATH = "/Users/renzhang/OpenStudy/pythonStudy/crawler/images"
IMG_SAVE_DIR = "17huo"
IMG_SAVE_PATH = os.path.join(os.path.split(os.path.abspath(__file__))[0], "../images", IMG_SAVE_DIRt )
chrome_drvier_path = "/Users/renzhang/Applications/chromedriver/chromedriver"
browser = webdriver.Chrome(chrome_drvier_path)
browser.set_page_load_timeout(30)

# get page count information
url = 'http://www.17huo.com/newsearch/?k=%E5%A4%A7%E8%A1%A3'
browser.get(url)
page_info = browser.find_element_by_css_selector("body > div.wrap > div.search_container > div.pagem.product_list_pager > div")
print(page_info.text)
page_count = int((page_info.text.split(",")[0]).split(' ')[1])
print("total %d pages" % page_count)
for page in range(page_count):
    if page > 2:
        break

    url = "http://www.17huo.com/newsearch/?k=%E5%A4%A7%E8%A1%A3&page=" + str(page + 1)
    browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    goods = browser.find_element_by_css_selector("body > div.wrap > div.search_container > div.book-item-list.clearfix")\
        .find_elements_by_class_name("book-item-list-box")
    print("第%d页有%d件商品" % ((page + 1), len(goods)))
    # body > div.wrap > div.search_container > div.book-item-list.clearfix > div:nth-child(1) > a > div.book-item-top.clearfix
    # body > div.wrap > div.search_container > div.book-item-list.clearfix > div:nth-child(2) > a > div.book-item-mid.clearfix
    # body > div.wrap > div.search_container > div.book-item-list.clearfix > div:nth-child(2) > a > div.book-item-top.clearfix
    # body > div.wrap > div.search_container > div.book-item-list.clearfix > div:nth-child(2) > a > div.book-item-mid.clearfix > div.book-item-price > span
    # body > div.wrap > div.search_container > div.book-item-list.clearfix > div:nth-child(3) > a > div.book-item-top.clearfix
    index = 1
    for good in goods:
        try:
            title = good.find_element_by_css_selector("div:nth-child(%d) > a > div.book-item-top.clearfix" % index).text
            price = good.find_element_by_css_selector("div:nth-child(%d) > a > div.book-item-mid.clearfix > div.book-item-price > span" % index).text
            img_url = good.find_element_by_css_selector("div:nth-child(%d) > a > div.img_box > img" % index).get_attribute("data-original") #src
            index += 1
            img_name = os.path.join(IMG_SAVE_PATH, "%s%s" % (title, os.path.splitext(img_url)[1]))
            urlretrieve(img_url, img_name)
            print("title:%s, price:%s, img:%s" % (title, price, img_url))
        except:
            print "Exception"


if __name__ == '__main__':
    pass