from selenium import webdriver
from time import sleep

class FoodOrder():
    def __init__(self):
        self.driver = webdriver.Firefox()


    def interface(self):
        #self.order = []
        #self.num_of_pizzas = input('How many pizzas would you like to buy: ')
        self.street_num = input('Input street number: ')
        self.street = input('Input street name: ')
        self.suburb = input('Input Suburb name: ')
        self.postcode = input('Input postcode: ')
        print('MENU \n 1. Simply Cheese \n 2. Cheesy Garlic With Creme Fraiche \n 3. Margherita \n 4. Pepperoni \n 5. Beef & Onion \n 6. Ham & Cheese \n 7. Spicey Veg Trio')
        for j in range(int(self.num_of_pizzas)):
            self.order.append(input('Input a number for the menu item you would like for item  #%s: ' %(j+1) ))
            




    def buy(self):
        self.num_of_pizzas = 1
        self.order = [1]




        self.driver.get('https://order.dominos.com.au/estore/en/CustomerDetails/Delivery')

        now_btn = self.driver.find_element_by_class_name('ordertimenow')
        now_btn.click()

        street_num_in = self.driver.find_element_by_xpath('//*[@id="customer-street-no"]')
        street_num_in.send_keys('97')

        street_in = self.driver.find_element_by_xpath('//*[@id="customer-street-name"]')
        street_in.send_keys('Elizabeth Street')

        suburb_in = self.driver.find_element_by_xpath('//*[@id="customer-suburb"]')
        suburb_in.send_keys('Brisbane City')

        postcode_in = self.driver.find_element_by_xpath('//*[@id="customer-postcode"]')
        postcode_in.send_keys('4000')

        next1_btn = self.driver.find_element_by_xpath('//*[@id="order-time-button"]')
        next1_btn.click()

        no1_btn = self.driver.find_element_by_xpath('//*[@id="no-button"]')
        no1_btn.click()

        address_btn = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/section/ul[1]/li/a')
        address_btn.click()

        for k in range(self.num_of_pizzas):
            if self.order[k] == 1:
                try:
                    pizza = self.driver.find_element_by_xpath('/html/body/div[6]/section/section/div[2]/section[1]/div[2]/div[5]/section/div[1]/div/a/div[4]/div/div/div/button')
                    pizza.click()
                except Exception:
                    self.close_popup6447()

                try:
                    add_to_order = self.driver.find_element_by_xpath('//*[@id="add-product-button"]')
                except Exception:
                    self.close_popup6401

            elif self.order[k] == 2:
                try:
                    pizza = self.driver.find_element_by_xpath('/html/body/div[6]/section/section/div[2]/section[1]/div[2]/div[5]/section/div[2]/div/a/div[4]/div/div/div/button')
                    pizza.click()
                except:
                    self.close_popup6447()
            elif self.order[k] == 3:
                try:
                    pizza = self.driver.find_element_by_xpath('/html/body/div[6]/section/section/div[2]/section[1]/div[2]/div[5]/section/div[3]/div/a/div[4]/div/div/div/button')
                    pizza.click()
                except:
                    self.close_popup6447()
            elif self.order[k] == 4:
                try:
                    pizza = self.driver.find_element_by_xpath('/html/body/div[6]/section/section/div[2]/section[1]/div[2]/div[5]/section/div[4]/div/a/div[4]/div/div/div/button')
                    pizza.click()
                except:
                    self.close_popup6447()
            elif self.order[k] == 5:
                try:
                    pizza = self.driver.find_element_by_xpath('/html/body/div[6]/section/section/div[2]/section[1]/div[2]/div[5]/section/div[5]/div/a/div[4]/div/div/div/button')
                    pizza.click()
                except:
                    self.close_popup6447()
            elif self.order[k] == 6:
                try:
                    pizza = self.driver.find_element_by_xpath('/html/body/div[6]/section/section/div[2]/section[1]/div[2]/div[5]/section/div[6]/div/a/div[4]/div/div/div/button')
                    pizza.click()
                except:
                    self.close_popup6447()
            elif self.order[k] == 7:
                try:
                    pizza = self.driver.find_element_by_xpath('/html/body/div[6]/section/section/div[2]/section[1]/div[2]/div[5]/section/div[7]/div/a/div[4]/div/div/div/button')
                    pizza.click()
                except:
                    self.close_add_to_your_order


    def close_popup6447(self):
        pop_up1 = self.driver.find_element_by_xpath('//*[@id="offer-addtoyourorder-no-6447"]')
        pop_up1.click()

    def close_popup6401(self):
        pop_up2 = self.driver.find_element_by_xpath('//*[@id="offer-addtoyourorder-no-6401"]')
        pop_up2.click()
            

    def main(self):
        self.interface()
        self.buy()

        # Better crust add on = //*[@id="offer-addtoyourorder-no-6401"]

        #At point of getting past the upgrade your crust pop-up







