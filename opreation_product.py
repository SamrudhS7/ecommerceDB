import os
import pandas as pd
import matplotlib.pyplot as plt
from model_product import Product
import math

class ProductOperations:

    def extract_products_from_files(self):
        product_data = []
        csv_locations = ['data/product/accessories.csv', 'data/product/bags.csv', 'data/product/beauty.csv',
                         'data/product/house.csv', 'data/product/jewelry.csv', 'data/product/kids.csv',
                         'data/product/men.csv', 'data/product/shoes.csv',
                         'data/product/women.csv']
        output_file = "data/products.txt"

        for location in csv_locations:
            df = pd.read_csv(location)
            df_dict = df.to_dict()
            for index, row in df.iterrows():
                # if len(row) == 24:
                # print(row, index)
                product_info = {
                    "pro_id": str(row["id"]),
                    "pro_model": str(row["model"]),
                    "pro_category": str(row["category"]),
                    "pro_name": str(row["name"]),
                    "pro_current_price": str(row["current_price"]),
                    "pro_raw_price": str(row["raw_price"]),
                    "pro_discount": str(row["discount"]),
                    "pro_likes_count": str(row["likes_count"])
                }
                product_data.append(product_info)

        with open(output_file, "w", encoding="utf-8") as file:
            for product_info in product_data:
                file.write(str(product_info) + "\n")
            # file.writelines(product_strings)
            # file.write(str(product_info))
        # print(len(product_data))

    def get_product_list(self, page_number):
        with open('data/products.txt', 'r') as file:
            lines = file.readlines()

        product_list = []
        for line in lines:
            if line.strip() == '':
                continue
            product_info = eval(line.strip())
            product_list.append(product_info)

        total_products = len(product_list)
        total_pages = (total_products // 10) + (1 if total_products % 10 != 0 else 0)

        start_index = (page_number - 1) * 10
        end_index = start_index + 10
        required_products = []

        for i in range(start_index, end_index):
            if i >= total_products:
                break
            product_info = product_list[i]
            product = Product(
                product_info['pro_id'],
                product_info['pro_model'],
                product_info['pro_category'],
                product_info['pro_name'],
                product_info['pro_current_price'],
                product_info['pro_raw_price'],
                product_info['pro_discount'],
                product_info['pro_likes_count']
            )
            required_products.append(product)

        return required_products, page_number, total_pages

    # def delete_product(self, product_id):
    #     df = pd.read_csv("data/products.txt")
    #     print(df.columns)
    #     df = df[df["pro_id"] != product_id]
    #     df.to_csv("data/products.txt", index=False)
    #     return True

    def delete_product(self, product_id):
        with open('data/products.txt', 'r') as file:
            lines = file.readlines()

        with open('data/products.txt', 'w') as file:
            deleted = False
            for line in lines:
                if product_id not in line:
                    file.write(line)
                else:
                    deleted = True

            return deleted


    def get_product_list_by_keyword(self, keyword):
        products = []

        with open('data/products.txt', 'r') as file:
            lines = file.readlines()

            for line in lines:
                if keyword.lower() in line.lower():
                    product_info = eval(line.strip())
                    product = Product(
                        product_info['pro_id'],
                        product_info['pro_model'],
                        product_info['pro_category'],
                        product_info['pro_name'],
                        product_info['pro_current_price'],
                        product_info['pro_raw_price'],
                        product_info['pro_discount'],
                        product_info['pro_likes_count']
                    )
                    products.append(product)

        return products


    def get_product_by_id(self, product_id):
        with open('data/products.txt', 'r') as file:
            lines = file.readlines()

            for line in lines:
                if product_id in line:
                    product_info = eval(line.strip())
                    return Product(
                        product_info['pro_id'],
                        product_info['pro_model'],
                        product_info['pro_category'],
                        product_info['pro_name'],
                        product_info['pro_current_price'],
                        product_info['pro_raw_price'],
                        product_info['pro_discount'],
                        product_info['pro_likes_count']
                    )

        return None


    def generate_category_figure(self):
        categories = {}

        with open('data/products.txt', 'r') as file:
            lines = file.readlines()

            for line in lines:
                product_data = eval(line)  # Parse the product data dictionary using eval
                category = product_data['pro_category']

                if category in categories:
                    categories[category] += 1
                else:
                    categories[category] = 1

        sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
        x = [category[0] for category in sorted_categories]
        y = [category[1] for category in sorted_categories]

        colors = ['lightskyblue', 'deepskyblue', 'dodgerblue', 'royalblue', 'mediumblue',
                  'navy', 'midnightblue', 'steelblue', 'cornflowerblue']

        plt.figure(facecolor='black', figsize=(10,6))
        plt.bar(x, y, color=colors)
        plt.xlabel('Category', color='white')
        plt.ylabel('Number of Products', color='white')
        plt.title('Total Number of Products per Category', color='white')
        plt.xticks(color='white')
        plt.yticks(color='white')
        plt.savefig('data/figure/generate_category_figure.png', facecolor='black')
        plt.close()


    def generate_discount_figure(self):
        discount_ranges = {'<30': 0, '30-60': 0, '>60': 0}

        with open('data/products.txt', 'r') as file:
            lines = file.readlines()

            for line in lines:
                product_data = eval(line)  # Parse the product data dictionary using eval
                discount = product_data['pro_discount']

                if int(discount) < 30:
                    discount_ranges['<30'] += 1
                elif 30 <= int(discount) <= 60:
                    discount_ranges['30-60'] += 1
                else:
                    discount_ranges['>60'] += 1

        labels = list(discount_ranges.keys())
        sizes = list(discount_ranges.values())

        colors = ['salmon', 'indianred', 'firebrick']


    def generate_likes_count_figure(self):
        categories = {}
        with open("data/products.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                try:
                    product = eval(line)
                    category = product['pro_category']
                    likes_count = int(product['pro_likes_count'])

                    if category in categories:
                        categories[category] += likes_count
                    else:
                        categories[category] = likes_count

                except Exception as e:
                    print(f"Error processing product: {line}")
                    print(str(e))

        sorted_categories = sorted(categories.items(), key=lambda x: x[1])
        x = [category[0] for category in sorted_categories]
        y = [category[1] for category in sorted_categories]

        fig, ax = plt.subplots()
        ax.barh(x, y)
        ax.set_xlabel("Sum of Likes Count")
        ax.set_ylabel("Category")
        ax.set_title("Sum of Products' Likes Count per Category")

        plt.tight_layout()
        plt.savefig("data/figure/generate_likes_count_figure.png")
        plt.close()

    def generate_discount_likes_count_figure(self):
        discount = []
        likes_count = []

        with open('data/products.txt', 'r') as file:
            lines = file.readlines()

            for line in lines:
                product_data = eval(line)  # Parse the product data dictionary using eval
                discount.append(float(product_data['pro_discount']))
                likes_count.append(int(product_data['pro_likes_count']))

        plt.scatter(discount, likes_count, c='green', alpha=0.7)
        plt.xlabel('Discount')
        plt.ylabel('Likes Count')
        plt.title('Relationship between Likes Count and Discount')
        plt.savefig('data/figure/generate_discount_likes_count_figure.png')
        plt.close()

    def delete_all_products(self):
        with open('data/products.txt', 'w') as file:
            file.write('')


p1=ProductOperations()
# Test extract_products_from_files method
# p1.extract_products_from_files()

# # Test get_product_list method
# page_number =7499
# products, page_number, total_pages = p1.get_product_list(page_number)
# print(f"Page Number: {page_number}")
# print(f"Total Pages: {total_pages}")
# for product in products:
#     print(product)
#
# # Test delete_product method
# product_id = "1671872"
# result = p1.delete_product(product_id)
# print(f"Product Deletion Result: {result}")
#
# # Test get_product_list_by_keyword method
# keyword = "Chapeau"
# products = p1.get_product_list_by_keyword(keyword)
# print(f"Products with Keyword '{keyword}':")
# for product in products:
#     print(product)
#
# # Test get_product_by_id method
# product_id = "16743784"
# product = p1.get_product_by_id(product_id)
# if product is not None:
#     print(f"Product with ID '{product_id}':")
#     print(product)
# else:
#     print(f"Product with ID '{product_id}' not found.")
#
# # Test generate_category_figure method
# p1.generate_category_figure()
# print("Category figure generated.")
#
# # Test generate_discount_figure method
# p1.generate_discount_figure()
# print("Discount figure generated.")
#
# # Test generate_likes_count_figure method
p1.generate_likes_count_figure()
print("Likes count figure generated.")
#
# # Test generate_discount_likes_count_figure method
# p1.generate_discount_likes_count_figure()
# print("Discount and likes count figure generated.")
#
# # Test delete_all_products method
# p1.delete_all_products()
# print("All products deleted.")
