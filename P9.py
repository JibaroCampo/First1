def adder(N):
    i = 0
    acumulator = 0
    while (i < N):
        i = i + 1
        acumulator = acumulator + i
    return acumulator

### practice##
print "adder(5):",adder(5)
print "adder(10):", adder(10)

##################
done = False
while not done:
    c = input ("Enter some value:")
    if c.isdigit(1):
       print "Is digit"
    elif c.isalpha():
        print " Is letter"
    else:
        done = True
print "Thanks for using this prgram"