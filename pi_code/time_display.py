import datetime
import pytz

tz = pytz.timezone("US/Eastern")

def get_datetime():
    dt = datetime.datetime.now(tz=tz).strftime("%y-%m-%d %H:%M:%S")
    return dt