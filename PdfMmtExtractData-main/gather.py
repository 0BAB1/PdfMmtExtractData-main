import os
import pdfplumber as pb
import clear_sorted_data as clear
import sort
from clean_text import cleanId, cleanTxt

def getId(line):
    try :
        id = str(cleanId(repr(line[2])))
        typeOfTable = "normal"
    except:
        id = str(cleanId(repr(line[1])))
        typeOfTable = "buged"
    return id, typeOfTable

def getCotes(cotes, data_folder,toSort = False):
    #CLEAR ET RE TRIER TOUS LES FICHERS CONTENUS DANS "./data/"
    if toSort:
        clear.clear("sorted_data")
        sort.sort("pdf", data_folder)
        print("data ready ! Processing...")
    else:
        print("data was not sorted, pass true as a toSort arg to sort files")
    #declarations des cotes a surveiller
    #cotes = [40, 196] <-- désormais un argument de la function
    data_path = "sorted_data"
    model = os.listdir(data_path)[0]
    #initialiser le nom et les tolérances des cotes
    pdf = pb.open(os.path.join(data_path,model))
    data = {}
    for page in pdf.pages:
        tables = page.find_tables()
        for table in tables:
            table = table.extract()
            for line in table:
                try:
                    #extraire l'id de la ligne pui check s'il fait partie des cibles'
                    id, typeOfTable = getId(line)
                    if id in cotes and typeOfTable == "normal":
                        data[id] = {
                            "name" : repr(line[3]).split("\\n")[0] + "  " + repr(line[3]).split("\\n")[1],
                            "up" : cleanTxt(repr(line[5]).split("\\n")[0]),
                            "down" : cleanTxt(repr(line[5]).split("\\n")[1])
                        }
                    elif id in cotes and typeOfTable == "buged":
                        data[id] = {
                            "name" : repr(line[2]).split("\\n")[0] + "  " + repr(line[2]).split("\\n")[1],
                            "up" : cleanTxt(repr(line[4]).split("\\n")[0]),
                            "down" : cleanTxt(repr(line[4]).split("\\n")[1])
                        }
                except:
                    ...
    print("mesurements ready to read ! Processing ...")
    #Loop dans chaque fichier
    for filename in os.listdir(data_path):
        file_path = os.path.join(data_path,filename)
        pdf = pb.open(file_path)
        #lire chaque page (de chaque fichier)
        for page in pdf.pages:
            #extraire les tebleaux de la page
            tables = page.find_tables()
            for table in tables:
                table = table.extract()
                #lire chaque ligne (de chaque page) (de chque tableau)
                for line in table:
                    try:
                        #extraire l'id de la ligne pui check s'il fait partie des cibles'
                        id, typeOfTable = getId(line)
                        if id in data.keys() and typeOfTable == "normal":
                            mesure = str(line[7])
                            data[id][filename[:-4]] = mesure.replace(".",",")
                            print("measurement added !")
                        elif id in data.keys() and typeOfTable == "buged":
                            mesure = str(line[6])
                            data[id][filename[:-4]] = mesure.replace(".",",")
                            print("measurement added !")
                    except :
                        ...
        print(filename + " was successfully processed ! Processing next file ...")


    return data