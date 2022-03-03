# Authur Salar Muhammadi
import time
# Prime numbers before an variable
n = input("Enter the Positive Integer Value : ")
while not n.isnumeric() or int(n) < 2:
    n = input("Enter the VALID Positive Integer Larger than 1 : ")
# Pure Numbers List
pureNums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Even Digit Numbers
lastDigitR = [0, 2, 4, 5, 6, 8]
NASJunk = [3, 6, 9]
pList = [2]
n = int(n)
#
##
###
####
#####

# Find Last Prime Divider AKA nearest prime number before half of the number
# chkNum = Current Number to check , lpd = last Prime divider of before number ,
#  pll = Prime List Current Length

# Find Last Prime INDEX that may be the divider of the number


def findLPD(chkNum, lpd, pll):
    for x in range(lpd, pll):
        if pList[x] > int(chkNum/2):
            return x - 1

#####
####
###
##
#

#
##
###
####
#####

# Check all the Prime numbers of the list before the half of the number wether can divide the number Clean or not


def findPD(chkNum, lpd):
    for x in range(lpd+1):
        if (chkNum % pList[x]) == 0:
            return True
    return False

#####
####
###
##
#

#
##
###
####
#####

# Check the last digit of the number that cannot be Even Number or 0 , 5 as a Prime number


def lastDigR(chkNum):
    digL = len(str(chkNum)) - 1
    ld = str(chkNum)[digL]
    for x in lastDigitR:
        if ld == x:
            return True
    return False

#####
####
###
##
#

#
##
###
####
#####


# Number Addition Sum


def NAS(num):
    nas = 0
    for x in range(len(str(num))):
        xx = int(str(num)[x])
        if xx == 9 or xx == 0:
            pass
        else:
            nas += xx
    return nas


# Pure Number Addition Sum


def PNAS(num):
    Num = num
    while len(str(Num)) != 1:
        Num = NAS(Num)
    return Num

#####
####
###
##
#

#
##
###
####
#####

# Numbers that the digitSum of them is 3 or 6 or 9 Can divide to 3 and so cannot be Prime


def pureJunk(chkNum):
    for x in NASJunk:
        if PNAS(chkNum) == x:
            return True
    return False

#####
####
###
##
#

#
##
###
####
#####


print(PNAS(n))
startTime = time.time()
if n >= 3:
    pList.append(3)
if n > 3:
    lastP = 0
    for x in range(4, n+1):
        if not lastDigR(x):
            if not pureJunk(x):
                lastP = findLPD(x, lastP, len(pList))
                if not findPD(x, lastP):
                    pList.append(x)
endTime = time.time()
print()
print(pList)
print()
ppList = []
for x in pList:
    ppList.append(PNAS(x))
print(ppList)
print()
AllTime = endTime - startTime
print("Founds Prime Numbers : ", len(pList),
      f" in just {AllTime} Seconds.")
