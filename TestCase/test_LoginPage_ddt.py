import time

import pytest

from selenium import webdriver
from Utilities import XLUtils
from PageObject.LoginPage_PO import LoginPage_PO
from Utilities.ReadPropertyfile import ReadConfig
from Utilities.Customlogger import LogGen

class Test_LoginPage_ddt:
    baseurl=ReadConfig.geturl()
    path=".//TestData//LogData.xlsx"

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_LoginPage(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.lp=LoginPage_PO(self.driver)

        self.row=XLUtils.getRowCount(self.path,"Sheet1")

        lst_status=[]

        for r in range(2,self.row+1):
            self.user=XLUtils.readData(self.path,"Sheet1",r,1)
            print(self.user)
            self.pwd = XLUtils.readData(self.path, "Sheet1", r, 2)
            print(self.pwd)

        self.lp.setusername(self.user)
        self.lp.setpassword(self.pwd)
        self.lp.clickloginbtn()
        time.sleep(4)

        self.driver.close()




