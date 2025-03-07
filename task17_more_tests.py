from typing import List, Dict, Any
# А также вам наверняка может понадобиться модуль functools...


users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'},
             {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22', 'email': 'bobJ@gmail.com'},
             {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01', 'email': 'lev46@gmail.com'}]

users_data_ext = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'}]


def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
    result_list = []
    for i in users:
        result_list.append(i['first_name']+' '+i['last_name'])
    return result_list

def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set:
    set_users_data, set_users_ext = set(), set()
    for el in users1:
        set_users_data.add(el['email'])
    set_users_ext.add(users2[0]['email'])
    set_intersept = set_users_data & set_users_ext
    return set_intersept

def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    result_dict, d = {}, {}
    l = []
    for i in range(len(users)):
        d = d | users[i]
        #d = {**d, **users[i]}
    for n in d.keys():
        for el in users:
            if el.get(n):
                l.append(el[n])
            else:
                l.append(None)
        t = tuple(l)
        #result_dict = result_dict | {n: t}
        result_dict = {**result_dict, **{n: t}}
        l = []
    return result_dict

to_test = [convert_to_full_name(users_data), find_matching_emails(users_data, users_data_ext), combine_user_data(users_data)]
# print(convert_to_full_name(users_data))
# print(find_matching_emails(users_data, users_data_ext))
# print(combine_user_data(users_data))
print(to_test)

# from typing import List, Dict, Any
# from functools import reduce
#
# def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
#     full_names = list(map(lambda user: f"{user['first_name']} {user['last_name']}", users))
#     return full_names
#
# def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set:
#     emails1 = set(map(lambda user: user['email'], users1))
#     emails2 = set(map(lambda user: user['email'], users2))
#     matching_emails = emails1.intersection(emails2)
#     return matching_emails
#
# def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
#     keys = users[0].keys()
#     combined_data = dict(zip(keys, zip(*[user.values() for user in users])))
#     return combined_data
