import pandas as pd
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)
# df_bellevue = pd.read_csv('./data/.../mydata.csv')  # you can also reference locally stored data

def fibonacci(n):
    """Return the nth Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fibonacci(9))  

def to_binary(n):
    """Convert an integer to its binary representation as a string."""
    if n == 0:
        return "0"
    bits = []
    while n:
        bits.append(str(n % 2))
        n //= 2
    return ''.join(reversed(bits))

print(to_binary(10))

def task_i():
    




