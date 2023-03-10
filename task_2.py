#  Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]
# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension


from random import randint

def enter_num(message):
    return int(input(message))

def create_string():
    symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    text = ''
    for _ in range (randint(1, 8)):
        text += symbols[randint(0, 51)]
    return text

def separate_by_elements(lst):
    result = []
    result.append(list(filter(lambda i: str(i).isalpha(), lst)))
    result.append(list(filter(lambda i: str(i).isdigit(), lst)))
    return result

def create_list(length):
    lst = []
    for _ in range(length):
        rand = randint(0, 1)
        lst.append(randint(0, 9999) if rand == 0 else create_string())
    return lst