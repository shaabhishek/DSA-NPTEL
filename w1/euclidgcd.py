def gcd(a,b):
    if a < b:
        (a,b) = (b,a)
    if a%b == 0:
        return (b)
    return (gcd(b, a%b))

# print(gcd(989, 11))
print(gcd(899123112313,991234999))

