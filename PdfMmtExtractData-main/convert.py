def toCsv(data : list) -> None:
    #turns data into csv
    with open("data.csv", "w+") as csvFile:
        for line in data:
            #get a nice string
            line = line.join(";")
            csvFile.write(line)