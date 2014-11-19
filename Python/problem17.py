def countletters(word):
    sum = 0
    for letter in word:
        if not letter == "-":
            sum = sum + 1
    return sum

def countphrase(phrase):
    sum = 0
    words = phrase.split()
    for word in words:
        sum = sum + countletters(word)
    return sum

def inttotext(n):
    string = str(n)
    length = len(string)
    result = ""
    hasand = length > 2
    andadded = False
    if length > 3:
        if string[-4] == "1":
            result = result + " one thousand"
        if string[-4] == "2":
            result = result + " two thousand"
        if string[-4] == "3":
            result = result + " three thousand"
        if string[-4] == "4":
            result = result + " four thousand"
        if string[-4] == "5":
            result = result + " five thousand"
        if string[-4] == "6":
            result = result + " six thousand"
        if string[-4] == "7":
            result = result + " seven thousand"
        if string[-4] == "8":
            result = result + " eight thousand"
        if string[-4] == "9":
            result = result + " nine thousand"
    if length > 2:
        if string[-3] == "1":
            result = result + " one hundred"
        if string[-3] == "2":
            result = result + " two hundred"
        if string[-3] == "3":
            result = result + " three hundred"
        if string[-3] == "4":
            result = result + " four hundred"
        if string[-3] == "5":
            result = result + " five hundred"
        if string[-3] == "6":
            result = result + " six hundred"
        if string[-3] == "7":
            result = result + " seven hundred"
        if string[-3] == "8":
            result = result + " eight hundred"
        if string[-3] == "9":
            result = result + " nine hundred"
    if length > 1:
        if string[-2] == "0":
            hasand = False
        if hasand:
            result = result + " and"
            andadded = True
        if string[-2] == "1":
            result = result + tentonineteen(string[-2]+string[-1])
            return result
        if string[-2] == "2":
            result = result + " twenty"
        if string[-2] == "3":
            result = result + " thirty"
        if string[-2] == "4":
            result = result + " forty"
        if string[-2] == "5":
            result = result + " fifty"
        if string[-2] == "6":
            result = result + " sixty"
        if string[-2] == "7":
            result = result + " seventy"
        if string[-2] == "8":
            result = result + " eighty"
        if string[-2] == "9":
            result = result + " ninety"
    hasand = length > 2
    if string[-1] == "0":
        hasand = False
    if hasand and not andadded:
        result = result + " and "
    if string[-1] == "1":
        result = result + "one" 
    if string[-1] == "2":
        result = result + "two"
    if string[-1] == "3":
        result = result + "three"
    if string[-1] == "4":
        result = result + "four"
    if string[-1] == "5":
        result = result + "five"
    if string[-1] == "6":
        result = result + "six"
    if string[-1] == "7":
        result = result + "seven"
    if string[-1] == "8":
        result = result + "eight"
    if string[-1] == "9":
        result = result + "nine"
    return result

def tentonineteen(string):
    if string[-1] == "0":
        return " ten"
    if string[-1] == "1":
        return " eleven"
    if string[-1] == "2":
        return " twelve"
    if string[-1] == "3":
        return " thirteen"
    if string[-1] == "4":
        return " fourteen"
    if string[-1] == "5":
        return " fifteen"
    if string[-1] == "6":
        return " sixteen"
    if string[-1] == "7":
        return " seventeen"
    if string[-1] == "8":
        return " eighteen"
    if string[-1] == "9":
        return " nineteen"

def countlettersuptoandincluding(n):
    result = 0
    for i in range(0,n+1):
        result = result + countphrase(inttotext(i))
    return result
 
print(countlettersuptoandincluding(int(input("How high? "))))
