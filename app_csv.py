import csv
import sys
import os

def load_product_list():
    list_of_products = []
    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\product_dictionary.csv", "r") as file:
        csv_file = csv.DictReader(file)
        for product in csv_file:
            list_of_products.append(product)
        return list_of_products

def load_courier_list():
    list_of_couriers = []
    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\courier_dictionary.csv", "r") as file:
        csv_file = csv.DictReader(file)
        for courier in csv_file:
            list_of_couriers.append(courier)
        return list_of_couriers

def load_order_list():
    list_of_orders = []
    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\order_dictionary.csv", "r") as file:
        csv_file = csv.DictReader(file, delimiter=",", quotechar='"', skipinitialspace=True)
        for courier in csv_file:
            list_of_orders.append(courier)
        return list_of_orders
# PUT EVERYTHING IN A TRY BLOCK INTO A FUNCTION? https://realpython.com/python-exceptions/#the-try-and-except-block-handling-exceptions

def main_menu():
    load_product_list()
    load_courier_list()
    load_order_list()
    print("Main Menu:")
    try:
        start = input("What would you like to do?\n"
                        "Press 1 to show Product Menu\n"
                        "Press 2 to show Courier Menu\n"
                        "Press 3 to show Order Menu\n"
                        "Press 0 to close app\n")
        while True:
            if int(start) == 1:
                return product_menu()
            elif int(start) == 2:
                return courier_menu()
            elif int(start) == 3:
                return order_menu()
            elif int(start) == 0:
                print("Okay. Closing the app. Byee")
                break
            else:
                start = input("Uh oh! That's not in the list. Please try again:\n"
                                "Press 1 to show Product Menu\n"
                                "Press 2 to show Courier Menu\n"
                                "Press 3 to show Order Menu\n"
                                "Press 0 to close app\n")
    except ValueError:
        print("Whoops! Please enter a number.")
        main_menu()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)
    finally:
        return sys.exit()

def product_menu():
    print("Product Menu:")
    try:
        options = input("Press 0 to return to Main Menu\n"
                        "Press 1 to display the list of current products\n"
                        "Press 2 to create a new product\n"
                        "Press 3 to update a product\n"
                        "Press 4 to delete a product\n")
        while True:
            if int(options) == 0:
                return return_to_main_menu()
            elif int(options) == 1:
                return display_list_of_products()
            elif int(options) == 2:
                return create_new_product()
            elif int(options) == 3:
                return update_product()
            elif int(options) == 4:
                return delete_a_product()
            else:
                options = input("Whoops! That number isn't in the list. Please enter again:\n"
                                "Press 0 to return to Main Menu\n"
                                "Press 1 to display the list of current products\n"
                                "Press 2 to create a new product\n"
                                "Press 3 to update a product\n"
                                "Press 4 to delete a product\n")
    except ValueError:
        print("Whoops! Please enter a number.")
        return product_menu()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)
            
def return_to_main_menu():
    print("Returning to Main Menu")
    return main_menu()

def print_product_list_line_by_line():
    for product in load_product_list():
        print(product) 

def display_list_of_products():
    print("Here is the list of products:")
    print_product_list_line_by_line()
    while True:
        finished_looking = input("Have you finished looking?\nPress 1 for Yes\nPress 2 for No\n")
        if finished_looking == "1":
            break
        elif finished_looking == "2":
            print("Okay, take your time!")
            print_product_list_line_by_line()
        else:
            print("Invalid input. Please enter again.")
    return product_menu()

def append_product_to_csv(new_product, new_price):
    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\product_dictionary.csv", "a") as file:
        fieldnames = ["product_name", "price"]
        writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator='\n')
        writer.writerow({"product_name": new_product, "price": new_price})

def create_new_product():
    print("Create New Product:")
    return create_new_product2()

def create_new_product2():
    print_product_list_line_by_line()
    new_product = input("What product would you like to add?\n"
                        "You can press 0 to go back.\n").title()
    if new_product == "0":
        print("Okay! Returning to Product Menu")
        return product_menu()
    else:
        new_price = input("What is the price of this product?\n")
        append_product_to_csv(new_product, new_price)
        print("You have successfully added {} to the list!".format(new_product))
        print(load_product_list())
        return create_another_product()

def continue_adding_prompt():
    continue_adding = input("Would you like to add anything else?\nPress 1 for Yes\nPress 2 for No\n")
    return continue_adding

def continue_adding_result():
    if continue_adding_prompt() == "1":
        return create_new_product2()
    elif continue_adding_prompt() == "2":
        return product_menu()
    else:
        print("Sorry, that wasn't an option.")
        return continue_adding_result()

def create_another_product():
    return continue_adding_result()

def convert_load_list_to_dictionary(objects):
    objects_to_print = {}
    line_num = 1
    for an_object in objects:
        objects_to_print[line_num] = an_object
        line_num += 1
    return objects_to_print

def product_dict():
    return convert_load_list_to_dictionary(load_product_list())

def courier_dict():
    return convert_load_list_to_dictionary(load_courier_list())

