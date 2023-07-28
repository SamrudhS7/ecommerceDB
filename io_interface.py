# author: sshe0094
#dev(s): @samrudhShetty
# creation date: 03/04/2023
# last modified: 05/05/2023
# description: create main, main_menu and generate_test_data methods

class IOOperation:
    def get_user_input(self, message, num_of_args):
        # This method takes user input and splits it into a list of arguments.
        # It ensures that the returned list has the desired number of arguments.
        user_input = input(message).split()[:num_of_args]
        user_args = user_input + [""] * (num_of_args - len(user_input))
        return user_args

    def main_menu(self):
        # This method displays the main menu options for login.
        print("╔══════════════════════════╗")
        print("║       Login menu         ║")
        print("╠══════════════════════════╣")
        print("║ 1. Login                 ║")
        print("║ 2. Register              ║")
        print("║ 3. Quit                  ║")
        print("╚══════════════════════════╝")

    def admin_menu(self):
        # This method displays the admin menu options.
        print("╔══════════════════════════════════════╗")
        print("║           Admin menu                 ║")
        print("╠══════════════════════════════════════╣")
        print("║ 1. Show products                     ║")
        print("║ 2. Add customers                     ║")
        print("║ 3. Show customers                    ║")
        print("║ 4. Show orders                       ║")
        print("║ 5. Generate test data                ║")
        print("║ 6. Generate all statistical figures  ║")
        print("║ 7. Delete all data                   ║")
        print("║ 8. Delete customer using customer id ║")
        print("║ 9. Delete order using order id       ║")
        print("║ 10. Delete product using product id  ║")
        print("║ 11. Logout                           ║")
        print("╚══════════════════════════════════════╝")

    def customer_menu(self):
        # This method displays the customer menu options.
        print("╔══════════════════════════════════════╗")
        print("║           Customer menu              ║")
        print("╠══════════════════════════════════════╣")
        print("║ 1. Show profile                      ║")
        print("║ 2. Update profile                    ║")
        print("║ 3. Show products (e.g., '3 keyword'  ║")
        print("║    or '3')                           ║")
        print("║ 4. Show history orders               ║")
        print("║ 5. Generate all consumption figures  ║")
        print("║ 6. Get product using product id      ║")
        print("║ 7. Logout                            ║")
        print("╚══════════════════════════════════════╝")

    def show_list(self, user_role, list_type, object_list):
        # This method displays a list of objects based on the user role and list type.
        if user_role == "admin" or list_type != "customer":
            objects, page_number, total_page = object_list
            print(f"{list_type.capitalize()} List:")
            for i, obj in enumerate(objects, start=1):
                print(f"{i}. {obj}")
            print(f"Page: {page_number}/{total_page}")
        else:
            print("You do not have permission to view this list.")

    def print_error_message(self, error_source, error_message):
        # This method prints an error message with the source of the error and the error message itself.
        print(f"Error in {error_source}: {error_message}")

    def print_message(self, message):
        # This method prints a general message.
        print(message)

    def print_object(self, target_object):
        # This method prints the string representation of the target object.
        print(str(target_object))


# Instantiate the IOOperation class
# io_operation = IOOperation()

# The following lines are commented out because they were used for testing individual methods.
# Uncomment them if you want to test each method separately.

# Test the get_user_input method
# user_input = io_operation.get_user_input("Enter your name, age: ", 2)
# print("User input:", user_input)

# Test the main_menu method
# io_operation.main_menu()

# Test the admin_menu method
# io_operation.admin_menu()

# Test the customer_menu method
# io_operation.customer_menu()

# Test for admin role, displaying a list of orders
# io_operation.show_list("admin", "order", order_list)

# Test for customer role, trying to display a list of customers (should be denied)
# io_operation.show_list("customer", "customer", customer_list)

# Test for admin role, displaying a list of products
# io_operation.show_list("admin", "product", product_list)

# Test for customer role, displaying a list of orders
# io_operation.show_list("customer", "order", order_list)

# Uncomment the following lines if you want to test the print_error_message, print_message, and print_object methods.
# error_source = "UserOperation.login"
# error_message = "Username or password incorrect"
# io_operation.print_error_message(error_source, error_message)
#
# message = "Welcome to the system!"
# io_operation.print_message(message)
#
# target_object = Customer()
# target_object = Admin()
# target_object = Order()
# target_object = Product()
# io_operation.print_object(target_object)
