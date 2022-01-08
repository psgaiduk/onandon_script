from datetime import datetime
from evening import start_evening
from morning import start_morning
from first_start import start_work


start_work()

if datetime.now().hour > 18:
    start_evening()
else:
    start_morning()