def order_dict():
    return convert_load_list_to_dictionary(load_order_list())

def print_object_dictionary_line_by_line(object_dict):
    for key, value in object_dict.items():
        print("{}: {}".format(key, value))

def update_product():
    print("Update A Product:")
    return update_product2()
    
def update_product2():
    product_dict()
    print_object_dictionary_line_by_line(product_dict())
    try:
        change_product = int(input("What product would you like to update?\nYou can press 0 to go back\n"))
        while True:
            if change_product == 0:
                break
            elif change_product in product_dict().keys():
                print("To update a product or price, enter what you would like to change it to. Or leave blank to skip:")
                new_product = input("Current product: {}\nReplace with: ".format(product_dict()[change_product]["product_name"])).title()
                if new_product == "":
                    new_product = product_dict()[change_product]["product_name"]
                else:
                    product_dict()[change_product]["product_name"] = new_product
                new_price = input("Current price: {}\nReplace with: ".format(product_dict()[change_product]["price"]))
                if new_price == "":
                    new_price = product_dict()[change_product]["price"]
                else:
                    product_dict()[change_product]["price"] = new_price
                with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\product_dictionary.csv", "r") as file:
                    reader = csv.reader(file.readlines())
                with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\product_dictionary.csv", "w") as f:
                    writer = csv.writer(f, lineterminator='\n')
                    for i, line in enumerate(reader, 0):
                        if i == change_product:
                            writer.writerow([new_product, new_price])
                        else:
                            writer.writerow(line)
                print(product_dict())
                print("You have successfully updated number {}:\nProduct name: {}. Price: {}".format(change_product, product_dict()[change_product]["product_name"], product_dict()[change_product]["price"]))
                return update_another_product()
            else:
                change_product = int(input("Sorry, that isn't in the list. Please enter again\n"))
        return product_menu()
    except ValueError:
        print("Oops! Please input a number.")
        return update_product()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)

def change_product_prompt():
    change_product = input("Would you like to update anything else?\nPress 1 for Yes\nPress 2 for No\n")
    return change_product

def change_product_result():
    if change_product_prompt() == "1":
        return update_product2()
    elif change_product_prompt() == "2":
        return product_menu()
    else:
        print("Sorry, that wasn't an option.")
        return change_product_result()

def update_another_product():
    return change_product_result()

def delete_a_product():
    print("Delete A Product:")
    return delete_a_product2()

def delete_a_product2():
    product_dict()
    print_object_dictionary_line_by_line(product_dict())
    try:
        delete_product = int(input("What product would you like to delete?\nYou can press 0 to go back\n"))
        while True:
            if delete_product == 0:
                break
            elif delete_product in product_dict().keys():
                confirm = int(input("Are you sure you want to delete {}?\nPress 1 for Yes\nPress 2 to cancel\n".format(product_dict()[delete_product])))
                if confirm == 1:
                    print("You've successfully deleted {} from the list!".format(product_dict()[delete_product]["product_name"]))
                    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\product_dictionary.csv", "r") as file:
                        reader = csv.reader(file.readlines())
                    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\product_dictionary.csv", "w") as f:
                        writer = csv.writer(f, lineterminator='\n')
                        for i, line in enumerate(reader, 0):
                            if i != delete_product:
                                writer.writerow(line)
                    print_object_dictionary_line_by_line(product_dict())
                    return delete_another_product()
                else:
                    print("Okay, cancelled!")
                    return delete_a_product()
            else:
                delete_product = int(input("Sorry, that isn't in the list. Please enter again\n"))
        return product_menu()
    except ValueError:
        print(product_dict())
        print("Oops! Please input a number.")
        return delete_a_product()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)

def delete_a_product_prompt():
    delete_again = int(input("Would you like to delete anything else?\nPress 1 for Yes\nPress 2 for No\n"))
    return delete_again

def delete_a_product_result():
    if change_product_prompt() == "1":
        return update_product2()
    elif change_product_prompt() == "2":
        return product_menu()
    else:
        print("Sorry, that wasn't an option.")
        return change_product_result()

def delete_another_product():
    product_dict()
    try:
        while True:
            delete_again = int(input("Would you like to delete anything else?\nPress 1 for Yes\nPress 2 for No\n"))
            if delete_again == 1:
                print(product_dict())
                delete_product = int(input("What product would you like to delete?\n"))
                if delete_product in product_dict().keys():
                    confirm = int(input("Are you sure you want to delete {}?\nPress 1 for Yes\nPress 2 to cancel\n".format(product_dict()[delete_product])))
                    if confirm == 1:
                        print("You've successfully deleted {} from the list!".format(product_dict()[delete_product]["product_name"]))
                        with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\product_dictionary.csv", "r") as file:
                            reader = csv.reader(file.readlines())
                        with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\product_dictionary.csv", "w") as f:
                            writer = csv.writer(f, lineterminator='\n')
                            for i, line in enumerate(reader, 0):
                                if i != delete_product:
                                    writer.writerow(line)
                        print_object_dictionary_line_by_line(product_dict())
                    else:
                        print("Okay, cancelled!")
                else:
                    print("Sorry, that isn't in the list.")
            elif delete_again == 2:
                print("Okay, thank you")
                break
            else:
                print("Sorry, that isn't an option")
        return product_menu()
    except ValueError:
        print("Oops! Please input a number.")
        return delete_another_product()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)
        
