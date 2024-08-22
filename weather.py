import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    formatted_date = datetime.fromisoformat(iso_string).strftime('%A %d %B %Y')
    return(formatted_date)


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp_in_celcius = (float(temp_in_fahrenheit) - 32) * 5.0 / 9.0
    return(round(temp_in_celcius, 1))


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # check there is weather data
    if weather_data != []:

        # initialize variables  
        total_temp = 0
        number_of_days = len(weather_data)

        # iterate through the weather data
        for each_item in weather_data:
            if each_item != []:
                total_temp += float(each_item)

        # calculate averages
        avg_temp = total_temp / len(weather_data)
        return(avg_temp)
    else:
        return()


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data_list = []
    
    with open(csv_file, encoding="utf-8") as my_file:
        csv_reader = csv.reader(my_file)
        next(csv_reader) # skip headers (first row)

        for row in csv_reader:
            if row:
                # Convert the second and third elements to str
                processed_row = [row[0], int(row[1]), int(row[2])]
                data_list.append(processed_row)

    return(data_list)


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if weather_data != []:
        #initialise the variables before entering the loop
        minimum_value = weather_data[0]
        position = 0
        # loop through each item and check if it is smaller than the current min value
        for index, weather_item in enumerate(weather_data):

            #if this is true then set the min value to the new item in the list and set the position
            if weather_item <= minimum_value:
                    minimum_value = weather_item
                    position = index
        # set the result to the min value and its position
        result = (float(minimum_value), position)
    else:
        result = ()
    #return the result
    return result

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if weather_data != []:
        #initialise the variables before entering the loop
        maximum_value = weather_data[0]
        position = 0
        # loop through each item and check if it is greater than the current max value
        for index, weather_item in enumerate(weather_data):

            #if this is true then set the max value to the new item in the list and set the position
            if weather_item >= maximum_value:
                    maximum_value = weather_item
                    position = index
        # set the result to the max value and its position
        result = (float(maximum_value), position)
    else:
        result = ()
    #return the result
    return result
    
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
        f"{number_of_days} Day Overview\n  The lowest temperature will be {min_low_celsius:.1f}°C, and will occur on {min_low_date_formatted}.\n  The highest temperature will be {max_high_celsius:.1f}°C, and will occur on {max_high_date_formatted}.\n  The average low this week is {avg_low_celsius:.1f}°C.\n  The average high this week is {avg_high_celsius:.1f}°C.\n"
        )
    else:
        return ()

    return summary


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
                f"---- {formatted_date} ----\n "
                f" Minimum Temperature: {min_low_celsius:.1f}°C\n"
                f"  Maximum Temperature: {max_high_celsius:.1f}°C\n"
            ) 
            summaries.append(summary)
            final_summary = "\n".join(summaries)
            final_summary = final_summary + "\n"

    else:
        return ()

    return final_summary
