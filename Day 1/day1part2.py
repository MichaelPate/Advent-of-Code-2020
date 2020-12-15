def main():
    lines = open('day1Input.txt').readlines()
    for l1 in lines:
        for l2 in lines:
            for l3 in lines:
                n1 = int(l1)
                n2 = int(l2)
                n3 = int(l3)
                if (n1 + n2 + n3 == 2020):
                    print(n1 * n2 * n3)
                    break




if __name__=='__main__':
    main()