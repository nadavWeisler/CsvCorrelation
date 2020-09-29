import csv

def read_csv(file_name):

    # opens the csv file and reads it
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        for row in readCSV:
            for col in row:
                print(col)


if __name__ == '__main__':
    read_csv("mlb_players.csv")
