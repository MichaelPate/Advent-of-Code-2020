def main():
    lines = open('day2Input.txt').readlines()
    validCount = 0
    for line in lines:
        minOccur = int(line.split('-')[0])
        maxOccur = int(line.split('-')[1].split(' ')[0])
        targetChar = line.split(' ')[1].split(':')[0]
        count = line.count(targetChar)-1
        print(count)
        if count <= maxOccur and count >= minOccur:
            validCount += 1
    print(validCount)

if __name__=='__main__':
    main()