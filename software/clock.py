try:
	from i2cDisplay import *
except:
	from spiDisplay import *

from datetime import datetime

def clock():
    """
    Print time to display

    Returns
    -------
    None.

    """
    
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    write(7, 2, time)

