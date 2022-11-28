from POM.productDetails import Product_details
from Data.read_obj import prod_search,mob_num

class TestProductDetails:
    def test_prodDetails(self,_driver):
        product = Product_details(_driver,)
        product.search(prod_search)
        product.pro_img()
        product.pro_price()
        product.pro_name()
        product.pro_details()
        product.offer()
        product.discount()
        product.pro_brand()
        product.pro_color()
        product.wishlist(mob_num)
        product.pro_size()
        product.cart()
        product.pro_share()