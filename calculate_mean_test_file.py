from datetime import datetime

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
                total_temp += each_item

        # calculate averages
        avg_temp = total_temp / len(weather_data)

        # conver the temp from fahrenheit to celsius           
        avg_temp_celcius = (float(avg_temp) - 32) * 5.0 / 9.0 
        return(avg_temp_celcius)

temperatures = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]
print(calculate_mean(temperatures))