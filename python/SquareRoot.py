# this little python program that calcuates the square root of a number based on the estimation method.
# Wewill puck a integer whose square is the closest but smaller than the number in question and one whose square root is bigger
# we will then average those numbers and try to approach the number.

def findRootBound(n: int) -> (int,int):
    i: int = 0
    lowerBound: int
    while i ** 2 <= n:
        lowerBound = i
        i += 1
    upperBound=i
    return (lowerBound, upperBound)



def squareRoot(n: int, niter: int=10 ) -> float:
    lowerBound,upperBound=findRootBound(n)[0],findRootBound(n)[1]
    while niter >0:
        candidate: float=(lowerBound+upperBound)/2
        if candidate**2 == float(n):
            return candidate
        elif candidate**2 > float(n):
            upperBound=candidate
        else:
            lowerBound=candidate
        niter -= 1
    assert isinstance(candidate, float)
    return candidate
    
print(squareRoot(2,40))
