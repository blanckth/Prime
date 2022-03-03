# Authur Salar Muhammadi
import time
#
##
###
####
#####
lastDigitR = [0, 2, 4, 5, 6, 8]


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

NASJunk = [3, 6, 9]


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

# Find Last Prime Divider AKA nearest prime number before half of the number
# chkNum = Current Number to check , lpd = last Prime divider of before number ,
#  pll = Prime List Current Length


def findLPD(chkNum, lpd, pll):
    for x in range(lpd, pll):
        if PrimeList[x] > int(chkNum/2):
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


def findPD(chkNum, lpd):
    if lastDigR(chkNum):
        return True
    if pureJunk(chkNum):
        return True
    for x in range(lpd+1):
        if (chkNum % PrimeList[x]) == 0:
            return True
    return False

#####
####
###
##
#


PrimeList = [2, 3]


def initPrimeList(pCount):
    Number = 4
    lastP = 0
    while len(PrimeList) < (pCount - 2):
        lastP = findLPD(Number, lastP, len(PrimeList))
        if not findPD(Number, lastP):
            PrimeList.append(Number)
        Number += 1


def initPrimeCheck(Number):
    for x in PrimeList:
        if (Number % x) == 0:
            return False
        if x > (Number // 2):
            return True
    return True


pow2L = []


def pow2Find(lowRange, powRange):
    for x in range(lowRange, powRange):
        pow2 = 2 ** x
        ppx = PNAS(pow2)
        if ppx == 1 or ppx == 4 or ppx == 7:
            pass
        else:
            p2p = pow2 - 1
            if initPrimeCheck(p2p):
                pow2L.append(p2p)


pits = time.time()
initpl = 888
initPrimeList(initpl)
pite = time.time()
pit = pite - pits
print(PrimeList)
print(f'init Prime List Time : {pit}')
p2pts = time.time()
plr = 8880
phr = 8889
phrr = phr - 1
prange = phr - plr - 1
pow2Find(plr, phr)
p2pte = time.time()
p2pt = p2pte - p2pts
print(pow2L)
lenpow2l = len(pow2L)
print(lenpow2l)
print(f'2^([{plr} to {phrr}]) -1 => {prange} Number(s) Check with {initpl} Prime Numbers Before ++> Find Probably {lenpow2l} Prime(s).')
print(f'init Prime List Time : {pit} for {initpl} Primes')
print(f'Power2Prime List Time : {p2pt}')
foundPerc = lenpow2l/prange
print(f'{lenpow2l} X 100 / {prange} = {foundPerc:.2%}')
lastpl = len(str(pow2L[lenpow2l - 1]))
print(f'Last Found Prime Number Has - {lastpl} - Digit.')
