# seed.py
import csv

# Sample data for episodes and guests
episodes_data = [
    {"date": "1/11/99", "number": 1},
    {"date": "1/12/99", "number": 2},
    {"date": "1/13/99", "number": 3}
]

guests_data = [
    {"name": "Michael J. Fox", "occupation": "actor"},
    {"name": "Sandra Bernhard", "occupation": "comedian"},
    {"name": "Tracey Ullman", "occupation": "television actress"}
]

# Write episodes data to CSV
with open('episodes.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["date", "number"])
    writer.writeheader()
    writer.writerows(episodes_data)

# Write guests data to CSV
with open('guests.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["name", "occupation"])
    writer.writeheader()
    writer.writerows(guests_data)

print("CSV files have been created!")
