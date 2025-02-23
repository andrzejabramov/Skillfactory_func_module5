first_names = ["Alice", "Bob", "Charlie"]
last_names = ["Smith", "Johnson", "Williams"]


def generate_user_data(count_res, first_names, last_names, list_age):
    for first_name in first_names:
        for last_name in last_names:
            yield first_name, last_name


user_data_generator = generate_user_data(5, first_names, last_names, [18, 60])
for user in user_data_generator:
   print(user)