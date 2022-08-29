from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class basepagecl:
    def __init__(self,driver):
        self.driver=driver
    # 进入页面
    def open(self,url):
        self.driver.get(url)
    # 退出页面
    def quit(self):
        self.driver.quit()
    # 定位元素
    def loctor(self,loct):
        return self.driver.find_element(*loct)
    # 输入
    def input(self,loct,text):
        self.loctor(loct).send_keys(text)
    # 点击
    def click(self,loct):
        self.loctor(loct).click()
# driver.close()
# 登录
class loginpagecl(basepagecl):
    def __init__(self,usename,pwd,button,driver,url):#重载父类魔法方法
        self.username2=usename
        self.pwd2=pwd
        self.button2=button
        self.driver=driver
        self.url=url

    def login(self):
        self.open(self.url)
        self.driver.implicitly_wait(60)  # 等待元素出现
        self.input(self.username2,'admin')
        self.input(self.pwd2,'123456')
        self.click(self.button2)
        time.sleep(60)

    # // *[ @ id = "app"] / div / div[2] / div / div[4] #确定按钮

    def defect(self):
        input1=self.driver.find_element_by_ID('//*[@id="input01"]')
        input1.sendkey(r'/media/json/')
        self.driver.find_element_by_XPATH('//*[ @id = "app"]/div/div[2]/div/div[4]').click()#点击开始识别
        while(True):
#             //*[@id="addtask"]  #选择识别文件夹
            wait=WebDriverWait(self.driver, 8*60*60)
            click1=wait.until(EC.presence_of_element_located(By.ID,'addtask'))
            time.sleep(60)
            click1.click()
            time.sleep(60)
            self.driver.find_element_by_XPATH('//*[ @id = "app"]/div/div[2]/div/div[4]').click()

#
if __name__ == '__main__':
    url = 'https://id2.bitahub.com/login?clientId=BITAHUB&redirectUrl=https%3A%2F%2Fwww2.bitahub.com%2F'  # 登录地址
    driver = webdriver.Chrome(executable_path='../../chromedriver')
    username = (By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[1]/div/div/span/input')  #
    pwd = (By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[2]/div/div/span/input')
    button = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[3]/button')
    Work=loginpagecl(username,pwd,button,driver,url)
    Work.login()

# 显式等待，等待自己想要得元素出来，出来之后立马执行，不管时间是否未到
# 设置浏览器：driver  等待时间：20s
# wait = WebDriverWait(driver, 20)
# # 设置判断条件：等待id='kw'的元素加载完成
# input_box = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
# ac=wait.until(EC.presence_of_element_located(By.XPATH,'//*/div[0]/class=dasdm'))

# ---------------------------
# 隐式等待不论元素是否加载完，都会等到设置得时间，才去执行
# driver.implicitly_wait(30) #隐式等待，driver全周期等待，30s内如果元素加载完就ok，未加载完则抛出异常


# 依据不同python版本使用
# driver.find_element(By.ID, 'b').click()
# driver.find_element_by_XPATH('//*/div[0]').click()