#!/usr/bin/env python3

import datetime


def return_info(start_date, end_date, date_format="%d_%m_%Y"):
    success = 0
    failure = 0
    start = datetime.datetime.strptime(start_date, date_format)
    end = datetime.datetime.strptime(end_date, date_format)
    paths = []
    for i in range((end - start).days + 1):
        name = (
            "logs/log_"
            + (start + datetime.timedelta(days=i)).strftime(date_format)
            + ".log"
        )
        paths.append(name)
    for log in paths:
        with open(log, "r") as file:
            lines = file.readlines()
            for line in lines:
                message_type = line[26:].split()[0]
                if message_type == "INFO":
                    success += 1
                else:
                    failure += 1
    return success, failure


start = "02_12_2024"
end = "05_12_2024"
sucess, failures = return_info(start, end)
print(sucess)
print(failures)
