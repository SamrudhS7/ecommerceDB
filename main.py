import pandas as pd

from io_interface import IOOperation
from operation_admin import Admin
from operation_customer import CustomerOperation
from operation_order import OrderOperation
from operation_user import UserOperations
from opreation_product import ProductOperations


def login_control():
    pass


def customer_control(customer):
    io_op = IOOperation()
    io_op.customer_menu()

    while True:
        try:
            user_choice = io_op.get_user_input("Welcome to the customer menu! Please enter your choice: ", 1)
        except ValueError:
            user_choice = [9]

        if user_choice[0] == '1':
            try:
                user_info_role = eval(str(customer))
                user_name = user_info_role['user_name']
                user_mobile = user_info_role['user_mobile']
                user_email = user_info_role['user_email']
                register_time = user_info_role['user_register_time']

                data = {
                    "Name": [user_name],
                    "Mobile": [user_mobile],
                    "Email": [user_email],
                    "Registered Time": [register_time]
                }

                df = pd.DataFrame(data)
                io_op.print_message(df)

            except Exception as e:
                io_op.print_message("An error occurred while retrieving user information.")
                io_op.print_message(str(e))

        elif user_choice[0] == '2':
            co1 = CustomerOperation()
            while True:
                io_op.print_message(
                    "You are now updating your profile. Please note only the username, email, and mobile number can be "
                    "updated. Please contact the admin for a change in password.")
                user_att = io_op.get_user_input("Please enter the attribute to be updated: ", 1)
                user_att_value = io_op.get_user_input("Please enter the new value to be updated: ", 1)
                try:
                    val = co1.update_profile(user_att, user_att_value, customer)

                    if val is False:
                        io_op.print_message("You are trying to do an update that isn't allowed. Please try again.")
                    elif val is True:
                        io_op.print_message("Profile update successful.")
                    else:
                        io_op.print_message("Invalid update!")

                except Exception as e:
                    io_op.print_message("An error occurred while updating the profile.")
                    io_op.print_message(str(e))

                choice = io_op.get_user_input("Do you want to update another attribute? (yes/no): ", 1)
                if choice[0].lower() != "yes":
                    break

            io_op.customer_menu()

        elif user_choice[0] == '3':
            try:
                io_op.print_message("Please choose how you'd like to see the products:")
                io_op.print_message("╔══════════════════════════════════════╗")
                io_op.print_message("║         Show products menu           ║")
                io_op.print_message("╠══════════════════════════════════════╣")
                io_op.print_message("║ 1. Show products by page number      ║")
                io_op.print_message("║ 2. Show products by id               ║")
                io_op.print_message("║ 3. Show products by keyword          ║")
                io_op.print_message("╚══════════════════════════════════════╝")
                choice = io_op.get_user_input("Please enter your choice: ", 1)
                co1 = ProductOperations()

                while True:
                    if choice[0] == '3':
                        pg_key = io_op.get_user_input("Please enter the keyword (Please be wary of the case): ", 1)
                        try:
                            products = co1.get_product_list_by_keyword(pg_key)
                            io_op.print_message(f"Products with Keyword: '{pg_key}'")
                            for product in products:
                                print(product)

                        except Exception as e:
                            io_op.print_message("An error occurred while retrieving products by keyword.")
                            io_op.print_message(str(e))

                    elif choice[0] == '1':
                        page_number = io_op.get_user_input("Please enter the page number: ", 1)[0]

                        if page_number.isdigit():
                            pg_key = int(page_number)
                            try:
                                products, page_number, total_pages = co1.get_product_list(pg_key)
                                io_op.print_message(f"Products on page: '{pg_key}'")
                                io_op.print_message(f"Page Number: {page_number}")
                                io_op.print_message(f"Total Pages: {total_pages}")

                                for product in products:
                                    io_op.print_message(product)

                            except Exception as e:
                                io_op.print_message("An error occurred while retrieving products by page number.")
                                io_op.print_message(str(e))

                        else:
                            io_op.print_message("Invalid page number. Please enter a valid integer.")

                    elif choice[0] == '2':
                        pg_key = io_op.get_user_input("Please enter the product ID: ", 1)

                        if pg_key.isdigit():
                            product = co1.get_product_by_id(pg_key)

                            if product is not None:
                                io_op.print_message(f"Product with ID '{pg_key}':")
                                io_op.print_message(product)
                            else:
                                io_op.print_message(f"Product with ID '{pg_key}' not found.")
                        else:
                            io_op.print_message("Invalid product ID. Please enter a valid integer.")

                    io_op.print_message("╔════════════════════════════╗")
                    io_op.print_message("║         Menu Options       ║")
                    io_op.print_message("╠════════════════════════════╣")
                    io_op.print_message("║ 1. Continue                ║")
                    io_op.print_message("║ 2. Go back                 ║")
                    io_op.print_message("╚════════════════════════════╝")
                    user_choice = io_op.get_user_input("Please enter your choice: ", 1)
                    if user_choice[0] == '2':
                        break  # Exit the while loop and go back

            except Exception as e:
                io_op.print_message("An error occurred while accessing the products menu.")
                io_op.print_message(str(e))

        elif user_choice[0] == '4':
            try:
                cust = eval(customer)
                cu_id = cust["user_id"]
                op = OrderOperation()
                pg_no = io_op.get_user_input("Please enter the page number: ", 1)
                page_orders, page_number, total_pages = op.get_order_list(cu_id, pg_no)
                for page_order in page_orders[0]:
                    io_op.print_message(page_order)
                    io_op.print_message(page_number + '/' + total_pages)

            except Exception as e:
                io_op.print_message("An error occurred while retrieving the order list.")
                io_op.print_message(str(e))

        elif user_choice[0] == '5':
            try:
                cust_id = io_op.get_user_input("Please enter the customer ID for which figures are to be generated: ",
                                               1)
                o1 = OrderOperation()

                o1.generate_single_customer_consumption_figure(cust_id[0])
                io_op.print_message("Single customer consumption figure generated and saved at "
                                    "data/figure/single_customer_consumption_figure.png")

                o1.generate_all_customers_consumption_figure()
                io_op.print_message("All customer consumption figure generated and saved at "
                                    "data/figure/all_customers_consumption_figure.png")

                o1.generate_all_top_10_best_sellers_figure()
                io_op.print_message("Top 10 best sellers figure generated and saved at "
                                    "data/figure/generate_all_top_10_best_sellers_figure.png")

                io_op.print_message('The figures have been generated successfully.')

                break

            except Exception as e:
                io_op.print_message("An error occurred while generating figures.")
                io_op.print_message(str(e))

        elif user_choice[0] == '6':
            try:
                pro_op = ProductOperations()
                valid_product_id = False

                while not valid_product_id:
                    product_id = io_op.get_user_input("Enter the product ID: ", 1)
                    if product_id[0].isdigit():
                        product_id_number = int(product_id[0])
                        valid_product_id = True
                    else:
                        io_op.print_message("Kindly enter a valid product ID: ")

                product = pro_op.get_product_by_id(product_id_number)

                if product is not None:
                    io_op.print_message(product)
                else:
                    io_op.print_message("Product ID does not exist")

            except Exception as e:
                io_op.print_message("An error occurred while retrieving product details.")
                io_op.print_message(str(e))

        elif user_choice[0] == '7':
            break

        else:
            io_op.print_message('Invalid Inputs, please try again.')


