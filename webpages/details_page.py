class DetailsPage():
    def __init__(self, driver):
        self.driver = driver

    def click_adopt_me(self):
        self.driver.implicitly_wait(10)
        self.adopt_me = self.driver.find_element_by_xpath('//input[@value="Adopt Me!"]').click()
        print('"Adopt Me!" is clicked')