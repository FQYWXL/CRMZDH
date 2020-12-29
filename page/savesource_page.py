from selenium.webdriver.common.by import By
from page.base_page import BasePage
from selenium.webdriver.support.select import Select
from time import sleep


class SaveClue(BasePage):
    fuzheren_locator = (By.ID, 'owner_name')
    chooseuser_locator = (By.ID, 'd_name')
    serch_locator = (By.CSS_SELECTOR, '#dialog-role-list > div > ul > button')
    gouxuan_locator = (By.CSS_SELECTOR, '#d_content > tr > td:nth-child(1) > input[type=radio]')
    ok_locator = (By.CSS_SELECTOR,
                  'body > div:nth-child(14) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span')
    gongsi_locator = (By.CSS_SELECTOR, '#name')
    laiyuan_locator = (By.ID, 'source')
    lianxiren_locator = (By.ID, 'contacts_name')
    beizhu_locator = (By.ID, 'description')
    save_locator = (By.CSS_SELECTOR, '#form1 > table > tfoot > tr > td > input:nth-child(1)')

    # def fuzheren(self):
    #     '''点击新建线索按钮后进入添加线索页面，进行的负责人元素定位'''
    #     self.find_element(self.fuzheren_locator).click()
    #
    # def chooseuser(self, user):
    #     '''点击负责人弹框后进行负责人输入框元素定位'''
    #     self.find_element(self.chooseuser_locator).send_keys(user)
    #
    # def serch(self):
    #     '''弹框中的搜索元素定位'''
    #     self.find_element(self.serch_locator).click()
    #
    # def gouxuan(self):
    #     '''弹框中的搜索到具体人以后勾选前面按钮元素的定位'''
    #     self.find_element(self.gouxuan_locator).click()
    #
    # def okchoose(self):
    #     '''弹框中的ok元素定位'''
    #     self.find_element(self.ok_locator).click()     以上部分负责人这块就改为默认，不指定具体负责人

    def gongsi(self, gsname):
        '''添加线索中的公司的元素定位'''
        self.find_element(self.gongsi_locator).send_keys(gsname)

    def laiyuan(self):
        '''来源定位,赋值'''
        locator = self.find_element(self.laiyuan_locator)
        select = Select(locator)
        select.select_by_index(1)

    def lianxiren(self, contactname):
        '''联系人元素定位'''
        self.find_element(self.lianxiren_locator).send_keys(contactname)

    def beizhu(self, contents):
        '''备注内容元素定位'''
        self.find_element(self.beizhu_locator).send_keys(contents)

    def savesource(self):
        '''新建线索完成后的保存元素定位'''
        self.find_element(self.save_locator).click()

    def sourcejihe(self, gsname, contactname, contents):
        # self.fuzheren()
        # self.chooseuser(user)
        # sleep(3)
        # self.serch()
        # sleep(1)
        # self.gouxuan()
        # sleep(1)
        # self.okchoose()
        # sleep(1)
        self.gongsi(gsname)
        sleep(2)
        self.laiyuan()
        sleep(2)
        self.lianxiren(contactname)
        sleep(2)
        self.beizhu(contents)
        sleep(2)
        self.savesource()

