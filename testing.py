# # class User:
# #     def __init__(self, id, name, active):
# #         self.id = id
# #         self.name = name
# #         self.active = active
        

# # from dataclasses import dataclass

# # @dataclass
# # class User:
# #     id:int
# #     name:str
# #     is_active: bool=True

# # user = User(19, 'Kristofer')
# # print(user.name )
# from abc import ABC, abstractmethod
# class Worker(ABC):
#     def __init__(self, post):
#         self.post = post
#     @abstractmethod
#     def work(self):
#         print('in process...')

# class BasicWorker(Worker):
#     def work(self):
#         print('Basic work in process...')
# class Director(Worker):
#     def work(self):
#         print('Not working but earning money')

# worker = BasicWorker('Employee')
# director = Director('Director')
# director.work()
# worker.work()

numbers = [
    [
        [

        ],
        [
            [1]
        ]
    ],
    [
        [2],
        [
            [
                [3],
                [3.5]
            ],
            [4]
        ]
    ],
    [5]
]
def print_elements(num):
    for i in num:
        if type(i) == list:
            print_elements(i)
        else:
            print(i)
            
print_elements(numbers)