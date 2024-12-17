import pandas as pd
from faker import Faker
import random
import uuid

# Initialize Faker
fake = Faker()

# Function to generate realistic debit transactions
def generate_realistic_debits(customer_id, income):
    transactions = []

    # Define total spending target
    total_spending = random.uniform(income * 0.6, income * 1.2)

    # Define transaction count
    num_transactions = random.randint(10, 120)

    # Distribute spending into small, medium, and large purchases
    small_percent = 70  # % of transactions are small
    medium_percent = 25  # % of transactions are medium
    large_percent = 5  # % of transactions are large

    small_transactions = int(num_transactions * small_percent / 100)
    medium_transactions = int(num_transactions * medium_percent / 100)
    large_transactions = num_transactions - (small_transactions + medium_transactions)

    spent_amount = 0


    # Generate transactions
    for _ in range(small_transactions):
        if spent_amount >= total_spending:
            break
        amount = round(random.uniform(10, 50), 2)
        spent_amount += amount
        transactions.append({
            "transaction_id": str(uuid.uuid4()),
            "customer_id": customer_id,
            "date": fake.date_this_year(before_today=True),
            "amount": -amount,  # Negative for debits
            "transaction_type": "Debit",
            "channel": random.choice(["ATM", "Online", "Branch"]),
        })

    for _ in range(medium_transactions):
        if spent_amount >= total_spending:
            break
        amount = round(random.uniform(100, 300), 2)
        spent_amount += amount
        transactions.append({
            "transaction_id": str(uuid.uuid4()),
            "customer_id": customer_id,
            "date": fake.date_this_year(before_today=True),
            "amount": -amount,
            "transaction_type": "Debit",
            "channel": random.choice(["ATM", "Online", "Branch"]),
        })

    for _ in range(large_transactions):
        if spent_amount >= total_spending:
            break
        amount = round(random.uniform(500, 5000), 2)
        spent_amount += amount
        transactions.append({
            "transaction_id": str(uuid.uuid4()),
            "customer_id": customer_id,
            "date": fake.date_this_year(before_today=True),
            "amount": -amount,
            "transaction_type": "Debit",
            "channel": random.choice(["ATM", "Online", "Branch"]),
        })

    # Adjust the last transaction to meet total_spending
    if spent_amount < total_spending:
        remaining = total_spending - spent_amount
        transactions.append({
            "transaction_id": str(uuid.uuid4()),
            "customer_id": customer_id,
            "date": fake.date_this_year(before_today=True),
            "amount": -round(remaining, 2),
            "transaction_type": "Debit",
            "channel": random.choice(["ATM", "Online", "Branch"]),
        })


    return transactions


# Function to generate transactions for a year
def generate_yearly_transactions(customers_df, min_bonus=1, max_bonus=3):
    transactions = []

    for i, (_, customer) in enumerate(customers_df.iterrows()):  # Added i for tracking progress
        customer_id = customer["customer_id"]
        income = customer["income"]

        # Progress message
        if i % 10 == 0:
            print(f"Processed {i} customers out of {len(customers_df)}")

        # Monthly salary credits
        monthly_salary = income / 12
        for month in range(1, 13):
            date = fake.date_this_year(before_today=True)
            while date.month != month:
                date = fake.date_this_year(before_today=True)

            salary_transaction = {
                "transaction_id": str(uuid.uuid4()),
                "customer_id": customer_id,
                "date": date,
                "amount": round(random.uniform(monthly_salary * 0.9, monthly_salary * 1.1), 2),
                "transaction_type": "Credit",
                "channel": random.choice(["Online", "Branch"]),
            }
            transactions.append(salary_transaction)

        # Debug message for salary credits


        # Random bonus credits
        num_bonus_transactions = random.randint(min_bonus, max_bonus)
        for _ in range(num_bonus_transactions):
            bonus_date = fake.date_this_year(before_today=True)
            bonus_amount = round(random.uniform(100, income * 0.05), 2)

            bonus_transaction = {
                "transaction_id": str(uuid.uuid4()),
                "customer_id": customer_id,
                "date": bonus_date,
                "amount": bonus_amount,
                "transaction_type": "Credit",
                "channel": random.choice(["ATM", "Online", "Branch"]),
            }
            transactions.append(bonus_transaction)

        # Debug message for bonus credits


        # Realistic debit transactions
        debit_transactions = generate_realistic_debits(customer_id, income)
        transactions.extend(debit_transactions)

    return transactions


# Load existing customer data
df_customers = pd.read_csv("customers.csv")

# Generate transactions for all customers
transaction_data = generate_yearly_transactions(df_customers)

# Save to CSV
df_transactions = pd.DataFrame(transaction_data)
df_transactions.to_csv("transactions.csv", index=False)

print("Transaction data generated and saved to 'transactions.csv'.")
