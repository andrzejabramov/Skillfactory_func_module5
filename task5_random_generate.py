import random


first_names = ["Alice", "Bob", "Charlie"]
last_names = ["Smith", "Johnson", "Williams"]


def generate_user_data(count_res, first_names, last_names, list_age):
    for i in range(count_res):
        yield (first_names[random.randint(0, len(first_names)-1)],
               last_names[random.randint(0, len(last_names)-1)],
               random.randint(list_age[0], list_age[-1]))

def generate_user_data1(count, first_names, last_names, age_diapason):
   for _ in range(count):
       name = random.choice(first_names)
       surname = random.choice(last_names)
       age = random.randint(age_diapason[0], age_diapason[1])
       yield name, surname, age


user_data_generator = generate_user_data(5, first_names, last_names, [18, 60])
for user in user_data_generator:
   print(user)