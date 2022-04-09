from i2cDisplay import * 

from datetime import datetime

while True:
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    write(20, 20, time)

