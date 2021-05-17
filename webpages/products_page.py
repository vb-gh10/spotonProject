import random


class ProductsPage():
    def __init__(self, driver):
        self.driver = driver

    def select_random_acc(self):
        nums = [1, 2, 3, 4]
        acc1 = random.choice(nums)
        acc2 = random.choice(nums)
        acc3 = random.choice(nums)
        while acc1 == acc2 or acc1 == acc3 or acc2 == acc3:
            acc1 = random.choice(nums)
            acc2 = random.choice(nums)
            acc3 = random.choice(nums)
        print(acc1)
        print(acc2)
        print(acc3)
        if acc1 == 1:
            self.random_acc = self.driver.find_element_by_id("collar").click()
            print('Collar and Leash are clicked')
        elif acc1 == 2:
            self.random_acc = self.driver.find_element_by_id("toy").click()
            print('Chew Toy is clicked')
        elif acc1 == 3:
            self.random_acc = self.driver.find_element_by_id("carrier").click()
            print('Travel Carrier is clicked')
        else:
            self.random_acc = self.driver.find_element_by_id("vet").click()
            print('First Vet Visit is clicked')
        if acc2 == "1":
            self.random_acc = self.driver.find_element_by_id("collar").click()
            print('Collar and Leash are clicked')
        elif acc2 == "2":
            self.random_acc = self.driver.find_element_by_id("toy").click()
            print('Chew Toy is clicked')
        elif acc2 == "3":
            self.random_acc = self.driver.find_element_by_id("carrier").click()
            print('Travel Carrier is clicked')
        else:
            self.random_acc = self.driver.find_element_by_id("vet").click()
            print('First Vet Visit is clicked')
        if acc3 == "1":
            self.random_acc = self.driver.find_element_by_id("collar").click()
            print('Collar and Leash are clicked')
        elif acc3 == "2":
            self.random_acc = self.driver.find_element_by_id("toy").click()
            print('Chew Toy is clicked')
        elif acc3 == "3":
            self.random_acc = self.driver.find_element_by_id("carrier").click()
            print('Travel Carrier is clicked')
        else:
            self.random_acc = self.driver.find_element_by_id("vet").click()
            print('First Vet Visit is clicked')

    def select_collar_leash(self):
        self.driver.implicitly_wait(10)
        self.collar_leash = self.driver.find_element_by_id("collar").click()
        print("Collar and Leash are selected")

    def select_second_collar_leash(self):
        self.driver.implicitly_wait(10)
        self.chewy_toy = self.driver.find_element_by_xpath('(//input[@id="collar"])[2]').click()
        print("Collar and Leash are selected for second puppy")

    def select_chewy_toy(self):
        self.driver.implicitly_wait(10)
        self.chewy_toy = self.driver.find_element_by_id("toy").click()
        print("Chewy Toy is selected")

    def select_travel_carrier(self):
        self.driver.implicitly_wait(10)
        self.travel_carrier = self.driver.find_element_by_id("carrier").click()
        print("Travel Carrier is selected")

    def select_vet_visit(self):
        self.driver.implicitly_wait(10)
        self.vet_visit = self.driver.find_element_by_id("vet").click()
        print("First Vet Visit is selected")

    def click_adopt_another_puppy(self):
        self.driver.implicitly_wait(10)
        self.adopt_another_puppy = self.driver.find_element_by_xpath('//input[@value="Adopt Another Puppy"]').click()
        print('"Adopt Another Puppy" is clicked')

    def click_complete_adoption(self):
        self.driver.implicitly_wait(10)
        self.complete_adoption = self.driver.find_element_by_xpath('//input[@value="Complete the Adoption"]').click()
        print('"Complete the Adoption" is clicked"')

