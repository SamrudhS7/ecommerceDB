import random
import string
import re
from model_admin import Admin
from model_customer import Customer

class UserOperations():
    def generate_unique_user_id(self):
        unique_id = ''.join(random.choices(string.digits, k=10))
        return f"u_{unique_id}"

    def encrypt_password(self, user_password):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=len(user_password) * 2))
        encrypted_password = "^^"
        for i in range(len(user_password)):
            encrypted_password += random_string[2 * i] + user_password[i]
        encrypted_password += "$$"
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        decrypted_password = encrypted_password[3:-2:2]
        return decrypted_password

    def check_username_exist(self, user_name):
        with open("data/users.txt", "r") as file:
            for line in file:
                user_info = eval(line)
                if user_info['user_name'] == user_name:
                    return True
        return False

    def validate_username(self, user_name):
        pattern = r'^[a-zA-Z_]{5,}$'
        return bool(re.fullmatch(pattern, user_name))

    def validate_password(self, user_password):
        pattern = r'^(?=.*[a-zA-Z])(?=.*\d).{5,}$'
        return bool(re.fullmatch(pattern, user_password))


    def login(self, user_name, user_password):
        with open("data/users.txt", "r") as file:
            for line in file:
                user_info = eval(line)
                if user_info['user_name'] == user_name and self.decrypt_password(user_info['user_password']) == user_password:
                    if user_info['user_role'] == 'customer':
                        return Customer(user_info['user_id'], user_info['user_name'], user_info['user_password'],
                                        user_info['user_register_time'],'customer', user_info['user_email'],
                                        user_info['user_mobile'])
                    elif user_info['user_role'] == 'admin':
                        return Admin(user_info['user_id'], user_info['user_name'], user_info['user_password'],
                                     user_info['user_register_time'], 'admin')
        return None


# Testing the UserOperations class
user_op = UserOperations()
#
# # Generate unique user IDs
# print(user_op.generate_unique_user_id())  # Output: u_1234567890
# print(user_op.generate_unique_user_id())  # Output: u_0987654321
#
# # Encrypt passwords
# print(user_op.encrypt_password("adminpass1"))  # Output: ^^qnwmradibo1$$
# print(user_op.encrypt_password("divya31"))  # Output: ^^muhVW60ISwTQ13h6f$$
#
# # Decrypt passwords
# print(user_op.decrypt_password("^^RCqu1sVtNommdeTrh_OJ19$$"))  # Output: FIT9136
# print(user_op.decrypt_password("^^SFHIXTQ9Z1k3r6$$"))
#
# # Check username existence
# print(user_op.check_username_exist("johnsmith"))  # Output: False
# print(user_op.check_username_exist("admin"))  # Output: True
#
# # Validate username
# print(user_op.validate_username("Johns"))  # Output: True
# print(user_op.validate_username("admin"))  # Output: False
#
# # Validate password
# print(user_op.validate_password("password1"))  # Output: True
# print(user_op.validate_password("test"))  # Output: False
#
# # Login
# user1 = user_op.login("divyah", "divya31")
# print(user1)  # Output: Customer object if user exists and role is customer, None otherwise
#
# user2 = user_op.login("johns", "Password123")
# print(user2)  # Output: Admin object if user exists and role is admin, None otherwise
