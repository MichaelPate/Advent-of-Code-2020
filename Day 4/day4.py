def main():
    with open("day4Input.txt") as f:
        lines = f.read()
    passports = lines.split("\n\n")
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    validCount = 0
    
    for p in passports:
        p = p.replace('\n', ' ')
        # cid is optional, the rest are not
        print(p)
        hasAll = True
        for field in fields:
            if field not in p:
                hasAll = False
                break
        if hasAll: validCount += 1
    
        print("\n")
    print(validCount)

if __name__=='__main__':
    main()