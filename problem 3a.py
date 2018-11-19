n = 600851475143
i = 2

while i * i < n:
    while n%i == 0:
        n = n / i
    i = i + 1

print (n)

#This explanation uses two while loops. The biggest thing to remember about while loops is that
# they run until they are no longer true.

#The outer loop states that while i * i isn't greater than n (because the largest prime factor
# will never be larger than the square root of n), add 1 to i after the inner loop runs.

#The inner loop states that while i divides evenly into n, replace n with n divided by i.
# This loop runs continuously until it is no longer true. For n=20 and i=2, n is replaced by 10,
# then again by 5. Because 2 doesn't evenly divide into 5, the loop stops with n=5 and the outer
# loop finishes, producing i+1=3.

#Finally, because 3 squared is greater than 5, the outer loop is no longer true and prints the result of n.