def courier_menu():
    print("Courier Menu:")
    try:
        options = input("Press 0 to return to Main Menu\n"
                        "Press 1 to display the list of current couriers\n"
                        "Press 2 to add a new courier\n"
                        "Press 3 to update a courier\n"
                        "Press 4 to delete a courier\n")
        while True:
            if int(options) == 0:
                return return_to_main_menu()
            elif int(options) == 1:
                return display_list_of_couriers()
            elif int(options) == 2:
                return create_new_courier()
            elif int(options) == 3:
                return update_courier()
            elif int(options) == 4:
                return delete_a_courier()
            else:
                options = input("Whoops! That number isn't in the list. Please enter again:\n"
                                "Press 0 to return to Main Menu\n"
                                "Press 1 to display the list of current courier\n"
                                "Press 2 to add a new courier\n"
                                "Press 3 to update a courier\n"
                                "Press 4 to delete a courier\n")
    except ValueError:
        print("Oops! Please input a number.")
        return courier_menu()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)

def print_courier_list_line_by_line():
    for courier in load_courier_list():
        print(courier) 

def display_list_of_couriers():
    print("Here is the list of couriers:")
    print_courier_list_line_by_line()
    while True:
        finished_looking = input("Have you finished looking?\nPress 1 for Yes\nPress 2 for No\n")
        if finished_looking == "1":
            break
        elif finished_looking == "2":
            print("Okay, take your time!")
            print_courier_list_line_by_line()
        else:
            print("Invalid input. Please enter again.")
    return courier_menu() 

def append_courier_to_csv(new_courier, new_phone):
    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\courier_dictionary.csv", "a") as file:
            fieldnames = ["courier_name", "phone"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator='\n')
            writer.writerow({"courier_name": new_courier, "phone": new_phone})

def create_new_courier():
    print("Add New Courier:")
    print(load_courier_list())
    new_courier = input("What courier would you like to add?\n"
                        "You can press 0 to go back.\n").title()
    if new_courier == "0":
        print("Okay! Returning to Courier Menu")
        return courier_menu()
    else:
        new_phone = input("What is their phone number?\n")
        append_courier_to_csv(new_courier, new_phone)
        print("You have successfully added {} to the list!".format(new_courier))
        print(load_courier_list())
        return create_another_courier()

def create_another_courier():
    while True:
        continue_adding = input("Would you like to add anyone else?\nPress 1 for Yes\nPress 2 for No\n")
        if continue_adding == "1":
            new_courier = input("Okay! What courier would you like to add?\n").title()
            new_phone = input("What is their phone number?\n")
            append_courier_to_csv(new_courier, new_phone)
            print("You have successfully added {} to the list!".format(new_courier))
            print(load_courier_list())
        elif continue_adding == "2":
            print("Okay. All done!")
            break
        else:
            print("Sorry, that wasn't an option. Please enter again.")
    return courier_menu()

def update_courier(): #if both inputs are empty, say okay, nothing has been updated
    print("Update A Courier:")
    courier_dict()
    print_object_dictionary_line_by_line(courier_dict())
    try:
        change_courier = int(input("What courier would you like to update?\nYou can press 0 to go back\n"))
        while True:
            if change_courier == 0:
                break
            elif change_courier in courier_dict().keys():
                print("To update a courier or phone number, enter what you would like to change it to. Or leave blank to skip:")
                new_courier = input("Current courier: {}\nReplace with: ".format(courier_dict()[change_courier]["courier_name"])).title()
                if new_courier == "":
                    new_courier = courier_dict()[change_courier]["courier_name"]
                else:
                    courier_dict()[change_courier]["courier_name"] = new_courier
                new_phone = input("Current phone number: {}\nReplace with: ".format(courier_dict()[change_courier]["phone"]))
                if new_phone == "":
                    new_phone = courier_dict()[change_courier]["phone"]
                else:
                    courier_dict()[change_courier]["phone"] = new_phone
                print("You have successfully updated number {}:\nCourier name: {}. Phone: {}".format(change_courier, courier_dict()[change_courier]["courier_name"], courier_dict()[change_courier]["phone"]))
                with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\courier_dictionary.csv", "r") as file:
                    reader = csv.reader(file.readlines())
                with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\courier_dictionary.csv", "w") as f:
                    writer = csv.writer(f, lineterminator='\n')
                    for i, line in enumerate(reader, 0):
                        if i == change_courier:
                            writer.writerow([new_courier, new_phone])
                        else:
                            writer.writerow(line)
                print(courier_dict())
                return update_another_courier()
            else:
                change_courier = int(input("Sorry, they aren't in the list. Please enter again\n"))
        return courier_menu()
    except ValueError:
        print("Oops! Please input a number.")
        return update_courier()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)

