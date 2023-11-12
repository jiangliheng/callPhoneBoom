#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


def visit_website(url):
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")
        driver.get(url)

        handles = driver.window_handles
        driver.switch_to.window(handles[-1])

        print('点击输入框')
        driver.find_element(By.CLASS_NAME, 'pc-imlp-component-typebox-container').click()
        time.sleep(3)
        print('输入病情')
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div[2]/div[4]/div[2]/textarea').send_keys(
            "您好,我比较急,想详细了解,能麻烦给我回电不?")
        time.sleep(3)
        print('发送病情')
        driver.find_element(By.XPATH, '//div[text()="发送"]').click()
        print('输入手机号')
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div[4]/div[2]/div[4]/div[2]/textarea').send_keys(phone)
        time.sleep(3)
        print('发送手机号')
        driver.find_element(By.XPATH, '//div[text()="发送"]').click()
    except Exception as exc:
        # 如果发生错误就跳过
        print("出现错误,跳过")
        pass


def boom(phone):
    """模仿浏览器，请求api信息"""
    with open('api.txt', 'r') as file:
        urls = file.readlines()

    num = len(urls)

    # 遍历链接地址
    for i, url in enumerate(urls):
        print(i,num)
        visit_website(url)


# 程序主入口
if __name__ == "__main__":
    # get_cookie()
    boom("phone1")
