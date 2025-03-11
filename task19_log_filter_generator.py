logs = """\
2023-08-15 14:15:24 INFO Starting the system.
2023-08-15 14:15:26 WARN System load is above 80%.
2023-08-15 14:15:27 ERROR Failed to connect to database.
2023-08-15 14:15:28 INFO Connection retry in 5 seconds.
"""


def log_filter(l, level_logs):
    lstr = logs.split('\n')
    for el in lstr:
        if el and level_logs in el:
            yield el.strip()

for log in log_filter(logs, 'ERROR'):
   print(log)