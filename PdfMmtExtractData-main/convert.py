def toCsv(data : list) -> None:
    #turns data into csv
    with open("data.csv", "w+") as csvFile:
        for line in data:
            #get a nice string (clean "none items and replace with 0")
            cleaned_line = [item if item is not None else "/" for item in line]
            line = ";".join(cleaned_line)
            csvFile.write(line)