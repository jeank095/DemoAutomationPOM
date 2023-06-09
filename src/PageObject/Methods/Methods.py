from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from src.PageObject.Locators import Locators as lc
from src.PageObject.Locators import Locators_Itera as li


class Methods:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_firstname(self, firstname):
        self.driver.find_element(By.CSS_SELECTOR, lc.css_firstname_placeholder).clear()
        self.driver.find_element(By.CSS_SELECTOR, lc.css_firstname_placeholder).send_keys(firstname)

    def set_lastname(self, lastname):
        self.driver.find_element(By.CSS_SELECTOR, lc.css_lastname_placeholder).clear()
        self.driver.find_element(By.CSS_SELECTOR, lc.css_lastname_placeholder).send_keys(lastname)

    def set_address(self, address):
        self.driver.find_element(By.XPATH, lc.xpath_address).clear()
        self.driver.find_element(By.XPATH, lc.xpath_address).send_keys(address)

    def set_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, lc.css_email_type).clear()
        self.driver.find_element(By.CSS_SELECTOR, lc.css_email_type).send_keys(email)

    def set_phone(self, phone):
        self.driver.find_element(By.CSS_SELECTOR, lc.css_phone_type).clear()
        self.driver.find_element(By.CSS_SELECTOR, lc.css_phone_type).send_keys(phone)

    def set_gender(self, gender):
        if gender.casefold() == 'male':
            self.driver.find_element(By.CSS_SELECTOR, lc.css_male_gender_value).click()
        elif gender.casefold() == 'female':
            self.driver.find_element(By.CSS_SELECTOR, lc.css_female_gender_value).click()
        else:
            self.driver.find_element(By.CSS_SELECTOR, lc.css_male_gender_value).click()

    def set_hobbies(self, hobby):
        if hobby.casefold() == 'cricket':
            self.driver.find_element(By.ID, lc.id_hobbies_cricket).click()
        elif hobby.casefold() == 'movies':
            self.driver.find_element(By.ID, lc.id_hobbies_movies).click()
        elif hobby.casefold() == 'hockey':
            self.driver.find_element(By.ID, lc.id_hobbies_hockey).click()

    def set_languages(self, languages):

        ddw = self.driver.find_element(By.XPATH, lc.language_box_xpath)
        ddw.click()
        self.wait.until(ec.element_to_be_clickable(ddw))
        options = self.driver.find_elements(By.XPATH, lc.language_options_xpath)
        for e in options:
            if e.text == languages:
                e.click()


    def set_skills(self, skill):
        skill_ddw = Select(self.driver.find_element(By.ID, lc.id_skills_ddw))
        skill_ddw.select_by_visible_text(skill)


class Methods_itera:

    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(By.ID, li.txbx_id_name).send_keys(name)

    def set_mobile(self, number):
        self.driver.find_element(By.ID, li.txbx_id_phone).send_keys(number)

    def set_email(self, email):
        self.driver.find_element(By.ID, li.txbx_id_email).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.ID, li.txbx_id_password).send_keys(password)

    def set_address(self, address):
        self.driver.find_element(By.ID, li.txbx_id_address).send_keys(address)

    def click_submit(self):
        self.driver.find_element(By.NAME, li.bttn_css_submit).click()

    def set_gender(self, gender):
        if gender == 'male':
            self.driver.find_element(By.ID, li.rd_id_male_gender).click()
        elif gender == 'female':
            self.driver.find_element(By.ID, li.rd_id_female_gender).click()

    def set_days(self, weekday):
        days = self.driver.find_elements(By.XPATH, li.days_xpath)
        for l in days:
            if l.text == weekday:
                l.click()

    def set_country(self, country):
        countries = Select(self.driver.find_element(By.CLASS_NAME, li.ddw_class_country))
        countries.select_by_visible_text(country)

    def set_year(self, year):
        years = self.driver.find_elements(By.XPATH, li.rd_years_xpath)
        for y in years:
            if y.text == year:
                y.click()