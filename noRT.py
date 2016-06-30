def rt():
    file = open("1.gender","r")
    file_out = open("noRT1.txt","w")
    for line in file:
        lijn = line.split()
        if lijn[2] != "RT":
            file_out.write(line)
    file_out.close()
                

if __name__ == "__main__":
    rt()
