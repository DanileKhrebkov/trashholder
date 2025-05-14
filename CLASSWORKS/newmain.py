from typing import List, Dict, Optional

# def process_list(items:list) -> dict[str, int]:
#     total = sum(items)
#     count = len(items)
#     return {'total': total, 'count':count}

# result = process_list([1,2,3,4,5])
# print(result)

#///////////////////////////////////////////////////

# students = ['Oleg', 'Kirill', 'Konstantin']

# def search_student(list: list[str], target: str) ->Optional[str]:
#     for student in list:
#         if student == target:
#             return student
#     return None

# r = search_student(students, 'Vlad')
# print(r) 

#/////////////////////////////////////////////////////
# def counter(count):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print('Что то перед')
#             result = func(*args, **kwargs)
#             print(count)
#             print('Что то после')
#             return result

#         return wrapper
#     return decorator

# @counter(4)
# def sum(a,b): return a + b 

# print(sum(1,2))

#//////////////////////////////////////////////////////

# from decorator import decorator
# @decorator
# def debug(func, *args, **kwargs):
#     print(f'Вызов функции: {func.__name__}, аргументы:{args}, {kwargs}')
#     result = func(*args, **kwargs)
#     print(f'result: {result}')
#     return result

# @debug
# def substract(a,b):
#     return a - b

#/////////////////////////////////////////////////////////

import functools