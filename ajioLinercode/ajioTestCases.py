import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

d_obj = webdriver.Chrome(ChromeDriverManager().install())
a_obj = ActionChains(d_obj)
d_obj.get("https://www.ajio.com/")
d_obj.maximize_window()
d_obj.implicitly_wait(30)

d_obj.find_element("xpath","//input[@type = 'text']").send_keys("shoes")
time.sleep(2)
d_obj.find_element_by_class_name("ic-search").click()
time.sleep(2)
## 1.User should be able to see product image.
d_obj.find_element_by_class_name("rilrtl-lazy-img").click()
time.sleep(2)

handler = d_obj.window_handles
print(handler)
print(d_obj.current_window_handle)
print(d_obj.title)
d_obj.switch_to.window(handler[1])


## 2.User should be able to see product image enlarge formate.
## 3.User should be able to see good quality of image.

d_obj.find_element_by_xpath("//img[@class = 'rilrtl-lazy-img img-alignment zoom-cursor rilrtl-lazy-img-loaded']").click()
time.sleep(2)
d_obj.find_element_by_xpath("//div[@class = 'ic-close-quickview']").click()
time.sleep(2)

## 4.User should be able to see different angle images of product.
d_obj.find_element_by_xpath("//button[@class = 'slick-arrow slick-next']").click()
time.sleep(2)
d_obj.find_element_by_xpath("//button[@class = 'slick-arrow slick-next']").click()
time.sleep(2)
d_obj.find_element_by_xpath("//button[@class = 'slick-arrow slick-next']").click()

## 5.User should be see the price of product is displayed.
product_price = d_obj.find_element_by_class_name("prod-sp").is_displayed()
print("Price of product = ",product_price)


## 6.User should be see the name of product is displayed.
product_name = d_obj.find_element_by_class_name("prod-name").is_displayed()
print("Name of Product = ",product_name)

## 7.User should be see product Details.
product_details = d_obj.find_element_by_class_name("prod-desc").is_displayed()
print("Details of product = ",product_details)


## 11.User should be able to see offers for purchasing product.
d_obj.find_element_by_class_name("pdp-toggle").click()
time.sleep(2)
d_obj.find_element_by_class_name("pdp-toggle").click()


## 12.User should be able to see Discount on purchasing product.
prduct_discount = d_obj.find_element_by_class_name("promo-desc-block").is_displayed()
print("Discount is available = ",prduct_discount)


## 9.User should be able to choose Brand of product.
d_obj.find_element_by_partial_link_text("Brand :").click()
time.sleep(2)
d_obj.back()


## 10.User should be able to choose colour of product.
d_obj.find_element_by_partial_link_text("Color :").click()
time.sleep(3)
d_obj.back()
a_obj.send_keys(Keys.PAGE_UP).perform()
time.sleep(2)


## 22.User click on Wishlist. User should be add product in Wishlist.
d_obj.find_element_by_xpath('//span[text() = "SAVE TO WISHLIST"]').click()
time.sleep(2)
d_obj.find_element_by_class_name("username").send_keys("7066962805")
d_obj.find_element_by_class_name("login-btn").click()
time.sleep(30)
d_obj.find_element_by_xpath('//input[@type = "submit"]').click()
time.sleep(2)
a_obj.send_keys(Keys.PAGE_UP).perform()


## 8.User should be able to choose size of product.
d_obj.find_element_by_xpath("//div[@class = 'size-variant-block']/..//div[@class = 'size-swatch']").click()
time.sleep(2)

## 19.User click on Product. User click on Add To Bag. User should be add product in cart.
d_obj.find_element_by_class_name("btn-gold").click()
time.sleep(2)
d_obj.find_element_by_xpath("//span[text() = 'REMOVE FROM WISHLIST']")

## 25.User should be share the product.
share = d_obj.find_element_by_xpath("//div[@class = 'sprite-img prod-share-block']")
a_obj.move_to_element(share).perform()
time.sleep(2)