import pandas as pd
import openpyxl


def criar_agenda(contatoscsv):
    df = pd.read_csv(contatoscsv)

    return df


agenda = criar_agenda('contacts.csv')

print(agenda)
