import re

string = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"
pairs = re.findall(r'(\w+)=(\w+)', string)
dictionary = {key: value for key, value in pairs}
print(dictionary)
