import re

def main():
    with open("day4Input.txt") as f:
        lines = f.read()
    passports = lines.split("\n\n")
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    validCount = 0
    
    for p in passports:
        p = p.replace('\n', ' ')
        # cid is optional, the rest are not
        #print(p)
        valid = True
        for field in fields:
            if field not in p:
                #print("MISSING FIELD " + field)
                valid = False
                break

        fieldData = p.split(" ")
        for dataPiece in fieldData:
            f = dataPiece.split(":")[0]
            d = dataPiece.split(":")[1]
            if (f == "byr"):
                if len(d) != 4: 
                    valid = False
                    #print("INVALID BIRTH YEAR")
                    
                elif int(d) < 1920 or int(d) > 2002: 
                    valid = False
                    #print("BIRTH YEAR OUT OF RANGE")
                    
            elif (f == "iyr"):
                if len(d) != 4: 
                    valid = False
                    #print("INVALID ISSUE YEAR")
                elif int(d) < 2010 or int(d) > 2020: 
                    valid = False   
                    #print("ISSUED YEAR OUT OF RANGE")                    
            elif (f == "eyr"):
                if len(d) != 4: 
                    valid = False
                    #print("INVALID EXPIRATION YEAR")
                elif int(d) < 2020 or int(d) > 2030: 
                    valid = False   
                    #print("EXPIRATION YEAR OUT OF RANGE")
            elif (f == "hgt"):
                #if ("cm" not in d) or ("in" not in d): valid = False
                num = int(re.sub("[^0-9]", "", d))
                if ("cm" in d):
                    if num < 150 or num > 193: 
                        valid = False
                        #print("INVALID NUMBER OF CENTIMETERS")
                elif ("in" in d):
                    if num < 59 or num > 76: 
                        valid = False
                        #print("INVALID NUMBER OF INCHES")
                else: 
                    valid = False
                    #print("MISSING HEIGHT UNIT")
            elif (f == "hcl"):
                if "#" not in d:
                    valid = False
                    #print("INVALID HAIR COLOR")
                else:
                    d = d.split("#")[1]
                    if (len(d) != 6):
                        None
                        #print("WRONG NUMBER OF COLOR DIGITS")
            elif (f == "ecl"):
                #amb blu brn gry grn hzl oth
                colors = ["amb","blu","brn","gry","grn","hzl","oth"]
                if not any(s in d for s in colors): 
                    valid = False
                    #print("INVALID EYE COLOR")
            elif (f == "pid"):
                if(len(d) != 9):
                    valid = False
                    #print("INVALID PID")
        if valid: 
            #print("THIS PASSPORT IS VALID")
            validCount += 1
        else:
            None 
            #print("THIS PASSPORT IS INVALID")
    
        #print("\n")
    print(validCount)

if __name__=='__main__':
    main()