from datetime import datetime

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    # check there is weather data
    if weather_data != []:

        # initialize variables
        min_low = weather_data[0][1]
        min_low_date = weather_data[0][0]
        max_high = weather_data[0][2]
        max_high_date = weather_data[0][0]
        total_low = 0
        total_high = 0
        number_of_days = len(weather_data)

        # iterate through the weather data
        for each_row in weather_data:
            if each_row != []:
                date, low, high = each_row
                # update min low temp and date
                if low < min_low:
                    min_low = low
                    min_low_date = date
                # update max high temp and date
                if high > max_high:
                    max_high = high
                    max_high_date = date
                # accumulate the totals for average calc
                total_low += low
                total_high += high
        # calculate averages
        avg_low = total_low / len(weather_data)
        avg_high = total_high / len(weather_data)

        # conver the temp from fahrenheit to celsius
        min_low_celsius = (min_low - 32) * 5.0 / 9.0
        max_high_celsius = (max_high - 32) * 5.0 / 9.0  
        avg_low_celsius = (avg_low - 32) * 5.0 / 9.0            
        avg_high_celsius = (avg_high - 32) * 5.0 / 9.0            
        # Format the dates using strftime()
        min_low_date_formatted = datetime.fromisoformat(min_low_date).strftime('%A %d %B %Y')
        max_high_date_formatted = datetime.fromisoformat(max_high_date).strftime('%A %d %B %Y')
        # Prepare the final summary string
        summary = (
            f"{number_of_days} Day Overview\n"
            f"The lowest temperature will be {min_low_celsius:.1f}°C, and will occur on {min_low_date_formatted}.\n"
            f"The highest temperature will be {max_high_celsius:.1f}°C, and will occur on {max_high_date_formatted}.\n"
            f"The average low this week is {avg_low_celsius:.1f}°C.\n"
            f"The average high this week is {avg_high_celsius:.1f}°C."
        )
    else:
        return ()

    return summary

example_one = [
["2020-06-19T07:00:00+08:00",-47,-46],
["2020-06-20T07:00:00+08:00",-51,67],
["2020-06-21T07:00:00+08:00",58,72],
["2020-06-22T07:00:00+08:00",59,71],
["2020-06-23T07:00:00+08:00",-52,71],
["2020-06-24T07:00:00+08:00",52,67],
["2020-06-25T07:00:00+08:00",-48,66],
["2020-06-26T07:00:00+08:00",53,66]
]
print(generate_summary(example_one))