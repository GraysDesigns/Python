file = open("./2021Day3/input.txt", "r")
content = file.read()
arraySTR = content.split("\n")

def splits(word):
    return [char for char in word]

arrayCHAR = []
for i in arraySTR:
    arrayCHAR.append(splits(i))

zeroArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zeroArraylen = len(zeroArray)
totalIndex = 0

for i in arrayCHAR:
    for j in i:
        pos = totalIndex % zeroArraylen
        if pos == 0 and j == '0':
            zeroArray[pos] += 1
        elif pos == 1 and j == '0':
            zeroArray[pos] += 1
        elif pos == 2 and j == '0':
            zeroArray[pos] += 1
        elif pos == 3 and j == '0':
            zeroArray[pos] += 1
        elif pos == 4 and j == '0':
            zeroArray[pos] += 1  
        elif pos == 5 and j == '0':
            zeroArray[pos] += 1
        elif pos == 6 and j == '0':
            zeroArray[pos] += 1
        elif pos == 7 and j == '0':
            zeroArray[pos] += 1
        elif pos == 8 and j == '0':
            zeroArray[pos] += 1  
        elif pos == 9 and j == '0':
            zeroArray[pos] += 1  
        elif pos == 10 and j == '0':
            zeroArray[pos] += 1  
        elif pos == 11 and j == '0':
            zeroArray[pos] += 1            
        totalIndex += 1
#zeroArray = [486, 490, 503, 513, 498, 510, 491, 475, 489, 528, 492, 494]
majority = totalIndex/len(zeroArray)/2
gammaArrayINT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
epsilonArrayINT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#populates the gamma array with the majority digit based on zeroCount
index = 0
for i in zeroArray:
    if i > majority:
        gammaArrayINT[index] = 0
    else:
        gammaArrayINT[index] = 1
    index += 1

#inverts gamma (G1 = E0)
index = 0
for i in gammaArrayINT:
    if gammaArrayINT[index] == 0:
        epsilonArrayINT[index] = 1
    else:
        epsilonArrayINT[index] = 0
    index += 1

#print('  gammaArrayINT = ' + str(gammaArrayINT))
#print('epsilonArrayINT = ' + str(epsilonArrayINT))

def BINArrayToINT (array):
    return int("".join(str(x) for x in array), 2)

gammaTotal = BINArrayToINT (gammaArrayINT)
epsilonTotal = BINArrayToINT (epsilonArrayINT)

#print('  gammaArrayINT = ' + str(gammaArrayINT))
#print('epsilonArrayINT = ' + str(epsilonArrayINT))

#print('  gammaTotal = ' + str(gammaTotal))
#print('epsilonTotal = ' + str(epsilonTotal))

powerConsumption = gammaTotal * epsilonTotal

#print('powerConsumption = ' + str(powerConsumption))
matchArray = []
matches = 0

def gammaFilter(array_of_array_of_chars, gamma_key, index):
    matchesGammaIndex = []
    for i in range(0, len(array_of_array_of_chars)):
        currentArray = array_of_array_of_chars[i]
        #print('currentArray = ' + str(currentArray))
        #print('index = ' + str(index))
        #print('currentArray[index] = ' + str(currentArray[index]))
        #print('gamma_key[index] = ' + str(gamma_key[index]))
        if currentArray[index] == str(gamma_key[index]):
            #print('MATCH FOUND')
            matchesGammaIndex.append(currentArray)
    return matchesGammaIndex



Gamma0Match = gammaFilter(arrayCHAR, gammaArrayINT, 0)
Gamma1Match = gammaFilter(Gamma0Match, gammaArrayINT, 1)
Gamma2Match = gammaFilter(Gamma1Match, gammaArrayINT, 2)
Gamma3Match = gammaFilter(Gamma2Match, gammaArrayINT, 3)
Gamma4Match = gammaFilter(Gamma3Match, gammaArrayINT, 4)
Gamma5Match = gammaFilter(Gamma4Match, gammaArrayINT, 5)
Gamma6Match = gammaFilter(Gamma5Match, gammaArrayINT, 6)
Gamma7Match = gammaFilter(Gamma6Match, gammaArrayINT, 7)
Gamma8Match = gammaFilter(Gamma7Match, gammaArrayINT, 8)
print('------------------------------------------------')
for i in range(0, len(Gamma8Match)):
    print('Gamma8@' + str(i) + ': ' + str(Gamma8Match[i]))
O2genRatingBIN = ['1', '1', '0', '0', '1', '0', '1', '1', '1', '1', '0', '0']
O2genRatingINT = BINArrayToINT(O2genRatingBIN)
print('gamma: ' + str(gammaArrayINT))
print('O2 Gen. Rating: ' + str(O2genRatingINT))

Eps0 = gammaFilter(arrayCHAR, epsilonArrayINT, 0)
Eps1 = gammaFilter(Eps0, epsilonArrayINT, 1)
Eps2 = gammaFilter(Eps1, epsilonArrayINT, 2)
Eps3 = gammaFilter(Eps2, epsilonArrayINT, 3)
Eps4 = gammaFilter(Eps3, epsilonArrayINT, 4)
Eps5 = gammaFilter(Eps4, epsilonArrayINT, 5)
Eps6 = gammaFilter(Eps5, epsilonArrayINT, 6)
Eps7 = gammaFilter(Eps6, epsilonArrayINT, 7)
Eps8 = gammaFilter(Eps7, epsilonArrayINT, 8)
Eps9 = gammaFilter(Eps8, epsilonArrayINT, 9)
Eps10= gammaFilter(Eps9, epsilonArrayINT, 10)
Eps11= gammaFilter(Eps10, epsilonArrayINT, 11)
for i in range(0, len(Eps8)):
    print('Eps8@' + str(i) + ': ' + str(Eps8[i]))
print('epsilon: ' + str(epsilonTotal))   
Co2ScrubRatingBIN = ['0', '0', '1', '1', '0', '1', '0', '0', '0', '1', '0', '0']
Co2ScrubRatingINT = BINArrayToINT(Co2ScrubRatingBIN)

print('CO2 Scrub Rating: ' + str(Co2ScrubRatingINT))

print('life support: ' + str(O2genRatingINT*Co2ScrubRatingINT))