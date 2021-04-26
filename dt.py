import datetime

DELTA = 0.25*10**6
t1 = datetime.datetime.now()
t2 = t1 + datetime.timedelta(milliseconds=3)
D = t2 - t1

compter = 0
while True:
    if D.microseconds > DELTA:
        t1 = t2
        print(f"delta = {D.microseconds}")
        compter += 1
    if compter > 10:
        break
    t2 = datetime.datetime.now()
    D = t2 - t1


print(D.microseconds)