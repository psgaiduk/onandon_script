from datetime import datetime
from evening import start_evening
from morning import start_morning

if datetime.now().hour > 18:
    start_evening()
else:
    start_morning()
