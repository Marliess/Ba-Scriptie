def findUniek():
    file = open("maletags.txt","r")
    file_match = open("femaletags.txt","r")
    dictio = []
    for line in file:
        a, b = line.split()
        dictio.append(b)

    for line in file_match:
        if line.split()[1] not in dictio:
            print(line)
        
if __name__ == "__main__":
    findUniek()
