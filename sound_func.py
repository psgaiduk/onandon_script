import winsound
import time

def small_beep():
    frequency = 2000  # Set Frequency To 2500 Hertz
    duration = 200  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def long_beep():
    frequency = 1000  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def last_second():
    for _ in range(3):
        small_beep()
        time.sleep(0.8)

