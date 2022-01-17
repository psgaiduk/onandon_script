from sound_func import small_beep, long_beep, last_second
import time
import os


def add_spaces(text, max_len):
    if len(text) < max_len:
        need_spaces = (max_len - len(text)) // 2
        text = ''.join([' ' * need_spaces, text, ' ' * need_spaces])

    return text


def countdown(time_minutes, text):
    print()
    input(f'{text} {time_minutes} минут, жми enter')
    need_times = [time_minutes // 4, time_minutes // 2, time_minutes - time_minutes // 4]
    second_text = 'осталось минут'
    max_len = max([len(text), len(second_text), len(str(time_minutes)) * 4])
    text = add_spaces(text, max_len)
    second_text = add_spaces(second_text, max_len)
    print(need_times)
    for i in range(time_minutes):

        print(f'{text}')
        print(f'{second_text}')
        print(f'{return_number(time_minutes - i, max_len)}')
        time.sleep(60)
        if i in need_times:
            small_beep()
        if i == time_minutes - 2:
            last_second()
        clear_window()
    long_beep()
    print()


def next_step(text):
    input(f'{text}, чтобы продолжить жми enter')
    print()


all_numbers = [
    '╔══╗─╔═╗╔══╗╔══╗╔╗╔╗╔══╗╔══╗╔══╗╔══╗╔══╗',
    '║╔╗║╔╝ ║╚═╗║╚═╗║║║║║║╔═╝║╔═╝╚═╗║║╔╗║║╔╗║',
    '║║║║╚╗ ║╔═╝║╔═╝║║╚╝║║╚═╗║╚═╗──║║║╚╝║║╚╝║',
    '║║║║─║ ║║╔═╝╚═╗║╚═╗║╚═╗║║╔╗║──║║║╔╗║╚═╗║',
    '║╚╝║─║ ║║╚═╗╔═╝║──║║╔═╝║║╚╝║──║║║╚╝║╔═╝║',
    '╚══╝─╚═╝╚══╝╚══╝──╚╝╚══╝╚══╝──╚╝╚══╝╚══╝']


def return_number(nums, max_len):
    new_num = ''
    if nums < 10:
        nums = f'0{nums}'
    else:
        nums = str(nums)
    for i in range(6):
        text_num = ''
        for num in nums:
            num = int(num)
            text_num = ''.join([text_num, all_numbers[i][num*4:num*4 + 4]])
        text_num = add_spaces(text_num, max_len)
        new_num = ''.join([new_num, text_num, '\n'])

    return new_num


def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')
