"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""


import csv

rows = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        rows.append(call)

    longest_duration = 0
    phone_number = ""

    for item in rows:
        duration = int(item[3])

        if duration > longest_duration:
            longest_duration = duration
            phone_number = item[0]


    print(f"{phone_number} spent the longest time, {longest_duration} seconds, on the phone during September 2016.")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

