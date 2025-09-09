import os
import django
import pandas as pd

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TimetableMGT.settings")
django.setup()

from myApp.models import AIML_1, Faculty

# Load Excel file
df = pd.read_excel('excels/AIML_1.xlsx')

# Normalize headers
df.columns = df.columns.str.strip().str.lower()

# Expected headers
expected = ["day", "time", "course", "year", "subject", "teacher", "room"]
missing = [c for c in expected if c not in df.columns]
if missing:
    raise ValueError(f"Missing columns in Excel: {missing}")

 
for _, row in df.iterrows():
    faculty, _ = Faculty.objects.get_or_create(
        name=row["teacher"],
        defaults={"password": "harsh@03"}   
    )

    # Create AIML_1 entry
    AIML_1.objects.create(
        day=row["day"],
        time=row["time"],
        course=row["course"],
        year=str(row["year"]),
        subject=row["subject"],
        faculty=faculty,
        room=row["room"]
    )

print("Data inserted into AIML_1")
