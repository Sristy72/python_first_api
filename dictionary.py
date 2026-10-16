user_dictionary = {
    "user1" : 'eshita',
    "user2" : 'shita',
    "user3" : 'hddj',
}
user_dictionary["married"] = True
print(user_dictionary)
print(user_dictionary["user1"])
print(len(user_dictionary))
user_dictionary.pop("user2")
print(user_dictionary)

for x , y in user_dictionary.items():
    print(x, y)

user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop('user3')
print(user_dictionary2)
print(user_dictionary)