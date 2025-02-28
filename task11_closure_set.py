def create_unique_checker():
    s = set()
    def trans(number):
        if number in s:
            return False
        else:
            s.add(number)
            return True
    return trans


unique_checker = create_unique_checker()
print(unique_checker(5))
print(unique_checker(5))
print(unique_checker(10))

# True
# False
# True