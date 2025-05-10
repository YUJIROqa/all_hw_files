import csv

with open('.vscode/lesson16/data.csv',newline='') as csv_file:
    file_data = csv.reader(csv_file)
    for row in file_data:
        print(row)

