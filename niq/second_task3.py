from datetime import datetime

def format_date_decorator(func):
    def wrapper(*args, **kwargs):
        date = func(*args, **kwargs)
        return date.strftime('%Y-%m/%d')
    return wrapper

@format_date_decorator
def get_first_day_of_last_week():
    today = datetime.now()

    if today.month == 12:
        first_day_next_month = datetime(year=today.year + 1, month=1, day=1)
    else:
        first_day_next_month = datetime(year=today.year, month=today.month + 1, day=1)

    last_day_current_month = first_day_next_month - datetime.resolution
    last_week_start_day = last_day_current_month.day - last_day_current_month.weekday()
    first_day_last_week = last_day_current_month.replace(day=last_week_start_day)
    return first_day_last_week

print(get_first_day_of_last_week())