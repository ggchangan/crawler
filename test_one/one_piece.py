#!/usr/bin/python
# -*- coding: UTF-8 -*-


import time
import os
from selenium import webdriver
from urllib import urlretrieve

IMG_SAVE_DIR = "one_piece"
IMG_SAVE_PATH = os.path.join(os.path.split(os.path.abspath(__file__))[0], "../images", IMG_SAVE_DIR)
print(IMG_SAVE_PATH)
chrome_drvier_path = "/Users/renzhang/Applications/chromedriver/chromedriver"
browser = webdriver.Chrome(chrome_drvier_path)
browser.set_page_load_timeout(30)

# get page count information
url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%B5%B7%E8%B4%BC%E7%8E%8B&oq=%E6%B5%B7%E8%B4%BC%E7%8E%8B&rsp=-1'
browser.get(url)
#browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#time.sleep(3)
images = browser.find_element_by_css_selector("#imgid > div:nth-child(1) > ul")\
    .find_elements_by_class_name("imgitem")
index = 1
for image in images:
    try:
        image_title = image.get_attribute("data-title") + str(index)
        img_url = image.find_element_by_css_selector("div > a > img").get_attribute("data-imgurl") #src
        #img_detail_url = ""
        print("title:%s, img:%s" % (image_title, img_url))
        index += 1
        img_name = os.path.join(IMG_SAVE_PATH, "%d%s" % (index, os.path.splitext(img_url)[1]))
        urlretrieve(img_url, img_name)
    except Exception, e :
        print(e.message)


#TODO get original picture
def get_orginal_img(browser, img_detail_url):
    browser.get(img_detail_url)
    img_url = browser.find_element_by_css_selector("#currentImg").get_attribute("src")

    urlretrieve(img_url, img_name)

if __name__ == '__main__':
    pass