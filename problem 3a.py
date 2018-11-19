#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

n = 600851475143
i = 2

while i * i < n:
    while n%i == 0:
        n = n / i
    i = i + 1

print (n)

#stack overflow: This explanation uses two while loops. The biggest thing to remember about while loops is that
# they run until they are no longer true.
#The outer loop states that while i * i isn't greater than n (because the largest prime factor
# will never be larger than the square root of n), add 1 to i after the inner loop runs.
#The inner loop states that while i divides evenly into n, replace n with n divided by i.
# This loop runs continuously until it is no longer true. For n=20 and i=2, n is replaced by 10,
# then again by 5. Because 2 doesn't evenly divide into 5, the loop stops with n=5 and the outer
# loop finishes, producing i+1=3.
#Finally, because 3 squared is greater than 5, the outer loop is no longer true and prints the result of n.


#personal comments: outer loop finds the i that goes into n evenly without any remainder (which triggers the inner loop)
#each iteration of the outer loop increases i by 1 until line 5 is satisfied
#at this point n is divided by the i that satisfies line 5 in order to determine the second multiple 
#have to accept the fact that the square of two numbers is less than 
