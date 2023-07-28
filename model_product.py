# author: sshe0094 dev(s): @samrudhShetty creation date: 03/04/2023 last modified: 05/05/2023 description: This code
# defines the Product class, which inherits from the User class. The Product class represents a product and contains
# information such as the product ID, model, category, name, current price, raw price, discount, and likes count. It
# also includes a __str__ method to provide a string representation of a product. The code includes some test
# examples to demonstrate the usage of the Product class.

from model_user import User


class Product(User):
    def __init__(self, pro_id="", pro_model="", pro_category="", pro_name="", pro_current_price=0.0, pro_raw_price=0.0,
                 pro_discount=0.0, pro_likes_count=0):
        """
        Initialize a Product object with the provided attributes.

        Parameters:
        - pro_id (str): The ID of the product.
        - pro_model (str): The model of the product.
        - pro_category (str): The category of the product.
        - pro_name (str): The name of the product.
        - pro_current_price (float): The current price of the product (default: 0.0).
        - pro_raw_price (float): The raw price of the product (default: 0.0).
        - pro_discount (float): The discount percentage applied to the product (default: 0.0).
        - pro_likes_count (int): The number of likes received by the product (default: 0).
        """
        super().__init__()
        self.pro_id = pro_id
        self.pro_model = pro_model
        self.pro_category = pro_category
        self.pro_name = pro_name
        self.pro_current_price = pro_current_price
        self.pro_raw_price = pro_raw_price
        self.pro_discount = pro_discount
        self.pro_likes_count = pro_likes_count

    def __str__(self):
        """
        Return a string representation of the Product object.

        Returns:
        - str: The string representation of the Product object in the format
               "{'pro_id':'<pro_id>', 'pro_model':'<pro_model>', 'pro_category':'<pro_category>',
               'pro_name':'<pro_name>', 'pro_current_price':'<pro_current_price>', 'pro_raw_price':'<pro_raw_price>',
               'pro_discount':'<pro_discount>', 'pro_likes_count':'<pro_likes_count>'}".
        """
        return f"{{'pro_id':'{self.pro_id}', 'pro_model':'{self.pro_model}', 'pro_category':'{self.pro_category}', " \
               f"'pro_name':'{self.pro_name}', 'pro_current_price':'{self.pro_current_price}', 'pro_raw_p" \
               f"rice':'{self.pro_raw_price}', 'pro_discount':'{self.pro_discount}', 'pro_likes_count':'" \
               f"{self.pro_likes_count}'}}"

# Testing the Product class
# product1 = Product(pro_id="p_123", pro_model="Model1", pro_category="Category1", pro_name="Product 1",
#                    pro_current_price=99.99, pro_raw_price=129.99, pro_discount=23.1, pro_likes_count=10)
# product2 = Product(pro_id="p_456", pro_model="Model2", pro_category="Category2", pro_name="Product 2",
#                    pro_current_price=199.99, pro_raw_price=249.99, pro_discount=20.0, pro_likes_count=5)
#
# print(product1)
