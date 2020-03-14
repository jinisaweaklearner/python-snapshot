import datetime

def calculate_time_delta(hour):
    time_now = datetime.datetime.now() 
    time_next_job =datetime.datetime(time_now.year, time_now.month, time_now.day, hour, 0)
    return (time_next_job-time_now).seconds
