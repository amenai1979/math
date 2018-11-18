binary={}
def binaryConverter(decimal=424):
    #the idea is to look for the maximum exponent of 2 that is still smaller than the number to convert
    i=0
    while (2**i <= decimal):
        i+=1
    if i==0:
        return
    else:
        binary[i-1]=True
        binaryConverter(decimal-2**(i-1))
binaryConverter(424)
print(binary)