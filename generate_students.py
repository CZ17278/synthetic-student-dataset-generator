import random
import string
import pandas as pd
from datetime import datetime, timedelta

random.seed(42)

N = 10000

# -----------------------------
# Helper functions
# -----------------------------
def random_name():
    first_names = ["Anna", "Lukas", "Maria", "Jean", "Sofia", "Marco", "Elena", "Paul", "Laura", "David"]
    last_names = ["Muller", "Dubois", "Rossi", "Garcia", "Popescu", "Kowalski", "Novak", "Silva", "Martin", "Schmidt"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def random_email(name, sid):
    domain = random.choice(["unitbv.ro", "student.edu", "campus.eu"])
    return f"{name.lower().replace(' ', '.')}.{sid}@{domain}"

def random_dob(start_year=1995, end_year=2006):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    return start + timedelta(days=random.randint(0, (end - start).days))

# -----------------------------
# Attribute pools
# -----------------------------
genders = ["Male", "Female", "Other"]
degree_programs = [
    "Computer Science", "Cybersecurity", "Engineering",
    "Economics", "Medicine", "Law", "Mathematics"
]
postal_codes = ["10{:03d}".format(i) for i in range(100)] + \
               ["75{:03d}".format(i) for i in range(100)] + \
               ["40{:03d}".format(i) for i in range(100)]

medical_status = ["None", "Chronic", "Disability"]

# -----------------------------
# Dataset generation
# -----------------------------
data = []

for i in range(N):
    name = random_name()
    student_id = f"S{100000+i}"
    email = random_email(name, student_id)

    dob = random_dob()
    gender = random.choice(genders)
    postal_code = random.choice(postal_codes)
    degree = random.choice(degree_programs)
    year = random.randint(1, 5)

    gpa = round(random.uniform(2.0, 4.0), 2)
    scholarship = random.choices(["Yes", "No"], weights=[0.3, 0.7])[0]
    medical = random.choices(medical_status, weights=[0.75, 0.15, 0.10])[0]

    data.append([
        name, student_id, email,
        dob.strftime("%Y-%m-%d"),
        gender, postal_code, degree, year,
        gpa, scholarship, medical
    ])

# -----------------------------
# Create DataFrame
# -----------------------------
columns = [
    "name", "student_id", "email",
    "date_of_birth", "gender", "postal_code",
    "degree_program", "year_of_study",
    "gpa", "scholarship", "medical_indicator"
]

df = pd.DataFrame(data, columns=columns)

# -----------------------------
# Save CSV
# -----------------------------
df.to_csv("synthetic_students.csv", index=False)

print("Dataset generated: synthetic_students.csv")
print(df.head())