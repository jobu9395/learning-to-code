"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

rows = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    for text in texts:
        rows.append(text)

    first_row = (rows[0])
    # print(first_row)

    incoming_number = first_row[0]
    answering_number = first_row[1]
    time = first_row[2]

    print(f"First record of texts, {incoming_number} texts {answering_number} at time {time}")

calls_rows = []

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        calls_rows.append(call)

    last_row = calls_rows[-1]
    # print(last_row)

    incoming_number = last_row[0]
    answering_number = last_row[1]
    time = last_row[2]
    duration = last_row[3]

    print((f"Last record of calls, {incoming_number} calls {answering_number} at time {time} lasting {duration} seconds"))


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

