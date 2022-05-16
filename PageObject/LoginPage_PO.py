from selenium import webdriver

class LoginPage_PO:
    text_username_id="Email"
    text_password_id="Password"
    button_login_xpath="//button[contains(text(),'Log in')]"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element_by_id(self.text_username_id).clear()
        self.driver.find_element_by_id(self.text_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element_by_id(self.text_password_id).clear()
        self.driver.find_element_by_id(self.text_password_id).send_keys(password)

    def clickloginbtn(self):
        self.driver.find_element_by_xpath(self.button_login_xpath)
