powerer = 2
powered = 2
powering = 0
sentence = []
random = 3

while 0 == 0 :
    #print(powering)
    if powerer == 6 :
        powered = powered + 1
        powerer = 2
        powering = powered ** powerer
        checker = powerer ** powered
        sentence.append(powering)
        powerer = powerer + 1
        if powered >= 6 :
            break
    powering = powered ** powerer
    powerer = powerer + 1
    sentence.append(powering)


sentence = set(sentence)
sentencea = len(sentence)
print(sentencea)