def admin_control():
    io_op = IOOperation()
    customer_operation = CustomerOperation()
    product_operation = ProductOperations()
    order_operation = OrderOperation()
    # user_info = eval(str(admin_obj))
    io_op.print_message("Operations for Admin")
    login = True
    while login:
        io_op.admin_menu()
        choice = io_op.get_user_input("Kindly enter your choice", 1)
        if choice[0] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
            io_op.print_message("Please enter a valid choice")
            continue
        if choice[0] == '1':
            io_op.print_message("The product list can be retrieved in 3 ways")
            valid_input = False
            user_choice = ''
            while not valid_input:
                io_op.print_message("1. By page number")
                io_op.print_message("2. By keyword")
                io_op.print_message("3. By product Id")
                product_choice = io_op.get_user_input("Kindly enter your choice", 1)
                if product_choice[0] not in ['1', '2', '3']:
                    io_op.print_message("Kindly enter the correct choice")
                else:
                    user_choice = product_choice[0]
                    valid_input = True
            if user_choice == '1':
                valid_page = False
                page_number = 0
                while not valid_page:
                    page = io_op.get_user_input("Kindly enter the page number", 1)
                    if page[0].isdigit():
                        page_number = int(page[0])
                        valid_page = True
                    else:
                        io_op.print_message("Kindly enter a valid number")
                product_list = product_operation.get_product_list(page_number)
                # io_op.show_list(product_list[0],page_number,product_list[2])
                io_op.print_message("The products are :")
                for product in product_list[0]:
                    io_op.print_message(product)
                io_op.print_message(f"Page Number : {product_list[1]}")
                io_op.print_message(f"Total number of pages : {product_list[2]}")
            elif user_choice == '2':
                keyword = io_op.get_user_input("Kindly enter the keyword", 1)
                product_list = product_operation.get_product_list_by_keyword(keyword[0])
                io_op.print_message(f"Product List by the keyword {keyword[0]} are :")
                for product in product_list:
                    io_op.print_message(product)
            elif user_choice == '3':
                product_id = io_op.get_user_input("Kindly enter the product id", 1)
                product_id_number = 0
                if product_id[0].isdigit():
                    product_id_number = int(product_id[0])
                    io_op.print_message(f"Product by the product id {product_id[0]} is :")
                    product = product_operation.get_product_by_id(product_id_number)
                    io_op.print_message(product)
                else:
                    io_op.print_message("Invalid Product Id number")
        elif choice[0] == '2':
            cust_name = io_op.get_user_input("Enter the customer user name", 1)
            cust_password = io_op.get_user_input("Enter the customer password", 1)
            cust_email = io_op.get_user_input("Enter mail id", 1)
            cust_phone = io_op.get_user_input("Enter 10 digit phone number", 1)
            registered = customer_operation.register_customer(cust_name, cust_password, cust_email, cust_phone)
            if registered:
                io_op.print_message(f"{cust_name} registered successfully")
            else:
                io_op.print_message("Customer Registration unsuccessful")

        elif choice[0] == '3':
            valid_page = False
            page_number = 0
            while not valid_page:
                page = io_op.get_user_input("Kindly enter the page number", 1)
                if page[0].isdigit():
                    page_number = int(page[0])
                    valid_page = True
                else:
                    io_op.print_message("Kindly enter a valid number")
            customer_list = customer_operation.get_customer_list(page_number)
            if len(customer_list[0]) == 0:
                io_op.print_message("No customers in that page")
            else:
                for customer in customer_list[0]:
                    no = 1
                    io_op.print_message(f"{no} {customer}")
                    no = no + 1

        elif choice[0] == '4':
            valid_page = False
            page_number = 0
            customer_id = io_op.get_user_input(
                "Please provide the customer ID for whom you would like to check orders.", 1)
            while not valid_page:
                page = io_op.get_user_input("Kindly enter the page number", 1)
                if page[0].isdigit():
                    page_number = int(page[0])
                    valid_page = True
                else:
                    io_op.print_message("Please enter a valid number")
            order_list = order_operation.get_order_list(customer_id[0], page_number)
            if len(order_list[0]) == 0:
                io_op.print_message("No orders in that page")
            else:
                for order in order_list[0]:
                    no = 1
                    io_op.print_message(f"{no} {order}")
                    no = no + 1

        elif choice[0] == '5':
            io_op.print_message("Generating simulated data...")
            order_operation.generate_test_order_data()
            io_op.print_message("Simulation data generated")

        elif choice[0] == '6':
            io_op.print_message("1. Generating Figure: Single Customer Consumption")
            customer_id = io_op.get_user_input(
                "Please enter the customer ID to generate their individual consumption figure:", 1)
            order_operation.generate_single_customer_consumption_figure(customer_id[0])
            io_op.print_message(
                "The figure for single customer consumption has been generated and saved at "
                "data/figure/single_customer_consumption_figure.png")

            io_op.print_message("2. Generating Figure: All Customer Consumption")
            order_operation.generate_all_customers_consumption_figure()
            io_op.print_message(
                "The figure for all customer consumption has been generated and saved at "
                "data/figure/all_customers_consumption_figure.png")

            io_op.print_message("3. Generating Figure: Top 10 Best Sellers")
            order_operation.generate_all_top_10_best_sellers_figure()
            io_op.print_message(
                "The figure for the top 10 best sellers has been generated and saved at "
                "data/figure/generate_all_top_10_best_sellers_figure.png")

            io_op.print_message("4. Generating Figure: Product Categories")
            product_operation.generate_category_figure()
            io_op.print_message(
                "The figure for product categories has been generated and saved at "
                "data/figure/generate_category_figure.png")

            io_op.print_message("5. Generating Figure: Discount Analysis")
            product_operation.generate_discount_figure()
            io_op.print_message(
                "The figure for discount analysis has been generated and saved at "
                "data/figure/generate_discount_figure.png")

            io_op.print_message("6. Generating Figure: Likes Count Analysis")
            product_operation.generate_likes_count_figure()
            io_op.print_message(
                "The figure for likes count analysis has been generated and saved at "
                "data/figure/generate_likes_count_figure.png")

            io_op.print_message("7. Generating Figure: Discount and Likes Count Analysis")
            product_operation.generate_discount_likes_count_figure()
            io_op.print_message(
                "The figure for discount and likes count analysis has been generated and saved at data/figure/generate_discount_likes_count_figure.png")

        elif choice[0] == '7':
            order_operation.delete_all_orders()
            io_op.print_message("All orders data deleted!")
            customer_operation.delete_all_users()
            io_op.print_message("all users data deleted!")

        elif choice[0] == '8':
            cu_id = io_op.get_user_input("Enter the customer ID to be deleted: ", 1)
            customer_operation.delete_customer(cu_id)
            io_op.print_message('Deleting customer- ' + cu_id + ' data...')

        elif choice[0] == '9':
            o_id = io_op.get_user_input("Enter the order ID to be deleted: ", 1)
            order_operation.delete_order(o_id)
            io_op.print_message('Deleting order- ' + o_id + ' data...')

        elif choice[0] == '10':
            p_id = io_op.get_user_input("Enter the product ID to be deleted: ", 1)
            product_operation.delete_product(p_id)
            io_op.print_message('Deleting order- ' + p_id + ' data...')

        elif choice[0] == '11':
            io_op.print_message("Logging out...")
            break

        else:
            io_op.print_message('Please enter a valid input.')


