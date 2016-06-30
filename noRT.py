import sys

def rt():
    file = open("1.gender","r")
    for line in file:
        lijn = line.split()
        if lijn[2] != "RT":
            print(line)
                

if __name__ == "__main__":
    rt()
