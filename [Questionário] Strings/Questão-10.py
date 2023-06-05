def decimal2bin(n):
    code = bin(n)
    code = code[2:]
    code = code.zfill(8)
    return str(code)

def reverse(s):
    rev = s[::-1]
    return rev

def decodifica(codeBinario, codeUnario): #funcão pincipal que decodifica.
    decimal = len(codeUnario)
    if decimal % 2 == 0:
        zero = codeBinario[-1]
        for i in codeBinario:
            if i != zero:
                um = i
                break
    else:
        um = codeBinario[-1]
        for i in codeBinario:
            if i != um:
                zero = i
                break
    return zero, um
    
def converte2alien(zero, um, code):
    decimal = int(code)
    binário = decimal2bin(decimal)
    alien = ""
    for i in binário:
        if i == "0":
            alien += zero
        elif i == "1":
            alien += um
    return alien

def converte2decimal(zero, um, code):
    decimal = "0b"
    for i in code:
        if i == zero:
            decimal += "0"
        elif i == um:
            decimal += "1"
    return int(decimal, 2)

def isBigEndian(códigoBinárioAlien, códigoUnárioAlien):
    decimal = len(códigoUnárioAlien)
    if decimal % 2 == 0:# par
        zero = códigoBinárioAlien[-1]
        for i in códigoBinárioAlien:
            if i != zero:
                um = i
                break
    else:#impar
        um = códigoBinárioAlien[-1]
        for i in códigoBinárioAlien:
            if i != um:
                zero = i
                break
    #print("zero",zero)
    #print("um",um)
    #zero e um codificados
    binario = "0b"
    for i in códigoBinárioAlien:
        if i == zero:
            binario += "0"
        elif i == um:
            binario += "1"
    #print("binario",binario)
    if int(binario, 2) == decimal:
        return True
    else:
        return False   
    
def BigEndian2LittleEndian(códigoBinárioAlien):
    return reverse(códigoBinárioAlien)

def LittleEndian2BigEndian(códigoBinárioAlien):
    return reverse(códigoBinárioAlien)
    
códigoBinário, códigoUnário = input().split()
n = len(códigoUnário)
bigEndian = isBigEndian(códigoBinário, códigoUnário)
#print(bigEndian)
if not(bigEndian): # revertemos se é não big.
    códigoBinário = BigEndian2LittleEndian(códigoBinário)
zero, um = decodifica(códigoBinário, códigoUnário) #ok
#print("zero",zero)
#print("um",um)
for i in range(n):
    code = input()
    if code.isdigit():# numero >> alien
        if bigEndian:
            print(converte2alien(zero, um, code))
        else:
            print(LittleEndian2BigEndian(converte2alien(zero, um, code)))
    else: #alien >> numero 
        if bigEndian:
            print(converte2decimal(zero, um, code))
        else:
            code = BigEndian2LittleEndian(code)
            print(converte2decimal(zero, um, code))
