#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?


number = 600851475143
i = 1
prime_factors = []


while i <= number:
    if number % i == 0:
        prime_factors.append(i)
        i = i + 1
    else:
        i = i + 1

# = (len(prime_factors) - 1)
print(prime_factors[len(prime_factors) - 1])

