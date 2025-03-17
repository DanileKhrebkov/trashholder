import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename='main.log',
    filemode='a',
    encoding='UTF-8'
)

logging.debug('Дебаг мэсседж')

def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError as e:
        logging.error(f'ошибка деления на 0: {e}')
        return None
    else:
        logging.info(f'результат: {result}')
        return result
    
# print("10/2", divide(10,2))
# print("10/0", divide(10,0))
def mult_string(s:str, num:int):
    try:
        if type(num) is int:
            logging.info("тип данных верен")
            return s * int(num)
        if num.isdigit():
            logging.warning("ТД верен, но строка из чисел")
            return s * int(num)
    except AttributeError as e:
        logging.error(f'Тип данных неверный, ошибка {e}')
        

mult_string('hello', '2')
mult_string('hello', 2)
mult_string('hello', [])