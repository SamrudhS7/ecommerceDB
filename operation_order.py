import datetime
import os
import random
import string
import time
import pandas as pd
import matplotlib.pyplot as plt


from model_order import Order, User
from operation_customer import CustomerOperation
from operation_user import UserOperations
from model_customer import Customer

class OrderOperation(Order):

    def generate_unique_order_id(self):
        order_id = "o_" + ''.join(random.choices(string.digits, k=5))
        return order_id

    def create_an_order(self, customer_id, product_id, create_time=None):

        if create_time is None:
            create_time = time.strftime("%Y-%m-%d %H:%M:%S")
        order_id = self.generate_unique_order_id()
        order_data=Order(order_id, customer_id, product_id, create_time)
        with open("data/orders.txt", "a") as file:
            file.write(str(order_data) + "\n")
        return True

    def delete_order(self, order_id):
        with open('data/orders.txt', 'r') as file:
            lines = file.readlines()

        with open('data/orders.txt', 'w') as file:
            deleted = False
            for line in lines:
                if order_id not in line:
                    file.write(line)
                else:
                    deleted = True

            return deleted

    def get_order_list(self, customer_id, page_number):
        orders = []
        with open("data/orders.txt", "r") as file:
            for line in file:
                order_data = eval(line.strip())
                order_id = order_data['order_id']
                user_id = order_data['user_id']
                pro_id = order_data['pro_id']
                order_time = order_data['order_time']
                order = Order(order_id, user_id, pro_id, order_time)
                if order.user_id == customer_id:
                    orders.append(order)

        page_size = 10
        total_pages = (len(orders) + page_size - 1) // page_size
        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size
        page_orders = orders[start_index:end_index]

        return page_orders, page_number, total_pages

    def generate_test_order_data(self):
        sets = 'ABCDEFGHIJ'
        customer_op = CustomerOperation()
        user_op = UserOperations()
        for _ in range(10):
            username = 'Customer' + '_' + sets[_]
            password = username + str(_)
            email = username + '@gmail.com'
            phone = '04' + ''.join(random.choice('01234567') for _ in range(10))
            customer_id = user_op.generate_unique_user_id()
            registration_time = "10-05-2022_00:00:00"
            encrypted_password = user_op.encrypt_password(password)
            customer = Customer(customer_id, username, encrypted_password, registration_time, 'customer', email,
                                phone)
            with open("data/users.txt", "a") as file:
                file.write(str(customer) + "\n")

            num_orders = random.randint(50, 200)
            customer_orders = []
            prod_idlist = []
            with open("data/products.txt", "r") as file:
                for line in file:
                    prod_data = eval(line)
                    pro_id = prod_data['pro_id']
                    prod_idlist.append(pro_id)
            for _ in range(num_orders):
                order_id = self.generate_unique_order_id()
                product_id = random.choice(prod_idlist)
                order_time = self.generate_random_time()
                order = Order(order_id, customer_id, product_id, order_time)
                customer_orders.append(str(order))

            with open("data/orders.txt", "a") as file:
                file.write("\n".join(customer_orders) + "\n")

    def generate_random_time(self):
        year = time.localtime().tm_year
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        order_date = f"{day:02d}-{month:02d}-{year:04d}_{hour:02d}:{minute:02d}:{second:02d}"
        return order_date

    def generate_single_customer_consumption_figure(self, customer_id):
        # Retrieve orders for the given customer
        customer_orders = []
        with open('data/orders.txt', 'r') as file:
            for line in file:
                order_info = eval(line.strip())

                order_id = order_info['order_id']
                order_customer_id = order_info['user_id']
                pro_id = order_info['pro_id']
                order_create_time = order_info['order_time']

                if order_customer_id == customer_id:
                    order = Order(order_id, order_customer_id, pro_id, order_create_time)
                    customer_orders.append(order)

        # Retrieve product prices for the orders
        product_prices = {}
        with open('data/products.txt', 'r') as file:
            for line in file:
                product_info = eval(line.strip())

                pro_id = product_info['pro_id']
                pro_current_price = float(product_info['pro_current_price'])

                product_prices[pro_id] = pro_current_price

        # Initialize a dictionary to store the monthly consumption
        monthly_consumption = {month: 0 for month in range(1, 13)}

        # Calculate the sum of order prices for each month
        for order in customer_orders:
            month = int(order.order_time[3:5])
            pro_id = order.pro_id

            if pro_id in product_prices:
                price = product_prices[pro_id]
                monthly_consumption[month] += price

        # Extract the month values and consumption values for plotting
        months = list(monthly_consumption.keys())
        consumption = list(monthly_consumption.values())

        # Create a time series plot
        plt.plot(months, consumption)
        plt.xlabel('Month')
        plt.ylabel('Consumption')
        plt.title('Monthly Consumption for Customer {}'.format(customer_id))
        plt.savefig('data/figure/generate_single_customer_consumption_figure.png')
        plt.show()



    def generate_all_customers_consumption_figure(self):
        # Read the orders data
        with open('data/orders.txt', 'r') as order_file:
            orders = [eval(line.strip()) for line in order_file]

        # Read the products data
        with open('data/products.txt', 'r') as product_file:
            products = [eval(line.strip()) for line in product_file]

        # Create DataFrame from orders data
        orders_df = pd.DataFrame.from_records(orders)

        # Create DataFrame from products data
        products_df = pd.DataFrame.from_records(products)

        # Merge orders and products data on pro_id
        merged_df = pd.merge(orders_df, products_df, on='pro_id')

        # Extract the month from order_time and calculate the monthly consumption
        merged_df['month'] = merged_df['order_time'].str[3:5].astype(int)
        monthly_consumption = merged_df.groupby('month')['pro_current_price'].sum()

        # Create a bar chart
        plt.bar(monthly_consumption.index, monthly_consumption.values)
        plt.xlabel('Month')
        plt.ylabel('Consumption')
        plt.title('Monthly Consumption for All Customers')
        plt.savefig('data/figure/generate_all_customers_consumption_figure.png')


    def generate_all_top_10_best_sellers_figure(self):
        # Read the orders data
        with open('data/orders.txt', 'r') as orders_file:
            orders_data = [eval(line) for line in orders_file]

        # Read the products data
        with open('data/products.txt', 'r') as products_file:
            products_data = [eval(line) for line in products_file]

        dfprods = pd.DataFrame.from_records(products_data)
        dforders = pd.DataFrame.from_records(orders_data)
        dfprods.set_index('pro_id', inplace=True)
        dforders.set_index('order_id', inplace=True)

        dforders.astype({'prod_id': 'str'})
        df_top_10 = dforders.groupby(['pro_id'])['order_id'].count()
        df_top_10 = df_top_10.sort_values(ascending=False).head(10)

        plt.figure(figsize=(10, 6))
        plt.barh([str(index) for index in df_top_10.index.to_list()], df_top_10.values.tolist())

        # Add labels to the bars
        for i, value in enumerate(df_top_10.values.tolist()):
            plt.text(value, i, str(value), ha='left', va='center')

        plt.xlabel("The total sales price")
        plt.ylabel("The Product categories")
        plt.title("Top 10 best sellers")

        # Reverse the y-axis
        plt.gca().invert_yaxis()

        # Adjust spacing between bars
        plt.barh([str(index) for index in df_top_10.index.to_list()], df_top_10.values.tolist(), height=0.6,
                 align='center')

        # Save the figure
        plt.savefig('data/figure/all_top_10_best_sellers_figure.png')

    def generate_all_top_10_best_sellers_figure(self):
        # Read the orders data
        with open('data/orders.txt', 'r') as orders_file:
            orders_data = [eval(line) for line in orders_file]

        # Read the products data
        with open('data/products.txt', 'r') as products_file:
            products_data = [eval(line) for line in products_file]

        df_products = pd.DataFrame.from_records(products_data)
        df_orders = pd.DataFrame.from_records(orders_data)
        df_products.set_index('pro_id', inplace=True)
        df_orders.set_index('order_id', inplace=True)

        df_merged = pd.merge(df_orders, df_products, how='inner', on='pro_id')
        df_top_10 = df_merged.groupby(['pro_category'])['pro_current_price'].sum()
        df_top_10 = df_top_10.sort_values(ascending=False).head(10)

        # print(df_top_10)
        plt.figure(figsize=(20, 10))
        plt.bar(df_top_10.index, df_top_10.values.tolist())
        plt.xlabel("The total sales price")
        plt.ylabel("The Product categories")
        plt.title("Top 10 best sellers")
        # plt.show()
        plt.savefig('data/figure/all_top_10_best_sellers_figure.png')

    def delete_all_orders(self):
        with open('data/orders.txt', 'w') as file:
            file.write('')


