from datetime import date

# Define two date objects
date1 = date(2022, 4, 15)
date2 = date(2022, 4, 20)

# Compare dates
if date1 < date2:
    print("Date1 is before Date2")
elif date1 > date2:
    print("Date1 is after Date2")
else:
    print("Date1 is equal to Date2")


date3 = date(2021, 12, 31)

if date1 > date3:
    print("Date1 is after Date3")
else:
    print("Date1 is before Date3")
