# author: sshe0094
# dev(s): @samrudhShetty


from model_user import User

class Order(User):
    def __init__(self, order_id="o_00000", user_id="", pro_id="", order_time="00-00-0000_00:00:00"):
        """
        Initialize an Order object with the provided attributes.

        Parameters:
        - order_id (str): The ID of the order (default: "o_00000").
        - user_id (str): The ID of the user associated with the order (default: "").
        - pro_id (str): The ID of the product associated with the order (default: "").
        - order_time (str): The timestamp of the order in the format "DD-MM-YYYY_hh:mm:ss"
                            (default: "00-00-0000_00:00:00").
        """
        self.order_id = order_id
        self.user_id = user_id
        self.pro_id = pro_id
        self.order_time = order_time

    def __str__(self):
        """
        Return a string representation of the Order object.

        Returns:
        - str: The string representation of the Order object in the format
               "{'order_id':'<order_id>', 'user_id':'<user_id>', 'pro_id':'<pro_id>', 'order_time':'<order_time>'}".
        """
        return f"{{'order_id':'{self.order_id}', 'user_id':'{self.user_id}', 'pro_id':'{self.pro_id}', 'order_time':'{self.order_time}'}}"

    # def save_to_file(self):
    #     """
    #     Save the order data to a file named "orders.txt".

    #     This method writes the string representation of the Order object to the file, appending it as a new line.

    #     Note: This method is currently commented out and not used in the code.
    #     """
    #     with open("data/orders.txt", "a") as file:
    #         file.write(str(self) + '\n')


# Testing the Order class
# order1 = Order(order_id="o_12345", user_id="u_9876543210", pro_id="p_456", order_time="01-01-2023_10:30:00")
# order2 = Order(order_id="o_67890", user_id="u_1234567890", pro_id="p_123", order_time="02-01-2023_15:45:00")
#
# print(order1)  # Output: {'order_id':'o_12345', 'user_id':'u_9876543210', 'pro_id':'p_456', 'order_time':'01-01-2023_10:30:00'}
# print(order2)  # Output: {'order_id':'o_67890', 'user_id':'u_1234567890', 'pro_id':'p_123', 'order_time':'02-01-2023_15:45:00'}