def update_another_courier():
    courier_dict()
    try:
        while True:
            another_update = int(input("Would you like to update anyone else?\nPress 1 for Yes\nPress 2 for No\n"))
            if another_update == 1:
                print(courier_dict())
                change_courier = int(input("What courier would you like to update?\n"))
                if change_courier in courier_dict().keys():
                    new_courier = input("Current courier: {}\nReplace with: ".format(courier_dict()[change_courier]["courier_name"])).title()
                    if new_courier == "":
                        new_courier = courier_dict()[change_courier]["courier_name"]
                    else:
                        courier_dict()[change_courier]["courier_name"] = new_courier
                    new_phone = input("Current phone number: {}\nReplace with: ".format(courier_dict()[change_courier]["phone"]))
                    if new_phone == "":
                        new_phone = courier_dict()[change_courier]["phone"]
                    else:
                        courier_dict()[change_courier]["phone"] = new_phone
                    print("You have successfully updated number {}:\nCourier name: {}. Phone: {}".format(change_courier, courier_dict()[change_courier]["courier_name"], courier_dict()[change_courier]["phone"]))
                    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\courier_dictionary.csv", "r") as file:
                        reader = csv.reader(file.readlines())
                    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\courier_dictionary.csv", "w") as f:
                        writer = csv.writer(f, lineterminator='\n')
                        for i, line in enumerate(reader, 0):
                            if i == change_courier:
                                writer.writerow([new_courier, new_phone])
                            else:
                                writer.writerow(line)
                    print(courier_dict())
                else:
                    print("Sorry, that isn't in the list.\n")
                    print(courier_dict())
            elif another_update == 2:
                print("Okay, thank you")
                break
            else:
                print(courier_dict())
                print("Sorry, that isn't an option")
        return courier_menu()
    except ValueError:
        print("Oops! Please input a number.")
        print(courier_dict())
        return update_another_courier()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)
        
def delete_a_courier():
    courier_dict()
    print_object_dictionary_line_by_line(courier_dict())
    try:
        delete_courier = int(input("Which courier would you like to delete?\nYou can press 0 to go back\n"))
        while True:
            if delete_courier == 0:
                break
            elif delete_courier in courier_dict().keys():
                confirm = int(input("Are you sure you want to delete {}?\nPress 1 for Yes\nPress 2 to cancel\n".format(courier_dict()[delete_courier])))
                if confirm == 1:
                    print("You've successfully deleted {} from the list!".format(courier_dict()[delete_courier]["courier_name"]))
                    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\courier_dictionary.csv", "r") as file:
                        reader = csv.reader(file.readlines())
                    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\courier_dictionary.csv", "w") as f:
                        writer = csv.writer(f, lineterminator='\n')
                        for i, line in enumerate(reader, 0):
                            if i != delete_courier:
                                writer.writerow(line)
                    print_object_dictionary_line_by_line(courier_dict())
                    return delete_another_courier()
                else:
                    print("Okay, cancelled!")
                    return delete_a_courier()
            else:
                delete_courier = int(input("Sorry, they aren't in the list. Please enter again\n"))
        return courier_menu()
    except ValueError:
        print(courier_dict())
        print("Oops! Please input a number.")
        return delete_a_courier()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)
        
def delete_another_courier():
    courier_dict()
    try:
        while True:
            delete_again = int(input("Would you like to delete anyone else?\nPress 1 for Yes\nPress 2 for No\n"))
            if delete_again == 1:
                print(courier_dict())
                delete_courier = int(input("What courier would you like to delete?\n"))
                if delete_courier in courier_dict().keys():
                    confirm = int(input("Are you sure you want to delete {}?\nPress 1 for Yes\nPress 2 to cancel\n".format(courier_dict()[delete_courier])))
                    if confirm == 1:
                        print("You've successfully deleted {} from the list!".format(courier_dict()[delete_courier]["courier_name"]))
                        with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\courier_dictionary.csv", "r") as file:
                            reader = csv.reader(file.readlines())
                        with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\courier_dictionary.csv", "w") as f:
                            writer = csv.writer(f, lineterminator='\n')
                            for i, line in enumerate(reader, 0):
                                if i != delete_courier:
                                    writer.writerow(line)
                        print_object_dictionary_line_by_line(courier_dict())
                        return delete_another_courier()
                    else:
                        print("Okay, cancelled!")
                        return delete_another_courier()
                else:
                    print("Sorry, they aren't in the list")
                    print(courier_dict())
            elif delete_again == 2:
                print("Okay, thank you")
                break
            else:
                print("Sorry, that isn't an option")
                print(courier_dict())
        return courier_menu()
    except ValueError:
        print(courier_dict())
        print("Oops! Please input a number.")
        return delete_another_courier()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)

