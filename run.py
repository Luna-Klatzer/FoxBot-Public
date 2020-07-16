#normal imports
import sys
import os
import runpy
from datetime import datetime
from datetime import date

#specifying the time
now = datetime.now()
date_now = date.today
def ctime():
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return current_time
current_time = ctime()

try:
    #running the main file and starting the process
    file_globals = runpy.run_path("./FoxBot/main.py")
except Exception as e:
    #printing out the error-time, message and reason
    print(f"{current_time} CRITICAL ERROR RUN.PY FAILED DUE TO {e}")