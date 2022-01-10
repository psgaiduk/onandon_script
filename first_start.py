import os.path
import json
from datetime import date


def check_file(name):
    have_file = os.path.exists(name)
    if not have_file:
        with open(name, 'w+'):
            pass
        return False

    return True


def start_work():
    was_file = check_file('history_user_morning.json')
    if not was_file:
        with open('history_user_morning.json', 'w+', encoding='utf-8') as file:
            data = []
            json.dump(data, file)
    check_file('history_user_evening.json')
    was_file = check_file('settings_user.json')
    if not was_file:
        name_user = input('Введите ваше имя: ')
        affirmacii = input('Введите ваши аффирмации через, разделяя их ; ')
        name_growing = input('Введите как вы будете саморазвиваться по утрам (чтение, решение задача и т.д.) ')
        name_art = input('Введите каким творчеством вы будете заниматься по вечерам (рисование, музыка и т.д.) ')
        with open('settings_user.json', 'w+', encoding='utf-8') as file:
            data = {
                'name_user': name_user,
                'affirmations': affirmacii.split(';'),
                'name_growing': name_growing,
                'name_art': name_art,
                'date_start': date.today().strftime('%Y-%m-%d'),
                'level': 0
            }
            json.dump(data, file)
