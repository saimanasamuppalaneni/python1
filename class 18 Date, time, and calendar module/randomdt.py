import random
import datetime
def random_date(start,end):
    random_sec=random.randint(0,int((end-start).total_seconds()))
    rdate=datetime.timedelta(seconds=random_sec)
    return start+rdate
start=datetime.datetime(2020,1,1)
end=datetime.datetime(2023,1,1)
rdate=random_date(start,end)
print(rdate.date())