def main():
    io_op = IOOperation()
    io_op.print_message("Welcome to the Abstergo E-Commerce System")
    io_op.print_message(
        "This is a CLI based system  which allows customers to login to the system, perform some shopping operations "
        "like purchasing products, viewing order history and showing user consumption reports")
    io_op.main_menu()
    admin = Admin()
    admin.register_admin()

    while True:
        try:
            user_choice = io_op.get_user_input("Please enter your choice: ", 1)
        # wrong user input check
        except ValueError:
            user_choice = 9

        if user_choice[0] == '1':
            user_name = io_op.get_user_input("Please enter your username: ", 1)
            user_password = io_op.get_user_input("Please enter your password: ", 1)
            uo = UserOperations()
            login_result = uo.login(user_name[0], user_password[0])
            if login_result is None:
                io_op.print_message("Invalid username or password or deactivated.")
                io_op.main_menu()
            # elif login_result is True:
            # # while True:
            #     user_info_role = eval(str(login_result))
            #     user_role = user_info_role['user_role']
            #     if user_role == 'customer':
            #         customer_control(login_result)
            #     elif user_role == 'admin':
            #             admin_control()
            else:
                # Developer testing code
                # io_op.print_message('Unreadable')
                user_info_role = eval(str(login_result))
                user_role = user_info_role['user_role']
                if user_role == 'customer':
                    customer_control(login_result)
                elif user_role == 'admin':
                    admin_control()

        elif user_choice[0] == '2':
            io_op.print_message("Please remember:")
            io_op.print_message(
                "The name should only contain letters or underscores, and its length should be at least 5 characters.")
            io_op.print_message(
                "The password should contain at least one letter (this letter can be either uppercase or lowercase) "
                "and one number.")
            io_op.print_message("The length of the password must be greater than or equal to 5 characters.")

            user_name = io_op.get_user_input("Please enter the username to register for your account: ", 1)
            user_password = io_op.get_user_input("Please enter the new password for your new account: ", 1)
            user_email = io_op.get_user_input("Please enter the email associated with your new account: ", 1)
            user_mobile = io_op.get_user_input("Please enter the mobile number associated with your new account: ", 1)
            register = CustomerOperation()
            cust = register.register_customer(user_name[0], user_password[0], user_email[0], user_mobile[0])
            if cust is True:
                io_op.print_message("You have created a new customer user! You can login now.")
                io_op.main_menu()
            else:
                io_op.print_message("You have given an invalid input, please try again.")
                io_op.main_menu()

        elif user_choice[0] == '3':
            # Log out
            io_op.print_message("Goodbye!")
            break


        else:
            io_op.print_message("\nplease enter a number between 1, 2 or 3")
            io_op.main_menu()


if __name__ == "__main__":
    main()
