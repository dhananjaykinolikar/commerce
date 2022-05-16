import time

import pytest
from selenium import webdriver
from PageObject.LoginPage_PO import LoginPage_PO
from Utilities.ReadPropertyfile import ReadConfig
from Utilities.Customlogger import LogGen

class Test_001_LoginPage:
    baseurl=ReadConfig.geturl()
    username=ReadConfig.getusername()
    password=ReadConfig.getpassword()

    logger = LogGen.loggen()
    @pytest.mark.sanity
    def test_loginPage(self,setup):
        self.logger.info("-------Testing Test_LoginPage Started---------")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp=LoginPage_PO(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickloginbtn()
        self.driver.save_screenshot(".\\Screenshots\\"+"test_loginPage.png")
        time.sleep(3)
        self.logger.info("-------Testing Test_LoginPage End---------")
        self.driver.close()