def order_menu():
    print("Order Menu:")
    try:
        options = input("Press 0 to return to Main Menu\n"
                        "Press 1 to display the list of current orders\n"
                        "Press 2 to create a new order\n"
                        "Press 3 to update the status of an order\n"
                        "Press 4 to update an order\n"
                        "Press 5 to delete an order\n")
        while True:
            if int(options) == 0:
                return return_to_main_menu()
            elif int(options) == 1:
                return display_list_of_orders()
            elif int(options) == 2:
                return create_new_order()
            elif int(options) == 3:
                return update_order_status()
            elif int(options) == 4:
                return update_order()
            elif int(options) == 5:
                return delete_an_order()
            else:
                options = input("Whoops! That number isn't in the list. Please enter again:\n"
                                "Press 0 to return to Main Menu\n"
                                "Press 1 to display the list of current orders\n"
                                "Press 2 to create a new order\n"
                                "Press 3 to update the status of an order\n"
                                "Press 4 to update an order\n"
                                "Press 5 to delete an order\n")
    except ValueError:
        print("Oops! Please enter a number.")
        return order_menu()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)

def print_order_list_line_by_line():
    for order in load_order_list():
        print(order) 

def display_list_of_orders():
    print("Here is the list of orders:")
    print_order_list_line_by_line()
    while True:
        finished_looking = input("Have you finished looking?\nPress 1 for Yes\nPress 2 for No\n")
        if finished_looking == "1":
            break
        elif finished_looking == "2":
            print("Okay, take your time!")
            print_order_list_line_by_line()
        else:
            print("Invalid input. Please enter again.")
    return order_menu()

def append_order_to_csv(new_name, new_address, new_phone, order_courier, order_status, order_products):
    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\order_dictionary.csv", "a") as file:
            fieldnames = ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator='\n')
            writer.writerow({"customer_name": new_name, "customer_address": new_address, "customer_phone": new_phone, "courier": order_courier, "status": order_status, "items": order_products})

def create_new_order():
    print("Create A New Order:")
    product_dict()
    courier_dict()
    print_object_dictionary_line_by_line(order_dict())
    new_name = input("What is the name of the customer would you like to add?\nYou can press 0 to go back.\n").title()
    if new_name == "0":
        print("Okay! Returning to Order Menu")
        return order_menu()
    else:
        new_address = input("What is their address?\n").title() #maybe first line, second, city, post code?
        new_phone = input("What is their number?\n")
        print_object_dictionary_line_by_line(product_dict())
        print("Please select the customer's chosen products from the list. Press 0 when done.")
        order_products = []
        choose_products = input("Product number: ")
        while choose_products != "0":
            order_products.append(choose_products)
            print(order_products)
            choose_products = input("Product number: ")
        print(order_products)
        print_object_dictionary_line_by_line(courier_dict())
        order_courier = input("Please select a courier\n")
        order_status = "Preparing"
        append_order_to_csv(new_name, new_address, new_phone, order_courier, order_status, order_products)
        print("Successfully created the order for {}!".format(new_name))
        print_object_dictionary_line_by_line(order_dict())
        return create_another_order()

def create_another_order():
    product_dict()
    courier_dict()
    while True:
        continue_adding = input("Would you like to add anything else?\nPress 1 for Yes\nPress 2 for No\n")
        if continue_adding == "1":
            new_name = input("Okay! What is the name of the customer would you like to add?\n").title()
            new_address = input("What is their address?\n").title()
            new_phone = input("What is their number?\n")
            print_object_dictionary_line_by_line(product_dict())
            print("Please select the customer's chosen products from the list. Press 0 when done.")
            order_products = []
            choose_products = input("Product number: ")
            while choose_products != "0":
                order_products.append(choose_products)
                print(order_products)
                choose_products = input("Product number: ")
            print(order_products)
            print_object_dictionary_line_by_line(courier_dict())
            order_courier = input("Please select a courier\n") #oops that's not in the list??????
            order_status = "Preparing"
            append_order_to_csv(new_name, new_address, new_phone, order_courier, order_status, order_products)
            print("Successfully created the order for {}!".format(new_name))
            print_object_dictionary_line_by_line(order_dict())
            return create_another_order()
        elif continue_adding == "2":
            print("Okay! Returning to Order Menu")
            break
        else:
            print("Sorry, that wasn't an option.")
            return create_another_order()
    return order_menu()

