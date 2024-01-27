import datetime
from datetime import datetime   
from datetime import timedelta

now = datetime.now()
date_first_invite = now.strftime("%Y-%m-%d")
dateobject_first=datetime.strptime(date_first_invite, "%Y-%m-%d")
date_first= dateobject_first.date()
print(f"Hello, user. Nice to see you) \nToday is {date_first_invite}")

while True:   
    some_date = input("________Let\'s start to calculate________ \nPlease, enter some date in format: YYYY-MM-DD \n")
    if len(some_date) !=10:
        input('Is something wrong? Try again:\n___')    
        # оброблення введених даних і перевірка на правильний формат
    break

# створення датаоб'єкту
dateobjects_entered = datetime.strptime(some_date, '%Y-%m-%d')
data_second = dateobjects_entered.date() 

def get_days_from_today():
    difference = (date_first.toordinal()-data_second.toordinal() )
    return difference

print (f"It\'s about {get_days_from_today()} days")