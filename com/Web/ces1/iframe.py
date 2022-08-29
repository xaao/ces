import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="../../../chromedriver.exe")
driver.get("https://www.runoob.com/try/try.php?filename=tryjs_alert")
driver.switch_to.frame("iframeResult") #进入frame 通过frame的id值
text=driver.find_element(By.XPATH,'/html/body/input').get_attribute('value') #获取按钮的文本value，通过get_attribute('value')方法
print(text)
driver.find_element(By.XPATH,'/html/body/input').click()
try:
    alert=WebDriverWait(driver,10).until(expected_conditions.alert_is_present()) #等待、定位alert弹窗
    time.sleep(5)
    print(alert.text)
    alert=driver.switch_to.alert#定位到alert弹窗
    alert.accept()#弹窗点击确认accept，点击取消是 dismiss
except Exception as e:
    print(e.args)
driver.switch_to.default_content()#回到默认页面，每次进入frame都要重新退出，进入默认页面