def update_order_status():
    print("Update Order Status:")
    products_to_print = {}
    line_num = 1
    for order in load_order_list():
        products_to_print[line_num] = order
        line_num += 1
    for key, value in products_to_print.items():
        print("{}: {}".format(key, value))
    try:
        while True:
            change_status = int(input("Which order would you like to update the status of?\nYou can press 0 to go back\n"))
            if change_status == 0:
                break
            elif change_status in products_to_print.keys():
                new_status = int(input("What would you like to change the status to?\n"
                                    "Press 1 for Preparing\nPress 2 for Out-For-Delivery\nPress 3 for Delivered\n"))
                if new_status == 1:
                    new_status = "Preparing"
                    products_to_print[change_status]["status"] = new_status
                elif new_status == 2:
                    new_status = "Out-For-Delivery"
                    products_to_print[change_status]["status"] = new_status
                elif new_status == 3:
                    new_status = "Delivered"
                    products_to_print[change_status]["status"] = new_status
                else:
                    print("Sorry, that wasn't an option")
                    return update_order_status()
                with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\order_dictionary.csv", "r") as file:
                    reader = csv.reader(file.readlines())
                with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\order_dictionary.csv", "w") as f:
                    writer = csv.writer(f, lineterminator='\n')
                    for i, line in enumerate(reader, 0):
                        if i == change_status:
                            writer.writerow([products_to_print[change_status]["customer_name"], products_to_print[change_status]["customer_address"], products_to_print[change_status]["customer_phone"], products_to_print[change_status]["courier"], new_status, products_to_print[change_status]["items"]])
                        else:
                            writer.writerow(line)
                print("You have successfully updated the order status from {} to {}!".format(products_to_print[change_status]["status"], new_status))
                print(load_order_list())
                return update_another_order_status()
            else:
                print("Sorry, that isn't in the list.")
        return order_menu()
    except ValueError:
        print("Oops! Please input a number.")
        return update_order_status()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)

def update_another_order_status():
    products_to_print = {}
    line_num = 1
    for order in load_order_list():
        products_to_print[line_num] = order
        line_num += 1
    try:
        while True:
            another_update = int(input("Would you like to update another status?\nPress 1 for Yes\nPress 2 for No\n"))
            if another_update == 1:
                for key, value in products_to_print.items():
                    print(key, value)
                change_status = int(input("What would you like to update the status of?\n"))
                if change_status in products_to_print.keys():
                    new_status = int(input("What would you like to change the status to?\n"
                                    "Press 1 for Preparing\nPress 2 for Out-For-Delivery\nPress 3 for Delivered\n"))
                    if new_status == 1:
                        new_status = "Preparing"
                        products_to_print[change_status]["status"] = new_status
                    elif new_status == 2:
                        new_status = "Out-For-Delivery"
                        products_to_print[change_status]["status"] = new_status
                    elif new_status == 3:
                        new_status = "Delivered"
                        products_to_print[change_status]["status"] = new_status
                    else:
                        print("Sorry, that wasn't an option")
                        return update_another_order_status()
                    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\order_dictionary.csv", "r") as file:
                        reader = csv.reader(file.readlines())
                    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\order_dictionary.csv", "w") as f:
                        writer = csv.writer(f, lineterminator='\n')
                        for i, line in enumerate(reader, 0):
                            if i == change_status:
                                writer.writerow([products_to_print[change_status]["customer_name"], products_to_print[change_status]["customer_address"], products_to_print[change_status]["customer_phone"], products_to_print[change_status]["courier"], new_status, products_to_print[change_status]["items"]])
                            else:
                                writer.writerow(line)
                    print("You have successfully updated the order status from {} to {}!".format(products_to_print[change_status]["status"], new_status))
                    print(load_order_list())
                    return update_another_order_status()
                else:
                    print("Sorry, that isn't in the list.")
                    return update_another_order_status()
            elif another_update == 2:
                print("Okay, thank you")
                break
            else:
                for key, value in products_to_print.items():
                    print(key, value)
                print("Sorry, that isn't an option")
        return order_menu()
    except ValueError:
        for key, value in products_to_print.items():
            print(key, value)
        print("Oops! Please input a number.")
        return update_another_order_status()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)

