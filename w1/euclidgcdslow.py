def gcd(a,b):
    if a < b:
        (a,b) = (b,a)

    if a%b == 0:
        return (b)
    diff = a-b;

    return( gcd(max(b, diff), min(b, diff)) );

# print(gcd(989, 11))
print(gcd(899123112313,991234999))
# print(gcd(18e9, 11))