import os

def clear(toClear):
    data_path = toClear

    for filename in os.listdir(data_path):
        os.remove(os.path.join(data_path,filename))