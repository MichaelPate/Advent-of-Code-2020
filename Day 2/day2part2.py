def main():
    lines = open('day2Input.txt').readlines()
    validCount = 0
    for line in lines:
        pos1 = int(line.split('-')[0]) - 1
        pos2 = int(line.split('-')[1].split(' ')[0]) - 1
        targetChar = line.split(' ')[1].split(':')[0]
        ps = line.split(' ')[2]

        if ps[pos1] == targetChar:
            if ps[pos2] != targetChar:
                validCount += 1
        elif ps[pos1] != targetChar:
            if ps[pos2] == targetChar:
                validCount += 1
        print(ps[pos1] + '\t' + ps[pos2])
        #count = line.count(targetChar)-1
        #print(count)
        #if count <= maxOccur and count >= minOccur:
        #    validCount += 1
    print(validCount)

if __name__=='__main__':
    main()