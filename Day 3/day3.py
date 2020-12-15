def main():
    lines = open('day3Input.txt').readlines()

    lineLength = 0
    treeCount = 0
    row = 0
    column = 0
    stringPos = 0

    for line in lines:
        line = line.split('\n')[0]
        lineLength = len(line)
        
        # Adapt column into stringPos
        stringPos = column % lineLength
        #print(str(stringPos) + "\t" + line[stringPos])
        if line[stringPos] == '#': treeCount += 1
        column += 3
    
    print(treeCount)


if __name__=='__main__':
    main()