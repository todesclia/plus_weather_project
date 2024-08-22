from datetime import datetime

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp_in_celcius = (temp_in_fahrenheit - 32) * 5.0 / 9.0
    return(round(temp_in_celcius, 1))

temp_in_fahrenheit = 49
print(convert_f_to_c(temp_in_fahrenheit))