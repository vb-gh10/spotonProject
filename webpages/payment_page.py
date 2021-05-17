class PaymentPage():
    def __init__(self, driver):
        self.driver = driver

    def add_order_name(self):
        self.driver.implicitly_wait(10)
        self.order_name = self.driver.find_element_by_id('order_name').send_keys("John Doe")
        print('Name is added')

    def add_order_address(self):
        self.driver.implicitly_wait(10)
        self.order_address = self.driver.find_element_by_id('order_address').send_keys("Chicago, IL")
        print('Address is added')

    def add_order_email(self):
        self.driver.implicitly_wait(10)
        self.order_email = self.driver.find_element_by_id('order_email').send_keys("johndoe@test.co")
        print('Email is added')

    def select_check_payment(self):
        self.driver.implicitly_wait(10)
        self.check_payment_option = self.driver.find_element_by_xpath('//select[@id="order_pay_type"]/option[@value="Check"]').click()
        print('Check is selected')

    def select_credit_card_payment(self):
        self.driver.implicitly_wait(10)
        self.check_payment_option = self.driver.find_element_by_xpath('//select[@id="order_pay_type"]/option[@value="Credit card"]').click()
        print('Credit card is selected')

    def click_place_order(self):
        self.driver.implicitly_wait(10)
        self.place_order = self.driver.find_element_by_xpath('//input[@value="Place Order"]').click()
        print('"Place Order" is clicked"')

