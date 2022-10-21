# Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

from random import randrange as RR

def get_pharse(*texts): return input(*texts)

def analyse_pharse(pharses, pharse):
    if pharse.lower() in {'q', 'й', 'stop', 'стоп', 'все', 'всё'}:
        print('HELLO!')
        return False
    if pharse.lower() in pharses:
        print(pharses.get(pharse) [RR(len(pharses.get(pharse)))])
    else:
        pharses[pharse.lower()] = new_pharse()
    return True

def returning(): return

def greeting():
    answers = {
        0: 'Привет!',
        1: 'Здравствуй!',
        2: 'Приветствую!',
        3: 'Приветик!',
        4: 'Добрый день!',
        5: 'Салют!'
    }
print(answers.get(RR(len(answers))))

def new_pharse():
    new_variant = {}
    print('Я не понимаю, скажи 3 варианта ответа на эту фразу: ')
    for i in range(3):
        answer = get_pharse(f'{i + 1} вариант: ')
        new_variant[i] = answer
    return new_variant

def main():
    greeting()
    pharses = {
        'Привет': {
            0: 'Привет!',
        1: 'Здравствуй!',
        2: 'Приветствую!',
        3: 'Приветик!',
        4: 'Добрый день!',
        5: 'Салют!'
    },
    'Как тебя зовут?': {
        0: 'Я - твой личный Бот',
        1: 'Я Бот',
        2: 'Меня зовут Кей',
        3: 'Интеллектуальный Бот'
    },
    }
    chatting = True
    while chatting:
        chatting = analyse_pharse(pharses, get_pharse())

main()