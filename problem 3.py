#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?


number = 600851475143
#i = 1
#prime_factors = []


#while i <= number:
#    if number % i == 0:
#        prime_factors.append(i)
#        i = i + 1
#    else:
#        i = i + 1

# = (len(prime_factors) - 1)
#print(prime_factors[-1])

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

print(largest_prime_factor(number))

#this was an interesting learning opportunity for me on how much I don't know
#The code I originally wrote to solve this problem is so inefficient because of the amount
#of calculations it has to go through, that I was never able to get it to print a solution
#even after several minutes of waiting. That code is included above as a comment for reference
#this working piece of code listed above is from stackoverflow and I have worked through understanding
#the math behind it
