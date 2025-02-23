def generate_urls(url, start, stop):
    for i in range(start, stop+1):
        yield f'{url}{i}'

url_generator = generate_urls("/product/", 1, 3)
for url in url_generator:
    print(url)

# def generate_test_data(n):
#    for i in range(n):
#        yield f"test_data_{i}"