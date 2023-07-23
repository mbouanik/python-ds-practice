def weekday_name(day_of_week):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wenesday', 'Thurday', 'Friday', 'Saturday']
    day_of_week -= 1
    if day_of_week >= 0 and day_of_week <= 6:
        return days[day_of_week]
    return None
