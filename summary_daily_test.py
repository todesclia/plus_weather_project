from datetime import datetime

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    # check there is weather data
    if weather_data != []:
        summaries = []

        # iterate through the weather data
        for each_row in weather_data:
            date, low, high = each_row
            min_temp = low
            max_temp = high
            days_date = date
    
            # conver the temp from fahrenheit to celsius
            min_low_celsius = (min_temp - 32) * 5.0 / 9.0
            max_high_celsius = (max_temp - 32) * 5.0 / 9.0

            # Format the dates using strftime()
            formatted_date = datetime.fromisoformat(days_date).strftime('%A %d %B %Y')

            # Prepare the final summary string
            # ---- Sunday 21 June 2020 ----
            #   Minimum Temperature: 14.4°C
            #   Maximum Temperature: 22.2°C

            summary = (
                f"--- {formatted_date} ----\n"
                f"Minimum Temperature: {min_low_celsius:.1f}°C.\n"
                f"Maximum Temperature: {max_high_celsius:.1f}°C.\n"
            )
            summaries.append(summary)
    else:
        return ()

    return summaries

example_one = [
["2021-07-02T07:00:00+08:00", 49, 67],
["2021-07-03T07:00:00+08:00", 57, 68],
["2021-07-04T07:00:00+08:00", 56, 62],
["2021-07-05T07:00:00+08:00", 55, 61],
["2021-07-06T07:00:00+08:00", 53, 62]
]
print(generate_daily_summary(example_one))