order_operation = OrderOperation()

# Generate a unique order ID
# unique_order_id = order_operation.generate_unique_order_id()
# print(unique_order_id)

# Create a new order
# customer_id = "c_001"
# product_id = "p_001"
# create_time = "2023-05-27 10:00:00"
# result = order_operation.create_an_order(customer_id, product_id, create_time)
# print(result)
#
# # Delete an order
# order_id = "o_78869"
# result = order_operation.delete_order(order_id)
# print(result)
#
# # Get a page of orders for a customer
# customer_id = "u_9955337954"
# page_number = 1
# orders, current_page, total_pages = order_operation.get_order_list(customer_id, page_number)

# for order in orders:
#     print(str(orders))
# print(current_page)
# print(total_pages)
# #
# # Generate test order data
# order_operation.generate_test_order_data()
#
# # Generate a consumption figure for a single customer
# customer_id = "u_9729816577"
# order_operation.generate_single_customer_consumption_figure(customer_id)

# # Generate a consumption figure for all customers
# order_operation.generate_all_customers_consumption_figure()
#
# # Generate a consumption figure for all customers

# Generate a figure for the top 10 best-selling products
# order_operation.generate_all_top_10_best_sellers_figure()

# order_operation.generate_single_customer_consumption_figure('u_8009549251')
