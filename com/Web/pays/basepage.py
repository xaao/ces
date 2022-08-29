
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