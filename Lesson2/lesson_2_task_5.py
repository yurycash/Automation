def month_to_season(mounth):
    if mounth in [12,1,2]:
        return "Зима"
    elif mounth in [3,4,5]:
        return "Весна"
    elif mounth in [6,7,8]:
        return "Лето"
    elif mounth in [9,10,11]:
        return "Осень"
    else:
        return "Неверный номер месяца"
print (month_to_season(2))
print (month_to_season(3))
print (month_to_season(8))
print (month_to_season(11))
print (month_to_season(99))