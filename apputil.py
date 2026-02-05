
def to_Binary(n):
    if n == 0:
        return "0"

    bits = [] 
    while n: 
        bits.append(str(n % 2))
        n //= 2
        return ''.join(reversed(bits))

print(to_Binary(10))

# update/add code below ...
