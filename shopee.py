# -*- coding: utf-8 -*-
# @Time    : 9/24/2020 8:35 PM
# @Author  : YenYoong
# @File    : SHOPEE 商品信息.py

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time


def command():
    search_name = input('请输入你想要搜索的内容：')
    page_num = input('请输入要爬取的页数：')
    print('正在努力爬取中.....')
    for page in range(0, int(page_num)):
        url = 'https://shopee.com.my/search?keyword={}&page={}'.format(search_name, page)
        spider(url, page)


def spider(url, page):
    try:
        driver = webdriver.Chrome(executable_path=r'C:\Users\HP\Documents\WorkSpace\Python\untitled\Scraping\07 Selenium 练习\chromedriver.exe')
        driver.get(url)
        driver.implicitly_wait(1)  # 隐式等待
        driver.find_element_by_xpath('//*[@id="modal"]/div[1]/div[1]/div/div[3]/div[3]/button').click()  # 点击选择语言
        time.sleep(0.8)
        items = driver.find_elements_by_class_name('col-xs-2-4')
        court = 0
        for item in items:
            driver.execute_script("window.scrollBy(0,1000)")
            court += 1
            # print(item.text)
            # item_name = item.find_element_by_xpath('//div[@class="_1NoI8_ _1JBBaM"]').text
            item_name = item.find_element_by_css_selector('._1NoI8_').text
            item_price = item.find_element_by_css_selector('._341bF0').text
            item_location = item.find_element_by_css_selector('._3amru2').text
            item_url = item.find_element_by_tag_name('a').get_attribute('href')

            msg = '''
                爬取页数：%s
                爬虫序号：%s
                商品名称: %s
                商品价格: %s
                出货地点: %s
                商品链接：%s
            ''' % (page, court, item_name, item_price, item_location, item_url)

            print(msg)

            with open('items_page_{}.csv'.format(page), 'a', encoding='utf-8') as f:
                f.write(msg)

        print('数据爬取完成！只爬取到了', court, '个商品')

    except Exception:
        print('中途遇到👽外星人阻挡去路，数据爬取不完整！')


if __name__ == '__main__':
    command()
