import datetime

birth_date = input("What date were you born? (dd/mm/yyyy)")
birth_date = ''.join(c for c in birth_date if c.isdigit())
# print(birth_date)

birth_day = int(birth_date[0:2])
birth_month = int(birth_date[2:4])
birth_year = int(birth_date[-4:])

# print(f"{birth_day} {birth_month} {birth_year}")

today = datetime.datetime.today()

# print(f"{today}")
# print(type(today.day))

age = today.year - birth_year

if birth_month > today.month or (birth_month == today.month and birth_day > today.day):
    age -= 1

print(f"You are {age} years old.")
