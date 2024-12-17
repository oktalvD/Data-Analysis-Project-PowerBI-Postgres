import random
import gender_guesser.detector as gender
from faker import Faker
import pandas as pd

fake = Faker("en_US")

d = gender.Detector()

# Top 3 cities for each state
us_state_cities = {
    "Alabama": ["Mobile", "Montgomery", "Huntsville"],
    "Alaska": ["Anchorage", "Fairbanks", "Juneau"],
    "Arizona": ["Phoenix", "Tucson", "Mesa"],
    "Arkansas": ["Little Rock", "Fort Smith", "Fayetteville"],
    "California": ["Los Angeles", "San Diego", "San Jose"],
    "Colorado": ["Denver", "Colorado Springs", "Aurora"],
    "Connecticut": ["Bridgeport", "New Haven", "Stamford"],
    "Delaware": ["Wilmington", "Middletown", "Newark"],
    "Florida": ["Jacksonville", "Miami", "Tampa"],
    "Georgia": ["Atlanta", "Augusta", "Columbus"],
    "Hawaii": ["Honolulu", "Hilo", "Kailua"],
    "Idaho": ["Boise", "Nampa", "Meridian"],
    "Illinois": ["Chicago", "Aurora", "Naperville"],
    "Indiana": ["Indianapolis", "Fort Wayne", "Evansville"],
    "Iowa": ["Des Moines", "Cedar Rapids", "Davenport"],
    "Kansas": ["Wichita", "Overland Park", "Kansas City"],
    "Kentucky": ["Louisville", "Lexington", "Bowling Green"],
    "Louisiana": ["New Orleans", "Baton Rouge", "Shreveport"],
    "Maine": ["Portland", "Lewiston", "Bangor"],
    "Maryland": ["Baltimore", "Frederick", "Rockville"],
    "Massachusetts": ["Boston", "Worcester", "Springfield"],
    "Michigan": ["Detroit", "Grand Rapids", "Warren"],
    "Minnesota": ["Minneapolis", "Saint Paul", "Rochester"],
    "Mississippi": ["Jackson", "Gulfport", "Biloxi"],
    "Missouri": ["St. Louis", "Kansas City", "Springfield"],
    "Montana": ["Billings", "Missoula", "Great Falls"],
    "Nebraska": ["Omaha", "Grand Island", "Bellevue"],
    "Nevada": ["Las Vegas", "Henderson", "Reno"],
    "New Hampshire": ["Derry", "Nashua", "Concord"],
    "New Jersey": ["Newark", "Jersey City", "Paterson"],
    "New Mexico": ["Albuquerque", "Las Cruces", "Rio Rancho"],
    "New York": ["New York City", "Buffalo", "Rochester"],
    "North Carolina": ["Charlotte", "Raleigh", "Greensboro"],
    "North Dakota": ["Fargo", "Bismarck", "Grand Forks"],
    "Ohio": ["Columbus", "Cleveland", "Cincinnati"],
    "Oklahoma": ["Oklahoma City", "Tulsa", "Norman"],
    "Oregon": ["Portland", "Salem", "Eugene"],
    "Pennsylvania": ["Philadelphia", "Pittsburgh", "Allentown"],
    "Rhode Island": ["Providence", "Cranston", "Pawtucket"],
    "South Carolina": ["Columbia", "Charleston", "Greenville"],
    "South Dakota": ["Sioux Falls", "Rapid City", "Brookings"],
    "Tennessee": ["Nashville", "Memphis", "Knoxville"],
    "Texas": ["Houston", "San Antonio", "Dallas"],
    "Utah": ["Salt Lake City", "West Valley City", "Provo"],
    "Vermont": ["Burlington", "Essex", "South Burlington"],
    "Virginia": ["Virginia Beach", "Norfolk", "Chesapeake"],
    "Washington": ["Seattle", "Spokane", "Tacoma"],
    "West Virginia": ["Charleston", "Huntington", "Morgantown"],
    "Wisconsin": ["Milwaukee", "Madison", "Green Bay"],
    "Wyoming": ["Cheyenne", "Casper", "Laramie"]
}

