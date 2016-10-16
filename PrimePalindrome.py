def primes( x,  div ):
    if div == 1:
        return 1
    elif x%div == 0:
        return 0
    else:
        return primes( x, div-1 )



def isPalindrome( num ):
    print num
    num = str(num)
    if len(num) == 1:
        return True
    else:
        if num[0] == num[len(num)-1]:
            if len(num) == 2:
                return True
            else:
                num = num[1:(len(num)-1)]
                return isPalindrome( num )
        else:
            return False


primeList = []
for x in range(100,1000):
    primesCheck = primes(x, x-1)
    if primesCheck == 1:
        primeList.append(x)


primeProducts = []

for y in primeList:
    for z in primeList:
        primeProducts.append( y*z )
   

            

primePalindromes = []
for a in primeProducts:
    if isPalindrome( a ):
        primePalindromes.append( a )


numPal = []
for x in range(100,1000):
    for y in range(100,1000):
        if isPalindrome( x*y ):
            numPal.append( x*y )

print sorted(numPal)

