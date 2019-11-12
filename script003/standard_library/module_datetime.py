# https://docs.python.org/3/library/datetime.html
from time import sleep
from datetime import datetime
start = datetime.now()
sleep(5)
finish = datetime.now()
delta = finish - start

type(start), type(finish), type(delta)
finish == delta + start
start.strftime("%Y-%m-%d")
new_date = datetime.strptime("2015-05-11", "%Y-%m-%d")



