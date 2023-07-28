# Import the User class from the model_user module.
from model_user import User


# Define the Customer class, which inherits from the User class.
class Customer(User):

    # Initialize the Customer object with the following parameters:
    # - user_id: The unique identifier for the customer user.
    # - user_name: The name of the customer user.
    # - user_password: The password for the customer user.
    # - user_register_time: The date and time when the customer user registered.
    # - user_role: The role of the customer user (e.g., "customer").
    # - user_email: The email address of the customer user.
    # - user_mobile: The mobile phone number of the customer user.
    def __init__(self, user_id="", user_name="", user_password="", user_register_time="00-00-0000_00:00:00", user_role="customer", user_email="", user_mobile=""):
        # Call the __init__() method of the User class to initialize the customer user object.
        super().__init__(user_id, user_name, user_password, user_register_time, user_role)
        # Set the user_email and user_mobile properties of the customer user object.
        self.user_email = user_email
        self.user_mobile = user_mobile

    # Define the __str__() method to return a string representation of the Customer object.
    def __str__(self):
        # Return a JSON object containing the following properties of the customer user object:
        # - user_id
        # - user_name
        # - user_password
        # - user_register_time
        # - user_role
        # - user_email
        # - user_mobile
        return f"{{'user_id':'{self.user_id}', 'user_name':'{self.user_name}', 'user_password':'{self.user_password}', 'user_register_time':'{self.user_register_time}', 'user_role':'{self.user_role}', 'user_email':'{self.user_email}', 'user_mobile':'{self.user_mobile}'}}"


# Testing the Customer class
# customer1 = Customer(user_id="u_1234567890", user_name="John Doe", user_password="password123", user_email="jdoe@email.com", user_mobile="98939823")
# customer2 = Customer(user_id="u_9876543210", user_name="Jane Smith", user_password="qwerty", user_email="jsmith@email.com", user_mobile="989398545")
#
# print(customer1)
# print(customer2)