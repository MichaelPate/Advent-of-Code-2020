def main():
    with open("day4Input.txt") as f:
        lines = f.read()
    passports = lines.split("\n\n")
    
    for p in passports:
        p = p.replace('\n', ' ')
        print(p)
        print("\n")


if __name__=='__main__':
    main()