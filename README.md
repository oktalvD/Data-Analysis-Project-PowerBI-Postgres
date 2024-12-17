Capital Metrics Data Simulation & Analysis

Project Overview

This project demonstrates my skills in data simulation, ETL processes, and data visualization. It involves generating realistic customer data, transaction data, and loan data, storing this information in a PostgreSQL database, and then visualizing it using Power BI.

Key Features:

Data Simulation: Generates large volume of fake customer profiles, including attributes such as income, age, role, and location.
Transaction Generation: Creates realistic debit and credit transactions, including salary credits, bonus payments, and typical debit card spending.
Loan Generation: Simulates various types of loans (e.g., personal, home, car, education, business) for customers.
PostgreSQL Integration: Stores simulated data into a PostgreSQL database, demonstrating proficiency in handling large datasets.
Power BI Visuals: Provides a set of interactive Power BI dashboards to analyze and visualize the data.

The project demonstrates proficiency in:
Data Generation: Creating synthetic data to represent real-world scenarios.
Database Management: Working with PostgreSQL to store and manage structured data.
ETL Processes: Extracting, transforming, and loading data into a database for analysis.
Data Visualization: Building interactive visualizations using Power BI to uncover trends and insights from the generated data.
Purpose

The primary purpose of this project is to showcase my skills in:
Simulating financial data and customer behavior.
Integrating with databases and performing ETL operations.
Creating insightful data visualizations with Power BI.
This project serves as a portfolio piece to demonstrate my ability to work with Python, databases (PostgreSQL), and Power BI.

Project Structure
Python files:
-generate_customers.py # Script for generating customer data
-generate_transactions.py # Script for generating transaction data
-generate_loans.py # Script for generating loan data
-save_to_postgres.py # Script for inserting data into PostgreSQL
Generated files:
-customers.csv # Generated customer data (CSV)
-transactions.csv # Generated transaction data (CSV)
-loans.csv # Generated loan data (CSV)
SQL Schema
PowerBI files

Key Components:
1. Data Simulation:
The project simulates customer data using the Faker library, including attributes such as income, age, gender, occupation, and account types.
For each customer a large volume of realistic transaction data is generated, including monthly salary credits, bonus payments, and debits for daily expenses.
Loan data is generated for each customer, with various types of loans (e.g., personal, car, home, education) and random amounts, interest rates, and statuses (active, paid, defaulted).
2. PostgreSQL Integration:
Data is stored in PostgreSQL, allowing for efficient querying and management of large datasets.
The project demonstrates the use of psycopg2 to interact with the database and perform CRUD operations.
3. Power BI Dashboards:
Power BI dashboards are created to visualize customer demographics, spending patterns, loan data, and transaction trends.
The Power BI template provided includes dynamic visuals that can be filtered and analyzed in real-time.

Technologies Used:
- Python (for data simulation and ETL operations)
- PostgreSQL (for storing and querying data)
- Power BI (for creating data visualizations)
