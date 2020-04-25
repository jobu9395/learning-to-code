"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from numpy import unique

rows = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    for text in texts:
        rows.append(text)

    duplicates = (len(set(rows[0])))

    unique_numbers = len(rows) - duplicates
    print(f"There are {unique_numbers} different telephone numbers in the text records.")


    print(unique(rows))

rows = []

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        rows.append(call)

    duplicates = (len(set(rows[0])))

    unique_numbers = len(rows) - duplicates
    print(f"There are {unique_numbers} different telephone numbers in the  calls records.")


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
