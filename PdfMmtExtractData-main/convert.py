import pandas as pd

def toCsv(data):
    pd.DataFrame(data).to_csv("data.csv", sep=";")
    print("Traitement terminé !")