import os
import pdfplumber as pb
import clear_sorted_data as clear
import sort
from clean_text import cleanId, cleanTxt

def getData(data_folder : str) -> list:
    #CLEAR ET RE TRIER TOUS LES FICHERS CONTENUS DANS "./data/"
    clear.clear("sorted_data")
    sort.sort(data_folder)
    print("data ready ! Processing...")
    
    #
    data_path = "sorted_data"
    #modele de data : [[ligne 1 du csv final], [ligne2], [etc...], etc...]
    data = []

    #Loop dans chaque fichier
    for filename in os.listdir(data_path):
        file_path = os.path.join(data_path,filename)
        pdf = pb.open(file_path)

        #lire chaque page
        for page in pdf.pages:
            #extraire les tebleaux de la page
            tables = page.find_tables()

            for table in tables:
                table = table.extract()
                #lire chaque ligne (de chaque page) (de chque tableau)
                for line in table:
                    data.append(line)

        print(filename + " was successfully processed ! Processing next file ...")

    return data