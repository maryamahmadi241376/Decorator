class PrimeIter:
    def __init__(self, m):
        self.m = m

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n < self.m:
            self.n += 1
            i = 2
            while i < (self.n // 2 + 1):
                if self.n % i == 0:
                    self.n = self.n + 1
                    if self.n >= self.m:
                        raise StopIteration
                    i = 1
                i += 1
            else:
                return self.n
        else:
            raise StopIteration


num = int(input("enter a number to see the prime numbers before it: "))
p = PrimeIter(num)
for i in p:
    print(i, end=' ')

# solution2 with generator

# def primes():
#     current = 1
#     while True:
#         current += 1
#         while True:
#             for i in range(2, current // 2 + 1):
#                 if current % i == 0:
#                     current += 1
#                     break
#             else:
#                 break
#         yield current
