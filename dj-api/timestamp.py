import datetime

# Convert ClickUp timestamp to human-readable date
timestamp = 1728292144264 / 1000  # ClickUp timestamps are in milliseconds, so divide by 1000
readable_date = datetime.datetime.utcfromtimestamp(timestamp).isoformat() + 'Z'

print(readable_date)

