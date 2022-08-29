# import webbrowser
# from selenium import webdriver
# webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
# b=webbrowser.get('chrome').open('www.baidu.com')
######################################
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(r"./chromedriver")
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[4]').click()
while (True):
    #             //*[@id="addtask"]  #选择识别文件夹
    wait = WebDriverWait(driver, 8 * 60 * 60)
    click1 = wait.until(EC.presence_of_element_located(By.ID, "addtask"))
    time.sleep(60)
    click1.click()
    time.sleep(60)

    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[4]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[4]').click()
