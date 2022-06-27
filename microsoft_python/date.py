from datetime import datetime, timedelta
current_date = datetime.now()
print("current day is"+str(current_date))

one_day = timedelta(days=1)
print("yesterday is "+str(current_date-one_day))

print("current_month"+str(current_date.month))
print("current_year "+str(current_date.year))
print("current_day"+str(current_date.day))
print("current_hour "+str(current_date.hour))
print("current_minute"+str(current_date.minute))
print("current_second"+str(current_date.second))

birthdate = datetime.strptime("22/11/2022", "%d/%M/%Y")
print(str(birthdate))
