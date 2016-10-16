fibs = []

def fib(lit):

    if lit == 1 or lit == 2:
        return 1
    else:
        lit = fib(lit-1) + fib(lit-2)
        return lit


sum = 0
for x in range(1,34):
    check = fib(x)
    print check
    if check%2 == 0:
        print "EVEN",check
        sum += check
        
print "CHECK IT",sum
