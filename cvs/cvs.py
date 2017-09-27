import csv

html_output = ''
names = []


with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    # we don't want first two lines
    next(csv_data)
    next(csv_data)

    for line in csv_data:
        print(line)