# Define occupation and role categories
employee_roles = [
    "Office Worker", "Teacher", "Nurse", "Engineer", "Technician", "Salesperson",
    "Office Clerk", "Electrician", "Mechanic", "Accountant", "Administrative Assistant",
    "Customer Service Representative", "Receptionist", "Warehouse Worker", "Cashier",
    "Security Guard", "Bank Teller", "Pharmacy Technician", "Bus Driver", "Chef",
    "Waiter", "Bartender", "HR Specialist", "Marketing Assistant", "Data Entry Clerk",
    "IT Support Specialist", "Graphic Designer", "Web Developer", "Project Manager",
    "Social Worker", "Police Officer", "Firefighter", "Librarian", "Paralegal",
    "Medical Assistant", "Physiotherapist", "Radiologic Technician", "Truck Driver",
    "Quality Inspector", "Purchasing Agent", "Translator", "Event Planner", "Surveyor",
    "Environmental Technician", "Childcare Worker", "Counselor", "Fitness Trainer",
    "Logistics Specialist", "Archivist", "Tailor", "Tour Guide", "Photographer",
    "Banking Associate", "Dental Assistant", "Veterinary Technician", "Yoga Instructor",
    "Personal Assistant", "Landscaper", "Factory Worker", "Cleaner", "Delivery Driver",
    "Assembler", "Construction Worker", "Research Assistant", "Statistician",
    "Public Relations Specialist", "Real Estate Agent", "Loan Officer", "Insurance Agent",
    "Budget Analyst", "Retail Manager", "Advertising Associate",
]

self_employed_roles = [
    "Consultant", "Artist", "Small Business Owner", "Freelance Writer", "Freelance Graphic Designer",
    "Photographer", "Videographer", "Freelance Web Developer", "Self-Published Author", "Online Tutor",
    "Freelance Marketer", "Freelance Accountant", "Voice Actor", "Life Coach", "Blogger",
]

high_income_roles = [
    "Doctor", "Lawyer", "Senior Manager", "Software Engineer", "IT Director", "CEO",
    "CFO", "Investment Banker", "Architect", "Actuary", "Pilot", "Business Owner", "Pharmacist",
    "Data Scientist", "Professor", "Financial Analyst", "Dentist", "Corporate Consultant",
]

gig_roles = [
    "Uber Driver", "Lyft Driver", "Delivery Rider", "Freelance Photographer",
    "Content Creator", "Dog Walker", "House Cleaner", "Personal Shopper",
    "Tasker", "Bicycle Courier", "Virtual Assistant", "Pet Sitter",
    "Online Reseller", "Etsy Seller", "Online Survey Taker", "Airbnb Host",
    "Car Washer", "Yard Cleaner", "Mover", "Freelance Coder",
]

# Define income ranges based on occupation
occupation_income_ranges = {
    "Employee": (30000, 100000),
    "Self-Employed": (40000, 150000),
    "Retired": (15000, 50000),
    "Student": (5000, 20000),
    "Unemployed": (0, 15000),
    "High-Income Professional": (100000, 300000),
    "Gig Worker": (10000, 40000)
}

# Define occupation distribution by age group
age_occupation_weights = {
    (18, 25): {
        "Student": 50,
        "Employee": 30,
        "Self-Employed": 5,
        "Unemployed": 5,
        "High-Income Professional": 3,
        "Gig Worker": 7
    },
    (26, 35): {
        "Student": 8,
        "Employee": 61,
        "Self-Employed": 10,
        "Unemployed": 4,
        "High-Income Professional": 5,
        "Gig Worker": 12
    },
    (36, 45): {
        "Student": 4,
        "Employee": 56,
        "Self-Employed": 8,
        "Unemployed": 3,
        "High-Income Professional": 13,
        "Gig Worker": 16
    },
    (46, 55): {
        "Student": 2,
        "Employee": 50,
        "Self-Employed": 8,
        "Unemployed": 3,
        "High-Income Professional": 15,
        "Gig Worker": 17,
        "Retired": 5
    },
    (56, 65): {
        "Student": 1,
        "Employee": 38,
        "Self-Employed": 7,
        "Unemployed": 10,
        "High-Income Professional": 10,
        "Gig Worker": 4,
        "Retired": 30
    }
}


