from gather import getData
from convert import toCsv

if __name__ == "__main__":
    data = getData("data/")
    toCsv(data)