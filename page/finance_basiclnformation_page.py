from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类


class FinanceBasiclnformation(BasePage):
    financenamess_loc = (By.CSS_SELECTOR,
                         'body > div.container > div.row > div:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(2)')
    def financenamess(self):
        self.find_element(self.financenamess_loc)
        return self.find_element(self.financenamess_loc)