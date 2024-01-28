import datetime
from datetime import datetime   
from datetime import timedelta

now = datetime.now() #використання datatime для ствоорення дати в реальному часі
date_first_invite = now.strftime("%Y-%m-%d") #перетворення дати в рядок для вступної частини програми
dateobject_first=datetime.strptime(date_first_invite, "%Y-%m-%d") #створення datatime об'єкту у заданому форматі
date_first= dateobject_first.date() #створення дата об'єкту без інформації про час
print(f"Hello, user. Nice to see you) \nToday is {date_first_invite}") #рядок-привітання з актуальною датою

while True:   #створення циклу для вводу рядка дати
    try:
        some_date = input("________Let\'s start to calculate________ \nPlease, enter some date in format: YYYY-MM-DD \n")
    except ValueError:
        print('Будь-ласка, введіть коректну дату')
    except Exception:
        input('Is something wrong?') 
    if len(some_date) !=10: # оброблення введених даних і перевірка на правильний формат
        input('Неправильний формат? Try again:\n___ ')    
    break

# створення і форматування датаоб'єкту
dateobjects_entered = datetime.strptime(some_date, '%Y-%m-%d')
data_second = dateobjects_entered.date() 

def get_days_from_today():    #створення функції для обрахування різниці між двома датами
    difference = (date_first.toordinal()-data_second.toordinal() )
    return difference
#виведення реезультату
print (f"It\'s about {get_days_from_today()} days")