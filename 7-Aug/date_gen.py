from datetime import datetime, timedelta


def date_gen(start, end):

    date_list = []

    start_date = datetime(start[2], start[1], start[0])
    end_date = datetime(end[2], end[1], end[0])

    while start_date != end_date:
        date_list.append(start_date.strftime("%Y-%m-%d"))
        start_date = start_date + timedelta(days = 1)
    date_list.append(end_date.strftime("%Y-%m-%d"))
    
    return date_list


