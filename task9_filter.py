phone_list = [
    '123-456-7890',
    '123.456.7890',
    '(123) 456-7890',
    '+1234567890',
    '1234567890'
]


def format_phone_number(number):
    return "".join(filter(lambda x: x.isdigit(), number))

formatted_numbers = list(map(lambda number: format_phone_number(number), phone_list))
print(formatted_numbers)







