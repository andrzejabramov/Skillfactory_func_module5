categories = {
   "Электроника": {
       "Телефоны": {
           "Смартфоны": {},
           "Проводные": {}
       },
       "Компьютеры": {
           "Ноутбуки": {},
           "Стационарные": {
               "Игровые": {},
               "Для работы": {}
           }
       }
   },
   "Одежда": {
       "Мужская": {
           "Джинсы": {},
           "Куртки": {}
       }
   }
}


def extract_categories(category_dict, parent_path=''):
   paths = []
   for category, subcategories in category_dict.items():
       current_path = f"{parent_path} > {category}" if parent_path else category
       paths.append(current_path)
       paths.extend(extract_categories(subcategories, current_path))
   return paths


paths = extract_categories(categories)
for path in paths:
    print(path)