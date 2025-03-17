import json
from dataclasses import dataclass


# date={
#     'name':'khrist',
#     'age': 55,
#     'city':'New York'
# }

# # json_data = json.dumps(date)

# # print(json_data)



# # date2 = json.loads(json_data)
# # print(date2)


# with open('data.json', 'w', encoding='UTF-8') as file:
#     json.dump(date, file)



# with open('data.json', 'r', encoding='UTF-8') as file:
#     data = json.load(file)
#     print(data)


@dataclass
class Person:
    name:str
    age:int
    
    def serialize(self):
        return json.dumps(self.__dict__, indent=1)
obj = Person('anton', 15)
print(obj.serialize())