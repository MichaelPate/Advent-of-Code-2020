def main():
    lines = open('day3Input.txt').readlines()

    product = 1
    product *= computePath(lines, 1, 1)
    product *= computePath(lines, 3, 1)
    product *= computePath(lines, 5, 1)
    product *= computePath(lines, 7, 1)
    product *= computePath(lines, 1, 2)
    print(product)
    #print(computePath(lines, 3, 1))


def computePath(array, colInc, rowInc):
    row = 0
    col = 0
    count = 0
    while row < len(array):
        line = array[row].split('\n')[0]
        if line[col % len(line)] == '#': count += 1
        row += rowInc
        col += colInc
    return count


if __name__=='__main__':
    main()