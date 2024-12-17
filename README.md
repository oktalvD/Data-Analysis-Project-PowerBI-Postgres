**_Capital Metrics Data Simulation & Analysis_**

**Project Overview**

This project demonstrates my skills in data simulation, ETL processes, and data visualization. It involves generating realistic customer data, transaction data, and loan data, storing this information in a PostgreSQL database, and then visualizing it using Power BI.

**Key Features:**

Data Simulation: _Generates large volume of fake customer profiles, including attributes such as: customer id, name, age , gender, occupation, role, income, account types, account opening date, last active date, state and city._

Transaction Generation: _Creates realistic debit and credit transactions, including salary credits, bonus payments, and typical debit card spending with dates of each transaction._

Loan Generation: _Simulates various types of loans (e.g., personal, home, car, education, business) for customers._ 

PostgreSQL Integration: _Stores simulated data into a PostgreSQL database, demonstrating proficiency in handling large datasets._ 

Power BI Visuals: _Provides a set of interactive Power BI dashboards to analyze and visualize the data._

**The project demonstrates proficiency in:**
- Data Generation: _Creating synthetic data to represent real-world scenarios._
- Database Management: _Working with PostgreSQL to store and manage structured data._
- ETL Processes: _Extracting, transforming, and loading data into a database for analysis._
- Data Visualization: _Building interactive visualizations using Power BI to uncover trends and insights from the generated data._
  

**The primary purpose of this project is to showcase my skills in:**
Simulating financial data and customer behavior.
Integrating with databases and performing ETL operations.
Creating insightful data visualizations with Power BI.
This project serves as a portfolio piece to demonstrate my ability to work with Python, databases (PostgreSQL), and Power BI.

**Project Structure**

Python files:
- generate_customers.py _# Script for generating customer data_
- generate_transactions.py _# Script for generating transaction data_
- generate_loans.py _# Script for generating loan data_
- save_to_postgres.py _# Script for inserting data into PostgreSQL_

Generated files:
- customers.csv _# Generated customer data (CSV)_
- transactions.csv _# Generated transaction data (CSV)_
- loans.csv _# Generated loan data (CSV)_

- SQL Schema
  
PowerBI files:
- CapitalMetrics.pbix _# The full PowerBI application report_
- PowerBi_report_CapitalMetrics.pdf _# Exported PowerBI visuals as pdf_

**Key Components:**
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
Created visuals are exported to the PowerBI_report_CapitalMetrics.pdf.

**Technologies Used:**
- _Python_ (for data simulation and ETL operations)
- _PostgreSQL_ (for storing and querying data)
- _Power BI_ (for creating data visualizations)
