def find_min(weather_data):
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

weather_data = []
print(find_min(weather_data))