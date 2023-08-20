import os
import shutil
def sort(mode, data_folder, min = 0, max = 99999999):
    data_path = data_folder
    destination_folder = "sorted_data"

    if mode == "xlsx":
        for filename in os.listdir(data_path):
            
            file_path = file_path = os.path.join(data_path, filename)

            if os.path.isfile(file_path) and filename[-4:] == "xlsx" :
                try:
                    file_num = int(filename[-8:-5])
                except:
                    try :
                        file_num = int(filename[-7:-5])
                    except:
                        ...
                if file_num > 50:
                    shutil.copy2(file_path, os.path.join(destination_folder, str(file_num) + ".xlsx"))
                    
    elif mode=="pdf":
        
        for filename in os.listdir(data_path):
        
            file_path = file_path = os.path.join(data_path, filename)
            if os.path.isfile(file_path) and filename[-3:] == "pdf":
                    try:
                        file_num = int(filename[-7:-4])
                        if file_num >= min and file_num <= max :
                            shutil.copy2(file_path, os.path.join(destination_folder, str(file_num) + ".pdf"))
                    except:
                        ...
