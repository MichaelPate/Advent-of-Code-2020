def main():
    lines = open('day3Input.txt').readlines()
    for line in lines:
        line = line.split('\n')[0]
        print(line)

if __name__=='__main__':
    main()