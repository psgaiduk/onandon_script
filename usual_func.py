from sound_func import small_beep, long_beep, last_second
import time

def countdown(time_minutes, text):
    input(f'{text} {time_minutes} минут, жми enter')
    for i in range(time_minutes):
        print(f'{time_minutes - i} минут осталось')
        time.sleep(60)
    long_beep()
    print()

def next_step(text):
    input(f'{text}, чтобы продолжить жми enter')
    print()
