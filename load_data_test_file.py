import csv

def load_data_from_csv(example_one):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    new_list = []
    with open(example_one, encoding="utf-8") as my_file:
        csv_reader = csv.reader(my_file)
        next(csv_reader) # skip headers (first row)

        for row in csv_reader:
            new_list.append(row)

    return(new_list)

example_one = [
["2021-07-02T07:00:00+08:00", 49, 67],
["2021-07-03T07:00:00+08:00", 57, 68],
["2021-07-04T07:00:00+08:00", 56, 62],
["2021-07-05T07:00:00+08:00", 55, 61],
["2021-07-06T07:00:00+08:00", 53, 62]
]
print(load_data_from_csv(example_one))