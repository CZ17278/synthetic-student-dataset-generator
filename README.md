# Synthetic Student Dataset Generator

This project generates a synthetic dataset of university students using Python.

## Features
- Generates 10,000 student records
- Includes personal, academic, and medical attributes
- Randomized but reproducible (seeded randomness)
- Exports data to CSV format

## Dataset Fields

| Column | Description |
|------|------------|
| name | Full name |
| student_id | Unique student ID |
| email | Generated email |
| date_of_birth | Date of birth |
| gender | Gender |
| postal_code | Postal code |
| degree_program | Field of study |
| year_of_study | Academic year |
| gpa | Grade point average |
| scholarship | Scholarship status |
| medical_indicator | Health condition flag |

## How to run

```bash
pip install -r requirements.txt
python src/generate_dataset.py
