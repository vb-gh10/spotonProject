import random


class PuppiesPage():
    def __init__(self, driver):
        self.driver = driver

    def click_brook_view_details(self):
        self.driver.implicitly_wait(10)
        self.brook_view_details = self.driver.find_element_by_xpath(
            '//h3[contains(text(),"Brook")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
        print('Brook "View Details" is clicked')

    def click_sparky_view_details(self):
        self.driver.implicitly_wait(10)
        self.sparky_view_details = self.driver.find_element_by_xpath(
            '//h3[contains(text(),"Sparky")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
        print('Sparky "View Details" is clicked')

    def random_view_details(self):
        global pup
        pups = ["Brook", "Hanna", "Maggie Mae", "Ruby Sue", "Sparky", "Spud", "Tipsy", "Topsy", "Twinkie"]
        pup = random.choice(pups)
        print("Random puppy is " + pup)
        if pup == "Brook":
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Brook")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Brook is clicked')
        elif pup == "Hanna":
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Hanna")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Hanna is clicked')
        elif pup == "Maggie Mae":
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Maggie Mae")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Maggie Mae is clicked')
        elif pup == "Ruby Sue":
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Ruby Sue")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Ruby Sue is clicked')
        elif pup == "Sparky":
            self.second_page = self.driver.find_element_by_xpath('//a[contains(text(),"2")]').click()
            self.driver.implicitly_wait(10)
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Sparky")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Sparky is clicked')
        elif pup == "Spud":
            self.second_page = self.driver.find_element_by_xpath('//a[contains(text(),"2")]').click()
            self.driver.implicitly_wait(10)
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Spud")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Spud is clicked')
        elif pup == "Tipsy":
            self.second_page = self.driver.find_element_by_xpath('//a[contains(text(),"2")]').click()
            self.driver.implicitly_wait(10)
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Tipsy")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Tipsy is clicked')
        elif pup == "Topsy":
            self.second_page = self.driver.find_element_by_xpath('//a[contains(text(),"2")]').click()
            self.driver.implicitly_wait(10)
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Topsy")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Topsy is clicked')
        else:
            self.third_page = self.driver.find_element_by_xpath('//a[contains(text(),"3")]').click()
            self.driver.implicitly_wait(10)
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Twinkie")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Twinkie is clicked')
        return pup

    def random_view_details2(self):
        pups = ["Brook", "Hanna", "Maggie Mae", "Ruby Sue", "Sparky", "Spud", "Tipsy", "Topsy", "Twinkie"]
        pup2 = random.choice(pups)
        while pup2 == pup:
            pup2 = random.choice(pups)
        print("Random puppy is " + pup2)
        if pup2 == "Brook":
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Brook")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Brook is clicked')
        elif pup2 == "Hanna":
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Hanna")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Hanna is clicked')
        elif pup2 == "Maggie Mae":
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Maggie Mae")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Maggie Mae is clicked')
        elif pup2 == "Ruby Sue":
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Ruby Sue")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Ruby Sue is clicked')
        elif pup2 == "Sparky":
            self.second_page = self.driver.find_element_by_xpath('//a[contains(text(),"2")]').click()
            self.driver.implicitly_wait(10)
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Sparky")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Sparky is clicked')
        elif pup2 == "Spud":
            self.second_page = self.driver.find_element_by_xpath('//a[contains(text(),"2")]').click()
            self.driver.implicitly_wait(10)
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Spud")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Spud is clicked')
        elif pup2 == "Tipsy":
            self.second_page = self.driver.find_element_by_xpath('//a[contains(text(),"2")]').click()
            self.driver.implicitly_wait(10)
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Tipsy")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Tipsy is clicked')
        elif pup2 == "Topsy":
            self.second_page = self.driver.find_element_by_xpath('//a[contains(text(),"2")]').click()
            self.driver.implicitly_wait(10)
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Topsy")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Topsy is clicked')
        else:
            self.third_page = self.driver.find_element_by_xpath('//a[contains(text(),"3")]').click()
            self.driver.implicitly_wait(10)
            self.view_details = self.driver.find_element_by_xpath('//h3[contains(text(),"Twinkie")]/parent::div/following-sibling::div//input[@value="View Details"]').click()
            print('Twinkie is clicked')

    def click_second_page(self):
        self.driver.implicitly_wait(10)
        self.second_page = self.driver.find_element_by_xpath('//a[contains(text(),"2")]').click()
        print('Second page is clicked')

    def assert_adopting_puppy(self):
        self.driver.implicitly_wait(10)
        self.adopting_puppy = self.driver.find_element_by_id("notice")
        assert self.adopting_puppy.text == 'Thank you for adopting a puppy!'
        print(self.adopting_puppy.text)

