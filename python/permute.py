
__author__ = 'amenai@amenai.net'

#maliste=['a','b','c']
mylist='abcdef'
def permute(mylist):
    permutations=[]
    for e in mylist:
        l=list(mylist)
        if len(l)==1:
            return l
        l.remove(e)
        P=permute(l)
        for p in P:
            permutations.append(e+p)
    return permutations
print(permute(mylist))