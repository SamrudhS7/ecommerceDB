class User:
    used_ids = set()  # Class variable to track used user_ids

    def __init__(self, user_id="u_0000000000", user_name=None, user_password=None,
                 user_register_time="00-00-0000_00:00:00", user_role="customer"):
        """
        Initialize a User object with the provided attributes.

        Parameters:
        - user_id (str): The ID of the user (default: "u_0000000000").
        - user_name (str): The name of the user (default: None).
        - user_password (str): The password of the user (default: None).
        - user_register_time (str): The timestamp of user registration in the format "DD-MM-YYYY_hh:mm:ss"
                                    (default: "00-00-0000_00:00:00").
        - user_role (str): The role of the user (default: "customer").
        """
        # if user_id in User.used_ids:
        #     raise ValueError("user_id must be unique.")

        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_register_time = user_register_time
        self.user_role = user_role

        User.used_ids.add(user_id)  # Add the user_id to the set of used ids

    def __str__(self):
        """
        Return a string representation of the User object.

        Returns:
        - str: The string representation of the User object in the format
               "{'user_id':'<user_id>', 'user_name':'<user_name>', 'user_password':'<user_password>',
               'user_register_time':'<user_register_time>', 'user_role':'<user_role>'}".
        """
        return f"{{'user_id':'{self.user_id}', 'user_name':'{self.user_name}', 'user_password':'{self.user_password}', 'user_register_time':'{self.user_register_time}', 'user_role':'{self.user_role}'}}"

    # def save_to_file(self):
    #     """
    #     Save the user data to a file named "users.txt".

    #     This method writes the string representation of the User object to the file, appending it as a new line.

    #     Note: This method is currently commented out and not used in the code.
    #     """
    #     with open("data/users.txt", "a") as file:
    #         file.write(str(self) + '\n')


# Testing the User class
# user1 = User(user_id="u_1234567890", user_name="John Doe", user_password="password123")
# user2 = User(user_id="u_9876543210", user_name="Jane Smith", user_password="qwerty")
#
# print(user1)
# #
# print(user2)
