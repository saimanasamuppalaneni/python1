# months
import calendar
for i in range (1,13):
    res = calendar.month_name[i]
    print("Month name : " + str(res))
    print(calendar.month(2025,i))