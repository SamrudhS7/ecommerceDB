# Import the User class from the model_user module.
from model_user import User


# Define the Admin class, which inherits from the User class.
class Admin(User):

    # Initialize the Admin object with the following parameters:
    # - user_id: The unique identifier for the admin user.
    # - user_name: The name of the admin user.
    # - user_password: The password for the admin user.
    # - user_register_time: The date and time when the admin user registered.
    # - user_role: The role of the admin user (e.g., "admin").
    def __init__(self, user_id="u_0000000000", user_name="admin", user_password="adminpass", user_register_time="00-00-0000_00:00:00",
                 user_role="admin"):
        # Call the __init__() method of the User class to initialize the admin user object.
        super().__init__(user_id, user_name, user_password, user_register_time, user_role)

    # Define the __str__() method to return a string representation of the Admin object.
    def __str__(self):
        # Return a JSON object containing the following properties of the admin user object:
        # - user_id
        # - user_name
        # - user_password
        # - user_register_time
        # - user_role
        return f"{{'user_id':'{self.user_id}', 'user_name':'{self.user_name}', 'user_password':'{self.user_password}', 'user_register_time':'{self.user_register_time}', 'user_role':'{self.user_role}'}}"


# Create an Admin object named admin1.
# admin1 = Admin()
#
# # Print the admin1 object.
# print(admin1)