def update_order():
    print("Update An Order:")
    order_dict()
    courier_dict()
    product_dict()
    print_object_dictionary_line_by_line(order_dict())
    try:
        while True:
            choose_update_order = int(input("Which order would you like to update?\nYou can press 0 to go back\n"))
            if choose_update_order == 0:
                return order_menu()
            elif choose_update_order in order_dict().keys():
                print("Please update the property, or leave blank to skip:")
                replace_name = input("Current customer name: {}\nReplace with: ".format(order_dict()[choose_update_order]["customer_name"])).title()
                if replace_name == "":
                    replace_name = order_dict()[choose_update_order]["customer_name"]
                else:
                    order_dict()[choose_update_order]["customer_name"] = replace_name
                replace_address = input("Current customer address: {}\nReplace with: ".format(order_dict()[choose_update_order]["customer_address"]))
                if replace_address == "":
                    replace_address = order_dict()[choose_update_order]["customer_address"]
                else:
                    order_dict()[choose_update_order]["customer_address"] = replace_address
                replace_phone = input("Current phone number: {}\nReplace with: ".format(order_dict()[choose_update_order]["customer_phone"]))
                if replace_phone == "":
                    replace_phone = order_dict()[choose_update_order]["customer_phone"]
                else:
                    order_dict()[choose_update_order]["customer_phone"] = replace_phone
                print(courier_dict())
                replace_courier = input("Current courier: {}\nReplace with: ".format(order_dict()[choose_update_order]["courier"]))
                if replace_courier == "":
                    replace_courier = order_dict()[choose_update_order]["courier"]
                else:
                    order_dict()[choose_update_order]["courier"] = replace_courier
                replace_status = input("What would you like to change the status to?\n"
                                    "Press 1 for Preparing\nPress 2 for Out-For-Delivery\nPress 3 for Delivered\n"
                                    "Current status: {}\nEnter here: ".format(order_dict()[choose_update_order]["status"]))
                if replace_status == "":
                    replace_status = order_dict()[choose_update_order]["status"]
                elif replace_status == "1": #make into a function or loop
                    replace_status = "Preparing"
                    order_dict()[choose_update_order]["status"] = replace_status
                elif replace_status == "2":
                    replace_status = "Out-For-Delivery"
                    order_dict()[choose_update_order]["status"] = replace_status
                elif replace_status == "3":
                    replace_status = "Delivered"
                    order_dict()[choose_update_order]["status"] = replace_status
                else:
                    print("Sorry, that wasn't an option")
                    #return update_order_status()
                print(product_dict())
                replacement_products_list = []
                replace_items = input("Current products: {}\nNew product: ".format(order_dict()[choose_update_order]["items"]))
                if replace_items == "":
                    replace_items = order_dict()[choose_update_order]["items"]
                    replacement_products_list = order_dict()[choose_update_order]["items"]
                else:
                    while replace_items != "0":
                        replacement_products_list.append(replace_items)
                        print("Current list: {}".format(replacement_products_list))
                        replace_items = input("New product: ")
                    order_dict()[choose_update_order]["items"] = replacement_products_list
                    print(replacement_products_list)
                print(order_dict()[choose_update_order])
                with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\order_dictionary.csv", "r") as file:
                    reader = csv.reader(file.readlines())
                with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\order_dictionary.csv", "w") as f:
                    writer = csv.writer(f, lineterminator='\n')
                    for i, line in enumerate(reader, 0):
                        if i == choose_update_order:
                            writer.writerow([replace_name, replace_address, replace_phone, replace_courier, replace_status, replacement_products_list])
                        else:
                            writer.writerow(line)
                return update_another_order()
            else:
                print("Sorry, that isn't in the list. Please enter again")
                return update_order()
    except ValueError:
        print("Oops! Please input a number.")
        return update_order()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)
    
def update_another_order():
    orders_to_print = {}
    line_num = 1
    for order in load_order_list():
        orders_to_print[line_num] = order
        line_num += 1
    couriers_to_print = {}
    line_num = 1
    for courier in load_courier_list():
        couriers_to_print[line_num] = courier
        line_num += 1
    products_to_print = {}
    line_num = 1
    for product in load_product_list():
        products_to_print[line_num] = product
        line_num += 1
    try:
        another_order_update = int(input("Would you like to update another order?\nPress 1 for Yes\nPress 2 for No\n"))
        if another_order_update == 1:
            for key, value in orders_to_print.items():
                print(key, value)
            choose_update_order = int(input("Which order would you like to update?\n"))
            if choose_update_order in orders_to_print.keys():
                print("Please update the property, or leave blank to skip:")
                replace_name = input("Current customer name: {}\nReplace with: ".format(orders_to_print[choose_update_order]["customer_name"])).title()
                if replace_name == "":
                    replace_name = orders_to_print[choose_update_order]["customer_name"]
                else:
                    orders_to_print[choose_update_order]["customer_name"] = replace_name
                replace_address = input("Current customer address: {}\nReplace with: ".format(orders_to_print[choose_update_order]["customer_address"]))
                if replace_address == "":
                    replace_address = orders_to_print[choose_update_order]["customer_address"]
                else:
                    orders_to_print[choose_update_order]["customer_address"] = replace_address
                replace_phone = input("Current phone number: {}\nReplace with: ".format(orders_to_print[choose_update_order]["customer_phone"]))
                if replace_phone == "":
                    replace_phone = orders_to_print[choose_update_order]["customer_phone"]
                else:
                    orders_to_print[choose_update_order]["customer_phone"] = replace_phone
                print(couriers_to_print)
                replace_courier = input("Current courier: {}\nReplace with: ".format(orders_to_print[choose_update_order]["courier"]))
                if replace_courier == "":
                    replace_courier = orders_to_print[choose_update_order]["courier"]
                else:
                    orders_to_print[choose_update_order]["courier"] = replace_courier
                replace_status = input("What would you like to change the status to?\n"
                                    "Press 1 for Preparing\nPress 2 for Out-For-Delivery\nPress 3 for Delivered\n"
                                    "Current status: {}\nEnter here: ".format(orders_to_print[choose_update_order]["status"]))
                if replace_status == "":
                    replace_status = orders_to_print[choose_update_order]["status"]
                elif replace_status == 1: #make into a function or loop
                    replace_status = "Preparing"
                    orders_to_print[choose_update_order]["status"] = replace_status
                elif replace_status == 2:
                    replace_status = "Out-For-Delivery"
                    orders_to_print[choose_update_order]["status"] = replace_status
                elif replace_status == 3:
                    replace_status = "Delivered"
                    orders_to_print[choose_update_order]["status"] = replace_status
                else:
                    print("Sorry, that wasn't an option")
                    return update_order_status()
                print(products_to_print)
                replacement_products_list = []
                replace_items = input("Current products: {}\nNew product: ".format(orders_to_print[choose_update_order]["items"]))
                if replace_items == "":
                    replace_items = orders_to_print[choose_update_order]["items"]
                    replacement_products_list = orders_to_print[choose_update_order]["items"]
                else:
                    while replace_items != "0":
                        replacement_products_list.append(replace_items)
                        print("Current list: {}".format(replacement_products_list))
                        replace_items = input("New product: ")
                    orders_to_print[choose_update_order]["items"] = replacement_products_list
                    print(replacement_products_list)
                print(orders_to_print[choose_update_order])
                with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\order_dictionary.csv", "r") as file:
                    reader = csv.reader(file.readlines())
                with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\order_dictionary.csv", "w") as f:
                    writer = csv.writer(f, lineterminator='\n')
                    for i, line in enumerate(reader, 0):
                        if i == choose_update_order:
                            writer.writerow([replace_name, replace_address, replace_phone, replace_courier, replace_status, replacement_products_list])
                        else:
                            writer.writerow(line)
                return update_another_order()
            else:
                print("Sorry, that isn't in the list.")
                return update_another_order()
        elif another_order_update == 2:
            print("Okay, thank you")
            return order_menu()
        else:
            print("Sorry, that isn't an option")
            return update_another_order()
    except ValueError:
        print("Oops! Please input a number.")
        return update_another_order()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)

