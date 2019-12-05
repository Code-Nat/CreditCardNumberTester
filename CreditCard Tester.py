def combine (num):
    num = int (num)
    print (int(num), end=" ")
    if (num > 9):
        num = num/10 + num%10
    print (int(num))
    return int(num)

def CreditTester(cNum):
    cNum = cNum.replace(" ","")
    cNum = [int(char) for char in cNum]
    for i in range (0,len(cNum),2):
        cNum[i] = combine(int(cNum[i])*2)
    num = 0
    for i in range(len(cNum)):
        num += cNum[i]
    print (num)
    if (num%10):
        return False
    return True

print ("The credit card number is: " + str(CreditTester(input("Please input your credit card number: "))))