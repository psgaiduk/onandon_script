from sound_func import small_beep, long_beep, last_second
from usual_func import countdown, clear_window
import time
import json
import os


def vdoh_vidoh(text, time_, period_time):
    print(text)
    small_beep()
    time.sleep(time_)
    return period_time + time_

with open(os.path.join("data.json"), encoding='utf-8') as file:
    data = json.load(file)

TIME_MEDITATION = data['TIME_MEDITATION']
TIME_AFRIMACII = data['TIME_AFRIMACII']
TIME_VISUAL = data['TIME_VISUAL']
TIME_EXSERSICE = 42
TIME_RELAX = 7
TIME_VDOH = 5
TIME_NO = 3
TIME_VIDOH = 5
TIME_SAMORASVITIE = data['TIME_SAMORAZVITIE']

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


def start_morning():
    os.system("mode 50,20'")
    input('Выпей стакан воды, жми enter')
    input('Водные процедуры, жми enter')
    input('Заправь постель, enter')

    print('Поехали')
    print()
    input('Время медитации, чтобы начать жми enter')
    time_meditation = TIME_MEDITATION
    time_period = 0
    clear_window()
    while time_period < time_meditation:
        print()
        time_period = vdoh_vidoh(text_vdoh, TIME_VDOH, time_period)
        clear_window()
        time_period = vdoh_vidoh(text_no, TIME_NO, time_period)
        clear_window()
        time_period = vdoh_vidoh(text_vidoh, TIME_VIDOH, time_period)
        clear_window()

    long_beep()
    print()
    input('Аффирмации, чтобы начать жми enter')
    print(data['AFRIMACII'])
    time.sleep(TIME_AFRIMACII)
    print()
    long_beep()
    input('Визуализация, чтобы начать жми enter')
    time.sleep(TIME_VISUAL)
    long_beep()
    print()
    input('Тренировка, чтобы начать жми enter')
    exersise = data['EXERCISE']
    for ex in exersise:
        print('Готовься - далее', ex)
        time.sleep(TIME_RELAX)
        last_second()
        long_beep()
        print('Делаем -', ex)
        time.sleep(TIME_EXSERSICE)
        last_second()
        long_beep()
    print()
    countdown(TIME_SAMORASVITIE, 'Саморазвите')
    print()
    input("Заполни дневник")
    input('Ты всё сделал, жми enter')


if __name__ == '__main__':
    start_morning()
