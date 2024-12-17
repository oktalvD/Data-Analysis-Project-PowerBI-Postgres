import psycopg2  # Import the psycopg2 library for connecting to PostgreSQL
import pandas as pd  # Import the pandas library for reading CSV files and handling data

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="capital_metrics",  # Name of the database we created in PostgreSQL
    user="postgres",  # PostgreSQL username (replace with your actual username if different)
    password="****",  # Password for your PostgreSQL user (replace with your actual password)
    host="localhost",  # Host is localhost because PostgreSQL is running on your local machine
    port="5433"  # Default PostgreSQL port
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Function to insert customer data into the customers table
def insert_customers():
    # Read the customer data from the CSV file
    df_customers = pd.read_csv("customers.csv")  # Load customer data into a pandas DataFrame
    # Loop through each row in the DataFrame
    for index, row in df_customers.iterrows():
        # Execute SQL query to insert data into the customers table
        cursor.execute("""
            INSERT INTO customers (customer_id, name, age, gender, occupation, role, income, account_type_1, account_type_2, account_type_3, account_opening_date, last_active_date, state,city)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, (
            row['customer_id'],  # customer_id from the CSV file
            row['name'],  # name from the CSV file
            row['age'],  # age from the CSV file
            row['gender'],  # gender from the CSV file
            row['occupation'],
            row['role'],
            row['income'],  # income from the CSV file
            row['account_type_1'],  # account_type from the CSV file
            row['account_type_2'],
            row['account_type_3'],
            row['account_opening_date'],  # account opening date from the CSV file
            row['last_active_date'],  # last active date from the CSV file
            row['state'],
            row['city']  # location from the CSV file
        ))
    # Commit the transaction to the database (save the changes)
    conn.commit()

# Function to insert transaction data into the transactions table
def insert_transactions():
    # Read the transaction data from the CSV file
    df_transactions = pd.read_csv("transactions.csv")  # Load transaction data into a pandas DataFrame
    # Loop through each row in the DataFrame
    for index, row in df_transactions.iterrows():
        # Execute SQL query to insert data into the transactions table
        cursor.execute("""
            INSERT INTO transactions (transaction_id, customer_id, date, amount, transaction_type, channel)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (
            row['transaction_id'],  # transaction_id from the CSV file
            row['customer_id'],  # customer_id from the CSV file
            row['date'],  # date of the transaction from the CSV file
            row['amount'],  # amount of the transaction from the CSV file
            row['transaction_type'],  # type of the transaction (e.g., 'payment' or 'refund')
            row['channel']  # channel of the transaction (e.g., 'online' or 'in-store')
        ))
    # Commit the transaction to the database (save the changes)
    conn.commit()

# Function to insert loan data into the loans table
def insert_loans():
    # Read the loan data from the CSV file
    df_loans = pd.read_csv("loans.csv")  # Load loan data into a pandas DataFrame
    # Loop through each row in the DataFrame
    for index, row in df_loans.iterrows():
        # Execute SQL query to insert data into the loans table
        cursor.execute("""
            INSERT INTO loans (loan_id, customer_id, loan_type, loan_amount, interest_rate, loan_start_date, loan_term, loan_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """, (
            row['loan_id'],  # loan_id from the CSV file
            row['customer_id'],  # customer_id from the CSV file
            row['loan_type'],  # type of the loan (e.g., 'personal', 'mortgage', etc.)
            row['loan_amount'],  # loan amount from the CSV file
            row['interest_rate'],  # interest rate for the loan from the CSV file
            row['loan_start_date'],  # date when the loan started
            row['loan_term'],  # loan term in months or years
            row['loan_status']  # status of the loan (e.g., 'active', 'paid off', 'defaulted')
        ))
    # Commit the transaction to the database (save the changes)
    conn.commit()

# Call the insert functions to insert data into the respective tables
insert_customers()  # Insert the customer data
insert_transactions()  # Insert the transaction data
insert_loans()  # Insert the loan data

# Close the cursor and connection once the data has been inserted
cursor.close()  # Close the cursor (used for executing SQL commands)
conn.close()  # Close the database connection

# Print a message to indicate that the data insertion is complete
print("Data inserted into PostgreSQL.")
