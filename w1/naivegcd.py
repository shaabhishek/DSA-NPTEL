def gcd(a,b):
    for i in range(min(a,b),0,-1):
        if a%i == 0 and b%i == 0:
            return (i)
    

# print(gcd(899123113,99999))
print(gcd(899123112313,991234999)) #v.v.slow
