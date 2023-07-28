import re
import time
from model_customer import Customer
from operation_user import UserOperations
from model_user import User

class CustomerOperation():
    def validate_email(self, user_email):
        """
        Validate the format of the email address.

        This method checks if the provided email address matches the required format.
        It uses regular expressions to perform the validation.

        Returns:
        - True if the email address is valid, False otherwise.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.fullmatch(pattern, user_email))

    def validate_mobile(self, user_mobile):
        """
        Validate the format of the mobile number.

        This method checks if the provided mobile number matches the required format.
        It uses regular expressions to perform the validation.

        Returns:
        - True if the mobile number is valid, False otherwise.
        """
        pattern = r'^(04|03)\d{8}$'
        return bool(re.fullmatch(pattern, user_mobile))

    def register_customer(self, user_name, user_password, user_email, user_mobile):
        """
        Register a new customer.

        This method registers a new customer by validating the provided user name, email,
        and mobile number. If the provided information is valid, it generates a unique user ID,
        encrypts the password, and writes the customer data to the "users.txt" file.

        Returns:
        - True if the customer registration is successful, False otherwise.
        """
        u1 = UserOperations()
        if u1.check_username_exist(user_name):
            return False
        if not self.validate_email(user_email) or not self.validate_mobile(user_mobile):
            return False
        if not u1.validate_username(user_name) or not u1.validate_password(user_password):
            return False

        u_id = u1.generate_unique_user_id()
        register_time = time.strftime("%Y-%m-%d %H:%M:%S")
        customer = Customer(u_id, user_name, u1.encrypt_password(user_password), register_time, 'customer', user_email, user_mobile)

        with open("data/users.txt", "a") as file:
            file.write(str(customer) + "\n")

        return True

    def update_profile(self, attribute_name, value, customer_object):
        """
        Update a customer's profile attribute.

        This method allows updating a customer's profile attribute such as user name, email, or mobile number.
        It performs validation on the provided value based on the attribute name and updates the customer's object
        and the "users.txt" file with the changes.

        Returns:
        - True if the profile update is successful, False otherwise.
        """
        u1 = UserOperations()

        # Check if the attribute name is valid
        if attribute_name not in ['user_name', 'user_email', 'user_mobile']:
            return False

        # Check if the provided value is valid
        if attribute_name == 'user_name':
            if not u1.validate_username(value):
                return False
        elif attribute_name == 'user_email':
            if not u1.validate_email(value):
                return False
        elif attribute_name == 'user_mobile':
            if not u1.validate_mobile(value):
                return False

        customer_obj=Customer()
        # Update the customer object's attribute value
        setattr(customer_obj, attribute_name, value)

        # Update the data/users.txt file with the changes
        updated_customers = []
        with open("data/users.txt", "r") as file:
            for line in file:
                user_info = eval(line)
                if user_info['user_id'] == customer_object.user_id:
                    user_info[attribute_name] = value
                updated_customers.append(user_info)

        with open("data/users.txt", "w") as file:
            for user_info in updated_customers:
                file.write(str(user_info) + "\n")

        return True

    def delete_customer(self, customer_id):
        """
        Delete a customer.

        This method deletes a customer from the "users.txt" file based on their customer ID.

        Returns:
        - True if the customer deletion is successful, False otherwise.
        """
        customers = []
        with open("data/users.txt", "r") as file:
            for line in file:
                customer_data = eval(line)
                if customer_data["user_id"] != customer_id:
                    customers.append(customer_data)

        with open("data/users.txt", "w") as file:
            for customer_data in customers:
                file.write(str(customer_data) + "\n")

        return True

    def get_customer_list(self, page_number):
        """
        Get a list of customers.

        This method retrieves a list of customers from the "users.txt" file based on the provided page number.
        It reads the file, extracts the customer data, and returns the customers along with the current page number
        and the total number of pages.

        Returns:
        - A tuple containing the list of customers, the current page number, and the total number of pages.
        """
        page_size = 10
        customers = []
        with open("data/users.txt", "r") as file:
            lines = file.readlines()
            total_pages = (len(lines) + page_size - 1) // page_size
            start_index = (page_number - 1) * page_size
            end_index = page_number * page_size
            for line in lines[start_index:end_index]:
                customer_data = eval(line)
                if customer_data["user_role"] == "customer":
                    customer = Customer(customer_data["user_id"], customer_data["user_name"],
                                        customer_data["user_password"], customer_data["user_register_time"],
                                        customer_data["user_email"], customer_data["user_mobile"])
                    customers.append(customer)

        return customers, page_number, total_pages

    def delete_all_users(self):
        """
        Delete all users from the "users.txt" file.

        This method deletes all users except the admin account from the "users.txt" file.
        """
        updated_users = []
        with open('data/users.txt', 'r') as file:
            for line in file:
                user = eval(line)
                if user.get('user_role') == 'admin':
                    updated_users.append(user)

        with open('data/users.txt', 'w') as file:
            for user in updated_users:
                file.write(str(user) + '\n')

# Register a customer
c1=CustomerOperation()
cu1=Customer()
# customer1 = Customer(user_name="johns", user_password="Password123", user_email="jdoe@email.com", user_mobile="98939823")
# print(c1.register_customer(user_name="johns", user_password="Password123", user_email="john@example.com", user_mobile="0412345678"))

# Update customer profile
# customer = UserOperations.login("johns", "Password123")
# c1.update_profile("user_email", "newemail@example.com", cu1)
#
# # Delete a customer
# c1.delete_customer("u_6341712642")
#
# # Get customer list
# page_number = 2
# customer_list, current_page, total_pages = c1.get_customer_list(page_number)
# print(customer_list, current_page, total_pages)
#
# # Delete all customers
# c1.delete_all_users()
