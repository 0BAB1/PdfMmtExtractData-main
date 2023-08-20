def toCsv(data : list, filter : bool = True) -> None:
    """turns data into csv, use filter (True by default) to get rid of symbols"""
    with open("data.csv", "w+") as csvFile:
        for line in data:
            #get a nice string (clean "none items and replace with 0" THEN join it)
            cleaned_line = [item if item is not None else "" for item in line]
            #i use repr to avoid unintended endline in the middle of a line, o also make the "\n" go away
            line = ";".join(cleaned_line).replace("\n", "")

            #filter symbols
            if filter:
                line = removeSymbols(line)   #clean text

            #write
            #so first we check for "emptyness"
            if not line.replace(";","") == "":
                #and then write line with enline
                csvFile.write(line + "\n")

def removeSymbols(txt : str):
    """removes symbols from text"""
    symbolsToRemove = "[]'\"*/" #symbols to remove
    for symbol in symbolsToRemove:
        txt = txt.replace(symbol, "")  #remove symbols
    
    return txt