occupation_account_weights = {
    "Employee": {
        ("Current",): 0.5,
        ("Current", "Savings"): 0.3,
        ("Current", "Savings", "Business"): 0.2
    },
    "Self-Employed": {
        ("Current",): 0.1,
        ("Current", "Business"): 0.4,
        ("Current", "Savings", "Business"): 0.5
    },
    "High-Income Professional": {
        ("Current",): 0.05,
        ("Current", "Savings"): 0.2,
        ("Current", "Savings", "Business"): 0.75
    },
    "Gig Worker": {
        ("Current",): 0.6,
        ("Current", "Savings"): 0.3,
        ("Current", "Savings", "Business"): 0.1
    },
    "Unemployed": {
        ("Current",): 0.77,
        ("Current", "Business"): 0.2,
        ("Current", "Savings", "Business"): 0.03
    },
    "Retired": {
        ("Current",): 0.55,
        ("Current", "Savings"): 0.35,
        ("Current", "Savings", "Business"): 0.1
    },
    "Student": {
        ("Current",): 0.75,
        ("Current", "Savings"): 0.2,
        ("Current", "Savings", "Business"): 0.05
    }
}



def generate_customer_data(num_customers=3000):
    customers = []
    used_ids = set()

    while len(customers) < num_customers:
        customer_id = random.randint(10000, 99999)
        if customer_id not in used_ids:
            used_ids.add(customer_id)

            name = fake.name()

            # Use gender-guesser to determine gender based on the name
            gender = d.get_gender(name.split()[0])  # Use the first name for gender guess

            # Assign a gender
            if gender == 'male':
                gender = 'Male'
            elif gender == 'female':
                gender = 'Female'
            else:
                gender = 'Male'  # For ambiguous cases


            state = random.choice(list(us_state_cities.keys()))
            city = random.choice(us_state_cities[state])
            age = random.randint(18, 65)

            # Determine occupation based on age
            for age_range, weights in age_occupation_weights.items():
                if age_range[0] <= age <= age_range[1]:
                    occupation = random.choices(
                        list(weights.keys()), list(weights.values()), k=1
                    )[0]
                    break

            # Assign role based on occupation
            if occupation == "Employee":
                role = random.choice(employee_roles)
            elif occupation == "Self-Employed":
                role = random.choice(self_employed_roles)
            elif occupation == "High-Income Professional":
                role = random.choice(high_income_roles)
            elif occupation == "Gig Worker":
                role = random.choice(gig_roles)
            else:
                role = "Unemployed"

            # Determine income based on occupation
            income_range = occupation_income_ranges.get(occupation)
            if income_range:
                income = round(random.uniform(income_range[0], income_range[1]), 2)
            else:
                income = 0

            # Apply age factor for income adjustment
            if 18 <= age <= 25:
                income *= random.uniform(0.7, 1.1)
            elif 26 <= age <= 35:
                income *= random.uniform(0.8, 1.2)
            elif 36 <= age <= 45:
                income *= random.uniform(0.9, 1.3)
            elif 46 <= age <= 55:
                income *= random.uniform(1.0, 1.4)
            elif 56 <= age <= 65:
                income *= random.uniform(0.8, 1.4)

            # Determine account types based on occupation
            account_combination = random.choices(
                list(occupation_account_weights[occupation].keys()),
                list(occupation_account_weights[occupation].values()),
                k=1
            )[0]

            # Fill in columns for account types
            account_types = list(account_combination)
            while len(account_types) < 3:
                account_types.append(None)

            customer = {
                "customer_id": customer_id,
                "name": name,
                "age": age,
                "gender": gender,
                "occupation": occupation,
                "role": role,
                "income": round(income, 2),  # Yearly salary in USD
                "account_type_1": account_types[0],
                "account_type_2": account_types[1],
                "account_type_3": account_types[2],
                "account_opening_date": fake.date_this_decade(),
                "last_active_date": fake.date_this_year(),
                "state": state,
                "city": city,
            }
            customers.append(customer)

    return customers



# Generate 3000 customer data
customer_data = generate_customer_data()

# Convert to DataFrame
df_customers = pd.DataFrame(customer_data)

# Set pandas options for better display
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.width', None)  # Ensure table is displayed without line breaks

# Display first 15 records
print(df_customers.head(15))

# Save to CSV
df_customers.to_csv("customers.csv", index=False)

print("Customer data with occupations, income, and account types generated and saved to 'customers.csv'.")
