import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp: str):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string: str) -> str:
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # "2024-08-18T14:30:00"
    date_obj = datetime.fromisoformat(iso_string)
    return date_obj.strftime("%A %d %B %Y")

# result_test = convert_date("2024-08-18T14:30:00")
# print(result_test)


def convert_f_to_c(temp_in_fahrenheit: float) -> float:
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """

    temp_in_celsius = (float(temp_in_fahrenheit) - 32) * 5/9
    temp_in_celsius = round(temp_in_celsius, 1)
    return temp_in_celsius


def calculate_mean(weather_data: list) -> float:
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    # the_mean = do cool stuyff, work out the mean weather_data
    # return the_mean
    total_sum = 0
    if len(weather_data) == 0:
        raise ValueError("There are no numbers in the list... We cannot calculate the mean")
    for number in weather_data: 
        total_sum += float(number)
    mean_value = total_sum/ len(weather_data)
    return mean_value

def load_data_from_csv(csv_file: str) -> list:
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data_list = []
    with open(csv_file, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skipping the header row
            for each_row in csv_reader:
                if each_row:
                    # Convert the last two elements to integers or floats
                    each_row[1] = int(each_row[1])
                    each_row[2] = int(each_row[2])
                    data_list.append(each_row)
    return data_list

def find_min(weather_data: list) -> tuple: 
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if len(weather_data) == 0:
        return ()

    min_value = float(weather_data[0])
    min_index = 0

    for i in range(len(weather_data)):
        value = float(weather_data[i])
        if value <= min_value:
            min_value = value
            min_index = i

    return min_value, min_index


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if len(weather_data) == 0:
        return ()

    max_value = float(weather_data[0])
    max_index = 0

    for i in range(len(weather_data)):
        value = float(weather_data[i])
        if value >= max_value:
            max_value = value
            max_index = i

    return max_value, max_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
# I wanto to make a summary of everything I have done before - using a function 
# read though weather data and output a summary 
# for each value in weather data output a string 
# convert_date , figure out how many rows 
# convert to celsius first then send it to calculate mean function 
# create list of max and send it to max function - same with low 

    minimum_temp = []
    maximum_temp = []
    dates = []

    for row in weather_data:
        # convert temperatures from Fahrenheit to Celsius using my function convert_f_to_c --> WILL RETURN A STRING
        min_temp_celsius = convert_f_to_c(row[1])
        max_temp_celsius = convert_f_to_c(row[2])
        
        # Append to lists --> we need to do this to send it to the find_min and Find_max function
        minimum_temp.append(min_temp_celsius)
        maximum_temp.append(max_temp_celsius)
        #converting iso string to readable format
        dates.append(convert_date(row[0]))

    # Find overall min and max temps and corresponding date using the index
    min_temp_value, min_temp_index = find_min(minimum_temp)
    max_temp_value, max_temp_index = find_max(maximum_temp)
    
    min_temp_date = dates[min_temp_index]
    max_temp_date = dates[max_temp_index]

    # Calculate average temperatures --> function requires a list!
    mean_min_temp = calculate_mean(minimum_temp)
    mean_max_temp = calculate_mean(maximum_temp)

    overview = (
        f"{len(weather_data)} Day Overview\n"
        f"  The lowest temperature will be {min_temp_value:.1f}°C, and will occur on {min_temp_date}.\n"
        f"  The highest temperature will be {max_temp_value:.1f}°C, and will occur on {max_temp_date}.\n"
        f"  The average low this week is {mean_min_temp:.1f}°C.\n"
        f"  The average high this week is {mean_max_temp:.1f}°C.\n"
    )

    return overview


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = []

    for row in weather_data:
        
        min_temp_celsius = convert_f_to_c(row[1])
        max_temp_celsius = convert_f_to_c(row[2])
        
        
        readable_date = convert_date(row[0])
        
        
        day_summary = (
            f"---- {readable_date} ----\n"
            f"  Minimum Temperature: {min_temp_celsius:.1f}°C\n"
            f"  Maximum Temperature: {max_temp_celsius:.1f}°C\n"
        )
        
        summary.append(day_summary)

    final_summary = "\n".join(summary) + "\n"
    
    return final_summary
