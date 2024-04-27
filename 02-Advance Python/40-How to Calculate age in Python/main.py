from datetime import datetime

def calculate_age(birthdate):
    # Get the current date
    current_date = datetime.now()

    # Calculate the difference between current date and birthdate
    age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))

    return age

# Example birthdate (year, month, day)
birthdate = datetime(1990, 4, 15)

# Calculate age
age = calculate_age(birthdate)
print("Age:", age)