def delete_an_order():
    print("Delete An Order:")
    products_to_print = {}
    line_num = 1
    for order in load_order_list():
        products_to_print[line_num] = order
        line_num += 1
    for key, value in products_to_print.items():
        print("{}: {}".format(key, value))
    try:
        delete_order = int(input("Which order would you like to delete?\nYou can press 0 to go back\n"))
        if delete_order == 0:
            return order_menu()
        elif delete_order in products_to_print.keys():
            confirm = int(input("Are you sure you want to delete {}?\nPress 1 for Yes\nPress 2 to cancel\n".format(products_to_print[delete_order])))
            if confirm == 1:
                with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\order_dictionary.csv", "r") as file:
                    reader = csv.reader(file.readlines())
                with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\order_dictionary.csv", "w") as f:
                    writer = csv.writer(f, lineterminator='\n')
                    for i, line in enumerate(reader, 0):
                        if i != delete_order:
                            writer.writerow(line)
                print("You've successfully deleted {}'s order from the list!".format(products_to_print[delete_order]["customer_name"]))
                products_to_print = {}
                line_num = 1
                for order in load_order_list():
                    products_to_print[line_num] = order
                    line_num += 1
                for key, value in products_to_print.items():
                    print("{}: {}".format(key, value))
                return delete_another_order()
            else:
                print("Okay, cancelled!")
                return delete_an_order()
        else:
            print("Sorry, that isn't an option")
    except ValueError:
        print("Oops! Please input a number.")
        return delete_an_order()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)

def delete_another_order(): #add in a while loop because otherwise it won't remember what has and hasn't been deleted
    products_to_print = {}
    line_num = 1
    for order in load_order_list():
        products_to_print[line_num] = order
        line_num += 1
    try:
        delete_order_again = int(input("Would you like to delete another order?\nPress 1 for Yes\nPress 2 for No\n"))
        if delete_order_again == 1:
            delete_order = int(input("Which order would you like to delete?\n"))
            if delete_order in products_to_print.keys():
                confirm = int(input("Are you sure you want to delete {}?\nPress 1 for Yes\nPress 2 to cancel\n".format(products_to_print[delete_order])))
                if confirm == 1:
                    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\order_dictionary.csv", "r") as file:
                        reader = csv.reader(file.readlines())
                    with open(r"C:\Users\lilbl\VSCode\MINI-PROJECT\source\order_dictionary.csv", "w") as f:
                        writer = csv.writer(f, lineterminator='\n')
                        for i, line in enumerate(reader, 0):
                            if i != delete_order:
                                writer.writerow(line)
                    print("You've successfully deleted {}'s order from the list!".format(products_to_print[delete_order]["customer_name"]))
                    products_to_print = {}
                    line_num = 1
                    for order in load_order_list():
                        products_to_print[line_num] = order
                        line_num += 1
                    for key, value in products_to_print.items():
                        print("{}: {}".format(key, value))
                    return delete_another_order()
                else:
                    print("Okay, cancelled!")
                    return delete_another_order()
            else:
                print("Sorry, that isn't an option")
                return delete_another_order()
        elif delete_order_again == 2:
            print("Okay,we're done here")
            return order_menu()
        else:
            print("Sorry, that isn't an option")
    except ValueError:
        print("Oops! Please input a number.")
        return delete_another_order()
    except KeyboardInterrupt:
        print("Keyboard Interrupt :)")
        os._exit(0)
        
main_menu()
#1194