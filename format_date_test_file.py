from datetime import datetime

def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    formatted_date = datetime.fromisoformat(iso_string).strftime('%A %d %B %Y')
    return(formatted_date)

iso_string = "2021-07-02T07:00:00+08:00"
print(convert_date(iso_string))