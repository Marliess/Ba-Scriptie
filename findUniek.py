def findUniek():
    f = open("femaletags.txt","r")
    f_match = open("maletags.txt","r")
    dictio = []
    for line in f:
        a, b = line.split()
        dictio.append(b)

    for line in f_match:
        if line.split()[1] not in dictio:
            print(line)
        



if __name__ == "__main__":
    findUniek()
