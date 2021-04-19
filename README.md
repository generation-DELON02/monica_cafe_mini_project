# Monica's Mini Project :)

## Overview:
The client has launched a pop-up cafe in a busy business district. They
are offering delivered home-made lunches and refreshments to the
surrounding offices. As such, they require a software application which
helps them to log and track orders.

## Requirements:
* I want to maintain a collection of products and couriers.
* When a customer makes a new order, I need to create this on the
  system.
* I need to be able to update the status of an order i.e: preparing,
  out-for-delivery, delivered.
* When I exit my app, I need all data to be persisted and not lost.
* When I start my app, I need to load all persisted data.
* I need to be sure my app has been tested and proven to work well.

## How To:
This is a program that runs on the command line (CLI).
After cloning the repo, open the file called app_csv.py. All you need to do is change the paths on lines 7, 15 and 23 to your own local paths so that Python can find the CSVs when running the program.
Then, just run the file, and follow the instructions in the terminal!

The file named app_mysql.py is the final version of this project. There are less lines of code in this file due to some refactoring, and error handling has been imporved. However, this connects to a local MySQL database using Docker, so this file will only run successfully on my local computer.

## Key learnings:
* Reading and writing to both .txt files and .csv files
* Writing MYSQL queries to access or update any row in the database