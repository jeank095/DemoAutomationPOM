import time
import unittest

from src.PageObject.WebDriverSetup.WebDriverSetup import WebDriverSetup
from src.PageObject.Methods.Methods import Methods


class Test_001_Register(WebDriverSetup):

    def test_register(self):
        driver = self.driver
        l = Methods(driver)
        l.set_firstname('Jean')
        l.set_lastname('Blanco')
        l.set_address('Calle 30#82C-30')
        l.set_email('jeank095@gmail.com')
        l.set_phone('3057199252')
        l.set_gender('Female')
        l.set_hobbies('Cricket')
        l.set_hobbies('Movies')
        l.set_languages('English')
        l.set_languages('Urdu')
        l.set_skills('C')


if __name__ == '__main__':
    unittest.main()
