import unittest

from src.PageObject.WebDriverSetup.WebDriverSetup import WebDriverSetup
from src.PageObject.Methods.Methods import Methods_itera


class Test002_Iteraqa(WebDriverSetup):

    def test_iteraqa(self):
        driver = self.driver

        i = Methods_itera(driver)
        i.set_name('Charles')
        i.set_mobile('3057199252')
        i.set_email('test@gmail.com')
        i.set_password('Aa123')
        i.set_address('clle 30#82c-30')
        i.click_submit()
        i.set_gender('male')
        i.set_days('Monday')
        i.set_days('Friday')
        i.set_country('Malta')
        i.set_year('2 years')


if __name__ == '__main__':
    unittest.main()
