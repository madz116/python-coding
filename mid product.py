n=int(input("Enter a number: "))
t=n
numLen=0
while t>0:
    numLen=numLen+1
    t=int(t/10)

if numLen>=4:
    numLen=int(numLen/2)
    chk=0
    while n>0:
        rem=n%10
        if chk==numLen:
            midOne=rem
        elif chk==(numLen-1):
            midTwo=rem
        n=int(n/10)
        chk=chk+1
    prod=midOne*midTwo
    print("Product of the miidle digits: ",prod)
else:
    print("Its not a 4 or more than a 4 digit number!")