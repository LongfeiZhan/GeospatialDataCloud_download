# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:43:55 2020

@author: ZhanLF
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

driver.get('https://www.gscloud.cn/accounts/login')

email = driver.find_element_by_xpath('//*[@id="userid"]')
email.send_keys('1627391527@qq.com')
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('keepmoving')
captcha = driver.find_element_by_xpath('//*[@id="id_captcha_1"]')
captcha_sj = input('请输入验证码：').strip()
captcha.send_keys(captcha_sj)

dr_buttoon = driver.find_element_by_xpath('//*[@id="login-form"]/input[3]').click() #输入验证码后点击登入按钮
time.sleep(3)
sjzy = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[4]/a/h4').click() #点击中国合成产品
time.sleep(3)
GDEMV30 = driver.find_element_by_xpath('//*[@id="dataset-listview"]/div/div/ul/li[3]/div/a[3]').click() #点击MODLT1D地表温度每天产品
time.sleep(3)

# #一共是2315页
page_num = 2315
page = 1

while page <= page_num:    
    page_sr = driver.find_element_by_xpath('//*[@id="pager1"]/div[2]/table/tbody/tr/td[7]/input')
    page_sr.clear() #清除里面数字
    time.sleep(0.5)
    page_sr.send_keys(page) #传递页码
    time.sleep(0.5)
    page_sr.send_keys(Keys.ENTER)
    time.sleep(0.5)
    # windows = driver.window_handles
    # driver.switch_to.window(windows[-1])    
    time.sleep(10)
    print('当前下载第{}页'.format(page))
    for tr_num in range(3,13): #只能取到3-12
        d_everypage = '//*[@id="all_datasets_listview"]/div/table/tbody/tr['+str(tr_num)+']/td[8]/div/div/a[2]/span'
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, d_everypage)))
        element = driver.find_element_by_xpath(d_everypage)
        webdriver.ActionChains(driver).move_to_element(element).click(element ).perform()
        # download = driver.find_element_by_xpath(d_everypage).click()
        time.sleep(5)  #每个下载间隔20s
    page += 1