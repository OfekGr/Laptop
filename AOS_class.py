from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AOS:
    def __init__(self, driver):
        self.driver = driver


    def speakers_category(self):
        self.driver.find_element(By.ID, "speakersImg").click()

    def return_to_previous(self):
        self.driver.back()

    def add_to_cart(self):
        self.driver.find_element(By.NAME, "save_to_cart").click()

    def get_first_prod_price_in_cart(self):
        prod_price_with =self.driver.find_element(By.XPATH, '//*[@id="product"]/td[3]/p').text
        prod_price_without=prod_price_with.replace('$','')
        return prod_price_without

    def get_first_prod_name_in_cart(self):
        return self.driver.find_element(By.XPATH, '//*[@id="product"]/td[2]/a/h3').text

    def get_first_prod_quantity_in_cart(self):
        quantity_with=self.driver.find_element(By.XPATH, '//*[@id="product"]/td[2]/a/label[1]').text
        return quantity_with.replace('QTY:','')

    def add_1_to_product_quantity(self):
        self.driver.find_element(By.CLASS_NAME, "plus").click()

    def remove_first_product_from_cart(self):
        self.driver.find_element(By.CLASS_NAME, "removeProduct").click()

