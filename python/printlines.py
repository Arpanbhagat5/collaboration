with open("./logfile.log", "r") as logfile:
    for line in logfile:
        line = line.split("\n")
        print(line)