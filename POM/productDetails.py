import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from Data import read_obj
product_obj = read_obj.read_locators()
print(product_obj)



class Product_details:

    def __init__(self,d_obj):
        self.d_obj=d_obj

    def search(self,value):
        self.value = value
        self.d_obj.find_element(*product_obj["text_search1"]).send_keys(value)
        self.d_obj.find_element(*product_obj["text_search2"]).click()

    def pro_img(self):
        self.d_obj.find_element(*product_obj["text_pro_img1"]).click()
        handler = self.d_obj.window_handles
        print(handler)
        print(self.d_obj.current_window_handle)
        self.d_obj.switch_to.window(handler[1])
        self.a_obj = ActionChains(self.d_obj)
        print(self.d_obj.current_window_handle)
        self.d_obj.find_element(*product_obj["text_pro_img2"]).click()
        time.sleep(2)
        self.d_obj.find_element(*product_obj["text_pro_img3"]).click()
        time.sleep(2)
        self.d_obj.find_element(*product_obj["text_pro_img4"]).click()
        time.sleep(2)
        self.d_obj.find_element(*product_obj["text_pro_img5"]).click()
        time.sleep(2)
        self.d_obj.find_element(*product_obj["text_pro_img6"]).click()


    def pro_price(self):
        self.product_price = self.d_obj.find_element(*product_obj["text_pro_price"]).is_displayed()
        print("Price of product = ", self.product_price)

    def pro_name(self):
        self.product_name = self.d_obj.find_element(*product_obj["text_pro_name"]).is_displayed()
        print("Name of Product = ", self.product_name)

    def pro_details(self):
        self.product_details = self.d_obj.find_element(*product_obj["text_pro_details"]).is_displayed()
        print("Details of product = ", self.product_details)

    def offer(self):
        self.d_obj.find_element(*product_obj["text_offer1"]).click()
        time.sleep(2)
        self.d_obj.find_element(*product_obj["text_offer2"]).click()

    def discount(self):
        prduct_discount = self.d_obj.find_element(*product_obj["text_discount"]).is_displayed()
        print("Discount is available = ", prduct_discount)

    def pro_brand(self):
        self.d_obj.find_element(*product_obj["text_brand"]).click()
        self.d_obj.back()

    def pro_color(self):
        self.d_obj.find_element(*product_obj["text_colour"]).click()
        self.d_obj.back()
        self.a_obj.send_keys(Keys.PAGE_UP).perform()

    def wishlist(self,num):
        self.num = num
        self.d_obj.find_element(*product_obj["text_wishlist1"]).click()
        self.d_obj.find_element(*product_obj["text_wishlist2"]).send_keys(num)
        self.d_obj.find_element(*product_obj["text_wishlist3"]).click()
        time.sleep(30)
        self.d_obj.find_element(*product_obj["text_wishlist4"]).click()
        self.a_obj.send_keys(Keys.PAGE_UP).perform()
        time.sleep(2)


    def pro_size(self):
        self.d_obj.find_element(*product_obj["text_pro_size"]).click()
        time.sleep(2)


    def cart(self):
        self.d_obj.find_element(*product_obj["text_cart"]).click()
        time.sleep(5)
        self.d_obj.find_element(*product_obj["text_wishlist5"]).click()

    def pro_share(self):
        self.share = self.d_obj.find_element(*product_obj["text_share"])
        self.a_obj.move_to_element(self.share).perform()

