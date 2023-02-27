from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def logout(self):
        wd = self.driver
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def create_group(self, Group):
        wd = self.driver
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(Group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(Group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(Group.footer)
        wd.find_element(By.NAME, "submit").click()
        wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, login, password):
        wd = self.driver
        wd.get("http://localhost/addressbook/")
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(login)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.ID, "LoginForm").submit()

    def destroy(self):
        self.driver.quit()