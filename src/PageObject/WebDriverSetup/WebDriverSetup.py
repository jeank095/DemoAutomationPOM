import unittest
from selenium import webdriver

class WebDriverSetup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.get("https://demo.automationtesting.in/Register.html")
        self.driver.get("https://itera-qa.azurewebsites.net/home/automation")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
