from datetime import date, timedelta, datetime

from sound_func import small_beep, long_beep, last_second
from usual_func import countdown, clear_window
from data import return_settings
import time
import json
import os


def vdoh_vidoh(text, time_, period_time):
    print(text)
    small_beep()
    time.sleep(time_)
    return period_time + time_

text_vdoh = '''
╔══╗──╔══╗─╔══╗╔══╗╔══╗
║╔╗║──║╔╗║─║╔╗║╚═╗║║╔═╝
║╚╝╚╗─║║║║─║║║║──║╚╝║──
║╔═╗║─║║║║─║║║║──║╔╗║──
║╚═╝║╔╝╚╝╚╗║╚╝║╔═╝║║╚═╗
╚═══╝╚════╝╚══╝╚══╝╚══╝
'''

text_no = '''
╔╗╔╗╔═══╗────╔══╗─╔╗──╔╗╔╗╔╗╔╗╔╗╔╗
║║║║║╔══╝────║╔╗║─║║──║║║║║║║║║║║║
║╚╝║║╚══╗────║║║║─║╚══╣║║║║║║║║║║║
║╔╗║║╔══╝────║║║║─║╔═╗║║║║║║║║║║╔║
║║║║║╚══╗───╔╝╚╝╚╗║╚═╝║║║╚╝╚╝║║╚╝║
╚╝╚╝╚═══╝───╚════╝╚═══╩╝╚════╝╚══╝
'''

text_vidoh = '''
╔══╗─╔╗──╔╗─╔══╗─╔══╗╔══╗╔══╗
║╔╗║─║║──║║─║╔╗║─║╔╗║╚═╗║║╔═╝
║╚╝╚╗║╚══╣║─║║║║─║║║║──║╚╝║──
║╔═╗║║╔═╗║║─║║║║─║║║║──║╔╗║──
║╚═╝║║╚═╝║║╔╝╚╝╚╗║╚╝║╔═╝║║╚═╗
╚═══╝╚═══╩╝╚════╝╚══╝╚══╝╚══╝
'''


def meditation(time_morning, time_inhale, time_delay, time_exhalation):
    print()
    input('Время медитации, чтобы начать жми enter')
    time_period = 0
    clear_window()
    while time_period < time_morning:
        print()
        time_period = vdoh_vidoh(text_vdoh, time_inhale, time_period)
        clear_window()
        time_period = vdoh_vidoh(text_no, time_delay, time_period)
        clear_window()
        time_period = vdoh_vidoh(text_vidoh, time_exhalation, time_period)
        clear_window()
    long_beep()


def affirmation(affirmations, time_morning):
    print()
    input('Аффирмации, чтобы начать жми enter')
    print(affirmations)
    time.sleep(time_morning)
    long_beep()


def visualisation(time_morning):
    print()
    input('Визуализация, чтобы начать жми enter')
    time.sleep(time_morning)
    long_beep()


def make_exercises(exercises, time_relax, time_exercises):
    print()
    input('Тренировка, чтобы начать жми enter')
    for ex in exercises:
        for ex_name, ex_info in ex.items():
            print('Готовься - далее', ex_name)
            print(ex_info)
            time.sleep(time_relax)
            last_second()
            long_beep()
            print('Делаем -', ex_name)
            time.sleep(time_exercises)
            last_second()
            long_beep()
            clear_window()


def start_morning(type_work='usual'):
    with open('settings_user.json', encoding='utf-8') as file:
        user_settings = json.load(file)

    print(user_settings)
    user_level = user_settings['level']
    affirmations = user_settings['affirmations']
    name_growing = user_settings['name_growing']

    all_data = return_settings(user_level, type_work)
    time_morning = all_data["time_morning"]
    time_self_development = all_data["time_self_development"]
    exercises = all_data["exercises"]
    time_exercises = all_data["time_exercises"]
    time_relax = all_data["time_relax"]
    time_inhale = all_data["time_inhale"]
    time_delay = all_data["time_delay"]
    time_exhalation = all_data["time_exhalation"]

    with open('history_user_morning.json', encoding='utf-8') as file:
        history = json.load(file)

    if history:
        last_series = history[-1]
        last_date = datetime.strptime(last_series[-1], '%Y-%m-%d').date()
        days_missed = (date.today() - last_date).days - 1
        if days_missed > 0:
            user_level -= days_missed
            if user_level < 1:
                user_level = 1
        else:
            if len(last_series) == 10:
                user_level += 1
                print(f'Поздравляю у тебя новый уровень {user_level}')
                history.append([])
                last_series = history[-1]

    else:
        history.append([])
        last_series = history[-1]

    print(history)
    input('Выпей стакан воды, жми enter')
    make_exercises(exercises, time_relax, time_exercises)
    countdown(50, 'Обучение')
    input('Водные процедуры, жми enter')
    input('Заправь постель, enter')
    countdown(50, 'Обучение')
    meditation(180, time_inhale, time_delay, time_exhalation)
    input("Пройди план на Puzzle English")
    print()
    input("Заполни ZenMoney")
    input('Ты всё сделал, жми enter')

    date_str = date.today().strftime("%Y-%m-%d")
    if date_str not in last_series:
        last_series.append(date_str)
    else:
        print('Сегодня ты уже занимался, это занятие не влияет на уровень')

    user_settings['level'] = user_level

    print(user_settings)
    with open('history_user_morning.json', 'w', encoding='utf-8') as file_history, \
            open('settings_user.json', 'w', encoding='utf-8') as setting_user:
        json.dump(history, file_history)
        json.dump(user_settings, setting_user)


if __name__ == '__main__':
    start_morning('test')
