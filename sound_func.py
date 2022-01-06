from playsound import playsound
import time


def small_beep():
    playsound('small.wav')


def long_beep():
    playsound('finish.wav')


def last_second():
    for _ in range(3):
        playsound('small.wav')
        time.sleep(0.8)

