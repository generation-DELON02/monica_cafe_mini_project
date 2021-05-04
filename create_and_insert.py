import csv
import os
import pymysql
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
connection = pymysql.connect(
    host,
    user,
    password,
    database
    )
cursor = connection.cursor()


def create_product_table():
    try:
        with connection.cursor() as cursor:
            sql = '''
            CREATE TABLE IF NOT EXISTS products(
                        product_id INT NOT NULL AUTO_INCREMENT,
                        product_name VARCHAR(100) NOT NULL,
                        price FLOAT,
                        PRIMARY KEY(product_id)
                        )'''
            cursor.execute(sql)
            connection.commit() 
    except Exception as e:
        print(e)     


def create_courier_table():
    try:
        with connection.cursor() as cursor:
            sql = '''
            CREATE TABLE IF NOT EXISTS couriers(
                        courier_id INT NOT NULL AUTO_INCREMENT,
                        courier_name VARCHAR(100) NOT NULL,
                        phone VARCHAR(100),
                        PRIMARY KEY(courier_id)
                        )'''
            cursor.execute(sql)
            connection.commit() 
    except Exception as e:
        print(e)     


def create_order_table():
    try:
        with connection.cursor() as cursor:
            sql = '''
            CREATE TABLE IF NOT EXISTS orders(
                        order_id INT NOT NULL AUTO_INCREMENT,
                        customer_name VARCHAR(100) NOT NULL,
                        customer_address VARCHAR(100) NOT NULL,
                        customer_phone VARCHAR(100) NOT NULL,
                        courier INT,
                        status VARCHAR(100) NOT NULL,
                        items VARCHAR(100) NOT NULL,
                        PRIMARY KEY(order_id)
                        )'''
            cursor.execute(sql)
            connection.commit() 
    except Exception as e:
        print(e)     


def insert_into_product_table():
    list_of_products = []
    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\product_dictionary.csv", "r") as file:
        csv_file = csv.DictReader(file)
        for product in csv_file:
            list_of_products.append(product)
    
    try:
        for row in list_of_products:
            cursor.execute("INSERT INTO products (product_name, price) VALUES (%s, %s)",(row['product_name'], row['price']))
            connection.commit()
    except Exception as e:
        print("exception!!", e)


def insert_into_courier_table():
    list_of_couriers = []
    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\courier_dictionary.csv", "r") as file:
        csv_file = csv.DictReader(file)
        for courier in csv_file:
            list_of_couriers.append(courier)
    
    try:
        for row in list_of_couriers:
            cursor.execute("INSERT INTO couriers (courier_name, phone) VALUES (%s, %s)",(row['courier_name'], row['phone']))
            connection.commit()
    except Exception as e:
        print("exception!!", e)


def insert_into_order_table():
    list_of_orders = []
    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\order_dictionary.csv", "r") as file:
        csv_file = csv.DictReader(file, delimiter=",", quotechar='"', skipinitialspace=True)
        for courier in csv_file:
            list_of_orders.append(courier)
    
    try:
        for row in list_of_orders:
            cursor.execute("INSERT INTO orders (customer_name, customer_address, customer_phone, courier, status, items) VALUES (%s, %s, %s, %s, %s, %s)",(row['customer_name'], row['customer_address'], row['customer_phone'], row['courier'], row['status'], row['items']))
            connection.commit()
    except Exception as e:
        print("exception!!", e)


create_product_table()
create_courier_table()
create_order_table()
print("Your tables have been created successfully!")

insert_into_product_table()
insert_into_courier_table()
insert_into_order_table()
print("The data from the CSV files have been inserted into the tables successfully!")
