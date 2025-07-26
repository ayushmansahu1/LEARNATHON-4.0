import pandas as pd
import random
from datetime import datetime, timedelta

# Define categorical value lists based on sample data
states = ['OH', 'IL', 'IN', 'PA', 'NC', 'SC', 'VA', 'WV', 'NY']
cities = ['Columbus', 'Arlington', 'Northbend', 'Springfield', 'Riverwood', 'Hillsdale', 'Northbrook']
makes = {
    'Honda': ['CRV', 'Civic'],
    'Audi': ['A5', 'A3'],
    'Suburu': ['Impreza', 'Forrestor', 'Legacy'],
    'Volkswagen': ['Passat', 'Jetta'],
    'Jeep': ['Wrangler', 'Grand Cherokee'],
    'Dodge': ['Neon', 'RAM'],
    'BMW': ['3 Series', 'X5', 'X6', 'M5'],
    'Ford': ['Escape', 'F150', 'Fusion'],
    'Nissan': ['Maxima', 'Ultima', 'Pathfinder'],
    'Chevrolet': ['Malibu', 'Silverado', 'Tahoe'],
    'Toyota': ['Camry', 'Corolla'],
    'Mercedes': ['ML350', 'E400'],
    'Saab': ['95', '92x'],
    'Accura': ['TL', 'MDX']
}
colors = ['White', 'Black', 'Gray', 'Silver', 'Red', 'Blue']
educations = ['High School', 'Associate', 'College', 'MD', 'PhD', 'JD', 'Masters']
occupations = ['adm-clerical', 'protective-serv', 'priv-house-serv', 'tech-support', 'exec-managerial', 
               'prof-specialty', 'sales', 'craft-repair', 'other-service', 'handlers-cleaners', 
               'machine-op-inspct', 'transport-moving', 'armed-forces', 'farming-fishing']
hobbies = ['polo', 'movies', 'board-games', 'reading', 'camping', 'yachting', 'skydiving', 'golf', 
           'basketball', 'hiking', 'dancing', 'bungie-jumping', 'cross-fit', 'exercise', 'chess', 
           'paintball', 'base-jumping', 'video-games', 'kayaking']
relationships = ['husband', 'wife', 'own-child', 'other-relative', 'not-in-family', 'unmarried']
accident_types = ['Single Vehicle Collision', 'Multi-vehicle Collision', 'Vehicle Theft', 'Parked Car']
collision_types = ['Front Collision', 'Rear Collision', 'Side Collision', 'Unknown']
severities = ['Trivial Damage', 'Minor Damage', 'Major Damage', 'Total Loss']
authorities = ['Police', 'Ambulance', 'Fire', 'Other', '']
property_damage = ['YES', 'NO', 'Unknown']
police_report = ['YES', 'NO', '']

# Helper functions for random value generation
def generate_claim_id(i):
    return f'AA{i:08d}'

def generate_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

def generate_bind_date():
    return generate_date(datetime(2020, 1, 1), datetime(2023, 12, 31))

def generate_policy_start_date(bind_date):
    return bind_date + timedelta(days=random.randint(0, 365))

def generate_policy_expiry_date(policy_start_date):
    return policy_start_date + timedelta(days=365)

def generate_accident_date(policy_start_date, policy_expiry_date):
    return generate_date(policy_start_date, policy_expiry_date)

def generate_claims_date(accident_date):
    return accident_date + timedelta(days=random.randint(1, 30))

def generate_dl_expiry_date(claims_date):
    return claims_date + timedelta(days=random.randint(365, 365 * 5))

def generate_vehicle_claim(severity, vehicle_cost):
    if severity == 'Total Loss':
        return vehicle_cost * random.uniform(0.8, 1.0)
    elif severity == 'Major Damage':
        return vehicle_cost * random.uniform(0.5, 0.8)
    elif severity == 'Minor Damage':
        return vehicle_cost * random.uniform(0.1, 0.5)
    else:  # Trivial Damage
        return vehicle_cost * random.uniform(0.0, 0.1)

def generate_injury_claim(bodily_injuries):
    return random.uniform(1000, 10000) * bodily_injuries if bodily_injuries > 0 else 0

def generate_property_claim(property_damage):
    return random.uniform(500, 5000) if property_damage == 'YES' else 0

