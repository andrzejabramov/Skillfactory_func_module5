def create_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter



counter = create_counter()
print(counter())  # вернет "1"
print(counter())  # вернет "2"
print(counter())  # вернет "3"