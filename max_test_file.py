def find_max(weather_data):
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

weather_data = [49, 57, 56, 55, 57]
print(find_max(weather_data))