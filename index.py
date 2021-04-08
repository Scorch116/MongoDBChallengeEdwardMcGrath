#importing json
import json
import code


#accessing JSON file with open file object.
with open ('code.json') as j:
    data = json.load(j)

# object accessed
print(data)


