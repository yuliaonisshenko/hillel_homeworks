import re

camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = []
for var_name in camel_case_list:
    snake_case_name = re.sub(r'(?<!^)(?=[A-Z])', '_', var_name).lower()
    snake_case_list.append(snake_case_name)
print(snake_case_list)

