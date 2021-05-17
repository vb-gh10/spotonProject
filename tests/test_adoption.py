import time
import unittest

from selenium import webdriver

from webpages.details_page import DetailsPage
from webpages.payment_page import PaymentPage
from webpages.products_page import ProductsPage
from webpages.puppies_page import PuppiesPage


class AdoptionTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Safari()
        self.driver.maximize_window()
        self.driver.get("http://puppies.herokuapp.com/")
        self.driver.implicitly_wait(10)


    def test_brook_adoption(self):
        """
        Test scenario: Adopt Brooke, add a Chewy Toy and a Travel Carrier, pay with Check
        """
        driver = self.driver

        puppiespage = PuppiesPage(driver)
        detailspage = DetailsPage(driver)
        productspage = ProductsPage(driver)
        paymentpage = PaymentPage(driver)

        time.sleep(3)
        puppiespage.click_brook_view_details()
        time.sleep(3)
        detailspage.click_adopt_me()
        time.sleep(3)
        productspage.select_chewy_toy()
        time.sleep(1)
        productspage.select_travel_carrier()
        time.sleep(1)
        productspage.click_complete_adoption()
        time.sleep(3)
        paymentpage.add_order_name()
        time.sleep(1)
        paymentpage.add_order_address()
        time.sleep(1)
        paymentpage.add_order_email()
        time.sleep(1)
        paymentpage.select_check_payment()
        time.sleep(1)
        paymentpage.click_place_order()
        time.sleep(3)
        puppiespage.assert_adopting_puppy()

    def test_sparky_adoption(self):
        """
        Test scenario: Adopt Sparky, add a Collar & Leash, pay with Credit Card
        """
        driver = self.driver

        puppiespage = PuppiesPage(driver)
        detailspage = DetailsPage(driver)
        productspage = ProductsPage(driver)
        paymentpage = PaymentPage(driver)

        time.sleep(3)
        puppiespage.click_second_page()
        time.sleep(3)
        puppiespage.click_sparky_view_details()
        time.sleep(3)
        detailspage.click_adopt_me()
        time.sleep(3)
        productspage.select_collar_leash()
        time.sleep(1)
        productspage.click_complete_adoption()
        time.sleep(3)
        paymentpage.add_order_name()
        time.sleep(1)
        paymentpage.add_order_address()
        time.sleep(1)
        paymentpage.add_order_email()
        time.sleep(1)
        paymentpage.select_credit_card_payment()
        time.sleep(1)
        paymentpage.click_place_order()
        time.sleep(3)
        puppiespage.assert_adopting_puppy()

    def test_random_dogs_collar_leash(self):
        """
        Test scenario: Adopt 2 Random Dogs, add a Collar & Leash to each, pay with Credit Card
        """
        driver = self.driver

        puppiespage = PuppiesPage(driver)
        detailspage = DetailsPage(driver)
        productspage = ProductsPage(driver)
        paymentpage = PaymentPage(driver)

        time.sleep(3)
        puppiespage.random_view_details()
        time.sleep(3)
        detailspage.click_adopt_me()
        time.sleep(3)
        productspage.click_adopt_another_puppy()
        time.sleep(3)
        puppiespage.random_view_details2()
        time.sleep(3)
        detailspage.click_adopt_me()
        time.sleep(3)
        productspage.select_collar_leash()
        time.sleep(1)
        productspage.select_second_collar_leash()
        time.sleep(1)
        productspage.click_complete_adoption()
        time.sleep(3)
        paymentpage.add_order_name()
        time.sleep(1)
        paymentpage.add_order_address()
        time.sleep(1)
        paymentpage.add_order_email()
        time.sleep(1)
        paymentpage.select_credit_card_payment()
        time.sleep(1)
        paymentpage.click_place_order()
        time.sleep(3)
        puppiespage.assert_adopting_puppy()

    def test_random_dogs_random_accessories(self):
        """
        Test Scenario: Adopt 2 Random Dogs add a 3 Random Accessories to 1, pay with Credit Card
        """
        driver = self.driver

        puppiespage = PuppiesPage(driver)
        detailspage = DetailsPage(driver)
        productspage = ProductsPage(driver)
        paymentpage = PaymentPage(driver)

        time.sleep(3)
        puppiespage.random_view_details()
        time.sleep(3)
        detailspage.click_adopt_me()
        time.sleep(3)
        productspage.click_adopt_another_puppy()
        time.sleep(3)
        puppiespage.random_view_details2()
        time.sleep(3)
        detailspage.click_adopt_me()
        time.sleep(3)
        productspage.select_random_acc()
        time.sleep(3)
        productspage.click_complete_adoption()
        time.sleep(3)
        paymentpage.add_order_name()
        time.sleep(1)
        paymentpage.add_order_address()
        time.sleep(1)
        paymentpage.add_order_email()
        time.sleep(1)
        paymentpage.select_credit_card_payment()
        time.sleep(1)
        paymentpage.click_place_order()
        time.sleep(3)
        puppiespage.assert_adopting_puppy()

    def tearDown(self):
        self.driver.implicitly_wait(10)
        self.driver.quit()
        print("Test Completed")
