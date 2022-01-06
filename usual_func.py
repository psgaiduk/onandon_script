from sound_func import small_beep, long_beep, last_second
import time


def countdown(time_minutes, text):
    input(f'{text} {time_minutes} минут, жми enter')
    need_times = [time_minutes // i for i in range(2, 5)]
    for i in range(time_minutes):
        print(f'{time_minutes - i} минут осталось')
        time.sleep(60)
        if i in need_times:
            small_beep()
        if i == 1:
            last_second()
    long_beep()
    print()


def next_step(text):
    input(f'{text}, чтобы продолжить жми enter')
    print()
