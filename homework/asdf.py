def convertIntToRomanNum(inputNumber):

    digitValue = [1000, 900, 600, 500, 400, 100, 90, 60, 50, 40, 11, 10, 9, 6, 5, 4, 1]
    romanDict = {1000: "M",
                 900: "CM",
                 600: "DC",
                 500: "D",
                 400: "CD",
                 100: "C",
                 90: "XC",
                 60: "LX",
                 50: "L",
                 40: "XL",
                 11: "XI",
                 10: "X",
                 9: "IX",
                 6: "VI",
                 5: "V",
                 4: "IV",
                 1: "I"}

    resultStr = ""
    diffNum = inputNumber

    while ( diffNum > 0):
        indDV = 0
        subtractT = True

        while indDV < len(digitValue)-1 or subtractT:
            if diffNum-digitValue[indDV] < 0:
                indDV += 1
            else:
                diffNum = diffNum - digitValue[indDV]
                resultStr = resultStr + romanDict[digitValue[indDV]]
                subtractT = False
    return resultStr

print(convertIntToRomanNum(9999))

