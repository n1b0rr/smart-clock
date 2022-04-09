from i2cDisplay import * 

import time

from datetime import datetime

start = time.time()
while True:
    interval = round(time.time() - start)
    hours = int(interval/3600)
    minutes = int((interval - (hours*3600))/60)
    seconds = int(interval - (hours*3600) - (minutes*60))
    write(20, 20, "{:0>2}".format(hours) + ":" + "{:0>2}".format(minutes) + ":" + "{:0>2}".format(seconds))

