import pandas as pd

def toCsv(cotes):
    pd.DataFrame(cotes).to_csv("data.csv", sep=";")
    print("Traitement terminé !")