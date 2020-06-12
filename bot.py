import requests
import bs4
from splinter import Browser
from selenium import webdriver

executable_path = {'executable_path': r'C:\Users\Paulito\Desktop\chromedriver_win32\chromedriver'}


class SupremeBot:
    def __init__(self, **info):
        self.home = 'http://www.supremenewyork.com/'
        self.shop_url = 'shop/all/'
        self.checkout_url = 'checkout/'
        self.info = info

    def home_page(self):
        self.browser = Browser('chrome', **executable_path)

    def find_product(self):
        r = requests.get("{}{}{}".format(self.home, self.shop_url, self.info['category'])).text
        soup = bs4.BeautifulSoup(r, "lxml")

        all_links = []
        needed_links = []

        for item in soup.find_all('a', href=True):
            all_links.append((item['href'], item.text))

        for link in all_links:
            if link[1] == self.info['product'] or link[1] == self.info['color']:
                needed_links.append(link[0])

        self.final_link = list(set([x for x in needed_links if needed_links.count(x)==2]))[0]
        return self.final_link

    def visit_site(self):
        self.browser.visit('{}{}'.format(self.home, self.final_link))
        self.browser.find_option_by_text(self.info['size']).click()
        self.browser.find_by_value('add to cart').click()

    def check_out(self):
        self.browser.visit('{}{}'.format(self.home, self.checkout_url))
        self.browser.find_by_id('order_billing_name').fill(self.info['name'])
        self.browser.find_by_id('order_email').fill(self.info['email'])
        self.browser.find_by_id('order_tel').fill(self.info['phone'])
        self.browser.find_by_id('bo').fill(self.info['addy'])
        self.browser.find_by_id('oba3').fill(self.info['apt'])
        self.browser.find_by_id('order_billing_zip').fill(self.info['zipfield'])
        self.browser.find_by_id('order_billing_city').fill(self.info['city'])
        self.browser.find_by_id('order_billing_name').fill(self.info['name'])
        self.browser.find_option_by_text(self.info['country']).click()
        self.browser.find_by_id('rnsnckrn').fill(self.info['number'])
        card_month = self.browser.find_by_id('credit_card_month').first
        card_month.select(self.info['month'])
        card_year = self.browser.find_by_id('credit_card_year').first
        card_year.select(self.info['year'])
        self.browser.find_by_id('orcer').fill(self.info['ccv'])

if __name__ == "__main__":
    INFO = {
            "product": "Raglan Court Jacket",
            "color": "Olive",
            "size": "Large",
            "category": "jackets",
            "name": "Blah Blah",
            "email": "xxxx@gmail.com",
            "phone": "123-456-7890",
            "addy": "111 5th St",
            "apt": 'XXXX',
            "city": "xxxxx",
            "zipfield": "90715",
            "country": "USA",
            "card": 'visa',
            "number": "XXXXXXXXXXXXXXXX",
            "month": '05',
            "year": '2022',
            "ccv": "XXXX"
        }
    bot = SupremeBot(**INFO)
    bot.home_page()
    bot.find_product()
    bot.visit_site()
    bot.check_out()
