import pandas as pd
from faker import Faker
import random
import uuid

# Initialize Faker
fake = Faker()

# Load existing customer data
df_customers = pd.read_csv("customers.csv")
customer_ids = df_customers["customer_id"].tolist()  # Extract all customer IDs


# Function to generate loan data
def generate_loans(customer_ids, min_loans=1, max_loans=3):
    loan_types = ["Personal", "Home", "Car", "Education", "Business"]
    loan_statuses = ["Active", "Paid", "Defaulted"]

    loans = []

    # Define loan amount ranges for each loan type
    loan_amount_ranges = {
        "Personal": (5000, 20000),  # Personal loans have lower amounts
        "Home": (30000, 500000),  # Home loans have higher amounts
        "Car": (10000, 100000),  # Car loans have moderate amounts
        "Education": (5000, 50000),  # Education loans have moderate amounts
        "Business": (20000, 200000)  # Business loans have large amounts
    }

    for customer_id in customer_ids:
        # Each customer can have a random number of loans (1 to 3)
        num_loans = random.randint(min_loans, max_loans)

        for _ in range(num_loans):
            loan_type = random.choice(loan_types)

            # Get the loan amount range based on the loan type
            loan_amount_min, loan_amount_max = loan_amount_ranges[loan_type]

            # Generate a random loan amount within the defined range for each loan type
            loan_amount = round(random.uniform(loan_amount_min, loan_amount_max), 2)

            interest_rate = round(random.uniform(3.5, 15), 2)  # Interest rate between 3.5% and 15%
            loan_term = random.choice([12, 24, 36, 48, 60])  # Loan term in months (1-5 years)

            loan = {
                "loan_id": str(uuid.uuid4()),  # Unique loan ID
                "customer_id": customer_id,  # Link to existing customer
                "loan_type": loan_type,
                "loan_amount": loan_amount,
                "interest_rate": interest_rate,
                "loan_start_date": fake.date_this_decade(),  # Random start date within the last 10 years
                "loan_term": loan_term,
                "loan_status": random.choice(loan_statuses),
            }
            loans.append(loan)

    return loans


# Generate loans for all customers
loan_data = generate_loans(customer_ids)
df_loans = pd.DataFrame(loan_data)

# Save to CSV
df_loans.to_csv("loans.csv", index=False)

print("Loan data generated and saved to 'loans.csv'.")