# Function to generate a single record
def generate_record(i):
    claim_id = generate_claim_id(i)
    bind_date = generate_bind_date()
    bind_date_str = bind_date.strftime('%m-%d-%Y')  # Matches sample format
    policy_start_date = generate_policy_start_date(bind_date)
    policy_start_date_str = policy_start_date.strftime('%m/%d/%Y')
    policy_expiry_date = generate_policy_expiry_date(policy_start_date)
    policy_expiry_date_str = policy_expiry_date.strftime('%m/%d/%Y')
    accident_date = generate_accident_date(policy_start_date, policy_expiry_date)
    accident_date_str = accident_date.strftime('%m/%d/%Y')
    claims_date = generate_claims_date(accident_date)
    claims_date_str = claims_date.strftime('%m/%d/%Y')
    dl_expiry_date = generate_dl_expiry_date(claims_date)
    dl_expiry_date_str = dl_expiry_date.strftime('%m-%d-%Y')  # Matches sample format

    customer_life_value = random.randint(10, 25)
    age_insured = random.randint(18, 80)
    policy_num = random.randint(100000000, 999999999)
    policy ACO = random.choice(states)
    policy_bi = random.choice(['100/300', '250/500', '500/1000'])
    policy_ded = random.choice([500, 1000, 2000])
    policy_premium = round(random.uniform(500, 2000), 2)
    umbrella_limit = random.choice([0, 4000000, 5000000, 6000000, 8000000])
    insured_zip = random.randint(400000, 699999)
    gender = random.choice(['MALE', 'FEMALE'])
    education = random.choice(educations)
    occupation = random.choice(occupations)
    hobbies = random.choice(hobbies)
    insured_relationship = random.choice(relationships)
    capital_gains = random.randint(0, 100000)
    capital_loss = random.randint(-100000, 0)
    garage_location = random.choice(['Yes', 'No'])

    accident_type = random.choice(accident_types)
    if accident_type in ['Vehicle Theft', 'Parked Car']:
        collision_type = 'Unknown'
        num_vehicles = 1
    else:
        collision_type = random.choice(['Front Collision', 'Rear Collision', 'Side Collision'])
        num_vehicles = random.randint(2, 4) if accident_type == 'Multi-vehicle Collision' else 1

    accident_severity = random.choice(severities)
    authorities_contacted = random.choice(authorities)
    accident_state = random.choice(states)
    accident_city = random.choice(cities)
    accident_location = f'{random.randint(1000, 9999)} {random.choice(["Oak", "Maple", "Pine", "Elm", "Cedar"])} {random.choice(["St", "Ave", "Blvd", "Ridge", "Ln", "Hwy", "Drive"])}'
    accident_hour = random.randint(0, 23)
    property_damage = random.choice(property_damage)
    bodily_injuries = random.randint(0, 3)
    witnesses = random.randint(0, 3)
    police_report = random.choice(police_report)

    auto_make = random.choice(list(makes.keys()))
    auto_model = random.choice(makes[auto_make])
    auto_year = random.randint(2015, 2024)
    vehicle_color = random.choice(colors)
    vehicle_cost = round(random.uniform(5000, 50000), 2)
    annual_mileage = random.randint(5000, 20000)
    diff_in_mileage = random.randint(2000, 8000)
    low_mileage_discount = 1 if annual_mileage < 10000 else 0
    fraud_ind = 'Y' if random.random() < 0.05 else 'N'  # 5% fraud rate
    commute_discount = 1 if random.random() < 0.1 else 0  # 10% chance

    vehicle_claim = round(generate_vehicle_claim(accident_severity, vehicle_cost), 2)
    injury_claim = round(generate_injury_claim(bodily_injuries), 2)
    property_claim = round(generate_property_claim(property_damage), 2)
    total_claim = round(injury_claim + property_claim + vehicle_claim, 2)
    vehicle_registration = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=9))
    check_point = 'No'  # Matches sample data

    return {
        'Claim_ID': claim_id,
        'Bind_Date1': bind_date_str,
        'Customer_Life_Value1': customer_life_value,
        'Age_Insured': age_insured,
        'Policy_Num': policy_num,
        'Policy_State': policy_state,
        'Policy_Start_Date': policy_start_date_str,
        'Policy_Expiry_Date': policy_expiry_date_str,
        'Policy_BI': policy_bi,
        'Policy_Ded': policy_ded,
        'Policy_Premium': policy_premium,
        'Umbrella_Limit': umbrella_limit,
        'Insured_Zip': insured_zip,
        'Gender': gender,
        'Education': education,
        'Occupation': occupation,
        'Hobbies': hobbies,
        'Insured_Relationship': insured_relationship,
        'Capital_Gains': capital_gains,
        'Capital_Loss': capital_loss,
        'Garage_Location': garage_location,
        'Accident_Date': accident_date_str,
        'Accident_Type': accident_type,
        'Collision_Type': collision_type,
        'Accident_Severity': accident_severity,
        'authorities_contacted': authorities_contacted,
        'Acccident_State': accident_state,  # Note: typo preserved as in sample
        'Acccident_City': accident_city,    # Note: typo preserved as in sample
        'Accident_Location': accident_location,
        'Accident_Hour': accident_hour,
        'Num_of_Vehicles_Involved': num_vehicles,
        'Property_Damage': property_damage,
        'Bodily_Injuries': bodily_injuries,
        'Witnesses': witnesses,
        'Police_Report': police_report,
        'DL_Expiry_Date': dl_expiry_date_str,
        'Claims_Date': claims_date_str,
        'Auto_Make': auto_make,
        'Auto_Model': auto_model,
        'Auto_Year': auto_year,
        'Vehicle_Color': vehicle_color,
        'Vehicle_Cost': vehicle_cost,
        'Annual_Mileage': annual_mileage,
        'DiffIN_Mileage': diff_in_mileage,
        'Low_Mileage_Discount': low_mileage_discount,
        'Fraud_Ind': fraud_ind,
        'Commute_Discount': commute_discount,
        'Total_Claim': total_claim,
        'Injury_Claim': injury_claim,
        'Property_Claim': property_claim,
        'Vehicle_Claim': vehicle_claim,
        'Vehicle_Registration': vehicle_registration,
        'Check_Point': check_point
    }

# Generate 70,000 records
records = [generate_record(i) for i in range(1, 70001)]

# Create DataFrame and save to CSV
df = pd.DataFrame(records)
df.to_csv('claims_data.csv', index=False)

print("Dataset of 70,000 records generated and saved as 'claims_data.csv'.")