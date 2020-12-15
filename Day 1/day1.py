def main():
    lines = open('day1Input.txt').readlines()
    for l1 in lines:
        for l2 in lines:
            if (int(l1) + int(l2) == 2020):
                print("SUM: " + str(int(l1) + int(l2)))
                print("PRODUCT: " + str(int(l1) * int(l2)))




if __name__=='__main__':
    main()