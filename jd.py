#-*- coding : utf-8 -*&-
# @Time     :2020/2/10 20:05
# @Author   :Zhou
# @File     :jd.py
# @Software :PyCharm
import re
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq

broswer = webdriver.Chrome()
wait = WebDriverWait(broswer,10)


def Search(key):
    try:
        broswer.get('https://www.jd.com/')
        #直到加载完成获取搜索输入框和提交按钮
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#key'))
        )
        submit = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#search > div > div.form > button'))
        )
        #输入关键词并提交
        input.send_keys(key)
        submit.click()

        #获取总页数
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#J_bottomPage > span.p-skip > em:nth-child(1) > b'))
        )
        #获取商品信息
        GetProducts()
        return total.text
    except TimeoutException:
        return Search()

#翻页
def NextPage(page_num):
    try:
        broswer.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > input'))
        )
        submit = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > a'))
        )
        input.clear()
        input.send_keys(page_num)
        broswer.execute_script("arguments[0].scrollIntoView(true);", submit)
        submit.click()

        #确定跳转到了当前页
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#J_bottomPage > span.p-num > a.curr'))
        )

        # 获取商品信息
        GetProducts()
    except TimeoutException:
        return NextPage(page_num)


#获取商品信息
def GetProducts():
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#J_goodsList > ul > li > div'))
    )
    html = broswer.page_source
    doc = pq(html)
    #提取商品所在li标签
    items = doc('#J_goodsList ul li').items()
    print(items)
    for item in items:
        # print(item)
        products = {
            'image' : item.find('img').attr('src'),
            'price' : item.find('.p-price').text(),
            'name' : item.find('.p-name a').attr('title'),
            'shop' : item.find('.p-shop .J_im_icon a').text(),
        }
        #打印商品信息，可换成存储
        print(products)


def main():
    total = Search('美食')
    print(total)
    for i in range(2,total):
        NextPage(i)


if __name__ == '__main__':
    main()