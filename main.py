import pandas as pd


def read_csv(file_name):
    """
    reads the cv and puts into a panda object
    :param file_name: the name of the file
    :return: the panda object
    """
    file_data = pd.read_csv(file_name)

    for i in file_data.columns:

        if type(file_data[i][0]) == str:
            file_data[i] = file_data[i].astype('category').cat.codes

    print(file_data.corr(method='kendall'))

if __name__ == '__main__':
    read_csv("mlb_players.csv")
