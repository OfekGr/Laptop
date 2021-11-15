from unittest import  TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from AOS_class import AOS
from time import sleep
class TestAOS_page(TestCase):
    def setUp(self):
        service1 = Service(r"C:\Users\PC\Desktop\drivers\chrome\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service1)
        self.driver.get("https://www.advantageonlineshopping.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.find_element(By.ID, "Layer_1").click()
        sleep(2)
        self.driver.close()

    # add 2 products (first quantity is 3, second quantity is 2),
    # to the shopping cart and check if the sum of products in cart is 5
    def test_add_products_to_cart(self):
        AOS.speakers_category(self)
        self.driver.find_element(By.ID, "20").click()
        for i in range(2):
            AOS.add_1_to_product_quantity(self)
        AOS.add_to_cart(self)
        AOS.return_to_previous(self)
        self.driver.find_element(By.ID, "25").click()
        AOS.add_1_to_product_quantity(self)
        AOS.add_to_cart(self)
        cart_sum=self.driver.find_element(By.CSS_SELECTOR, "#shoppingCartLink > span")
        self.assertEqual(int(cart_sum.text),5)


    # add 3 products in different colors and quantities, and check if the cart is correct
    def test_cart_after_adding_products(self):
        AOS.speakers_category(self)
        self.driver.find_element(By.ID, "20").click()
        AOS.add_1_to_product_quantity(self)
        AOS.add_to_cart(self)
        self.driver.find_element(By.CSS_SELECTOR, '[title="GRAY"]').click()
        self.driver.find_element(By.CLASS_NAME, "minus").click()
        AOS.add_to_cart(self)
        AOS.return_to_previous(self)
        self.driver.find_element(By.ID, "25").click()
        AOS.add_to_cart(self)
        total_price=self.driver.find_element(By.XPATH, '//*[@id="toolTipCart"]/div/table/tfoot/tr[1]/td[2]/span')
        sum_total_price=total_price.get_attribute('innerHTML')
        first_prod_name=self.driver.find_element(By.CSS_SELECTOR, '[href="#/product/25?color=55CDD5&quantity=1&pageState=edit"]>h3')
        self.assertEqual(first_prod_name.text, "BOSE SOUNDLINK WIRELESS SPE...")
        first_prod_price=AOS.get_first_prod_price_in_cart(self)
        AOS.remove_first_product_from_cart(self)
        second_prod_color=self.driver.find_element(By.CSS_SELECTOR,'a[href="#/product/20?color=C3C3C3&quantity=1&pageState=edit"]>label>span[class="ng-binding"]')
        self.assertEqual(second_prod_color.text, "GRAY")
        second_prod_price = AOS.get_first_prod_price_in_cart(self)
        AOS.remove_first_product_from_cart(self)
        third_prod_quantity=self.driver.find_element(By.XPATH,'//*[@id="product"]/td[2]/a/label[1]')
        self.assertEqual(third_prod_quantity.text, "QTY: 2")
        third_prod_price = AOS.get_first_prod_price_in_cart(self)
        self.assertEqual(float(first_prod_price), 129.00)
        self.assertEqual(float(second_prod_price), 269.99)
        self.assertEqual(float(third_prod_price), 539.98)
        self.assertEqual(float(sum_total_price.replace('$','')), 938.97)

    # Add 2 different products to cart and remove one, check if the 2nd still in cart
    def test_cart_after_removing_product(self):
        AOS.speakers_category(self)
        self.driver.find_element(By.ID, "20").click()
        AOS.add_to_cart(self)
        AOS.return_to_previous(self)
        self.driver.find_element(By.ID, "25").click()
        AOS.add_to_cart(self)
        prod_in_cart = self.driver.find_element(By.XPATH, '//*[@id="product"]/td[2]/a/h3')
        self.assertEqual(prod_in_cart.get_attribute('innerHTML'), "BOSE SOUNDLINK WIRELESS SPE...")
        AOS.remove_first_product_from_cart(self)
        prod_in_cart=self.driver.find_element(By.XPATH,'//*[@id="product"]/td[2]/a/h3')
        self.assertNotEqual(prod_in_cart.get_attribute('innerHTML'), "BOSE SOUNDLINK WIRELESS SPE...")

    # Check if the shopping cart screen actually appears after adding a product and clicking the cart icon
    def test_transfer_to_cart_page(self):
        AOS.speakers_category(self)
        self.driver.find_element(By.ID, "20").click()
        AOS.add_to_cart(self)
        self.driver.find_element(By.ID, "menuCart").click()
        shopping_cart_text=self.driver.find_element(By.XPATH, "/html/body/div[3]/section/article/nav/a[2]")
        self.assertEqual(shopping_cart_text.text, "SHOPPING CART")


    def test_name_price_quantity(self):
        AOS.speakers_category(self)
        self.driver.find_element(By.ID, "20").click()
        AOS.add_to_cart(self)
        AOS.return_to_previous(self)
        self.driver.find_element(By.ID, "25").click()
        AOS.add_1_to_product_quantity(self)
        AOS.add_to_cart(self)
        AOS.return_to_previous(self)
        self.driver.find_element(By.ID, "24").click()
        for i in range(2):
            AOS.add_1_to_product_quantity(self)
        AOS.add_to_cart(self)

        total_price = self.driver.find_element(By.XPATH, '//*[@id="toolTipCart"]/div/table/tfoot/tr[1]/td[2]/span')
        sum_total_price = total_price.get_attribute('innerHTML')
        first_prod_name = AOS.get_first_prod_name_in_cart(self)
        first_prod_price=float(AOS.get_first_prod_price_in_cart(self))
        first_prod_quantity=int(AOS.get_first_prod_quantity_in_cart(self))
        AOS.remove_first_product_from_cart(self)
        second_prod_name = AOS.get_first_prod_name_in_cart(self)
        second_prod_price=float(AOS.get_first_prod_price_in_cart(self))
        second_prod_quantity=int(AOS.get_first_prod_quantity_in_cart(self))
        AOS.remove_first_product_from_cart(self)
        third_prod_name = AOS.get_first_prod_name_in_cart(self)
        third_prod_price = float(AOS.get_first_prod_price_in_cart(self))
        third_prod_quantity = int(AOS.get_first_prod_quantity_in_cart(self))
        webpayment=sum_total_price.replace('$', '')
        amount_to_pay=float(webpayment)
        sum_of_payments=first_prod_price+second_prod_price+third_prod_price
        print(f"{first_prod_name}, quantity: {first_prod_quantity}, price in $: {first_prod_price} \n{second_prod_name}, quantity: {second_prod_quantity}, price in $: {second_prod_price} \n{third_prod_name}, quantity: {third_prod_quantity}, price in $: {third_prod_price}")
        print(f"sum of product prices: {sum_of_payments} \namount to pay on website: {amount_to_pay}")
        if amount_to_pay != sum_of_payments:
            raise AssertionError("Sum of products isn't equal to the payment amount!")
        else:
            print("Prices are the same, you're free to go!")