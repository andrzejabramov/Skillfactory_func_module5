from datetime import date, datetime
from typing import List, Dict, Any


users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15'},
              {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22'},
              {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01'}]


def calculate_age(birth_date: str) -> int:
    date_now = date.today()
    birthday = datetime.strptime(birth_date, '%Y-%m-%d').date()
    age = date_now.year - birthday.year - ((date_now.month, date_now.day) < (birthday.month, birthday.day))
    return age

def filter_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    adult_users = []
    for birth in users:
        if calculate_age(birth['birth_date']) >= 18:
            adult_users.append(birth)
    return adult_users

def generate_username(first_name: str, last_name: str) -> str:
     return f'{first_name[0].lower()}.{last_name.lower()}'


print(calculate_age("1990-05-15"))
print(filter_adults(users_data))
print(generate_username("John", "Doe"))




